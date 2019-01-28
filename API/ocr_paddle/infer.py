# coding: utf-8

from __future__ import print_function

import os
import time

import numpy as np
import paddle.fluid as fluid
from PIL import Image, ImageEnhance, ImageFilter

from .crnn_ctc_model import ctc_infer
from .utility import get_ctc_feeder_data


class Arg:
    def __init__(self):
        current_file_path = os.path.realpath(__file__)
        current_dir_path = os.path.dirname(current_file_path)
        model_path = os.path.join(current_dir_path, "models", "model_14000")
        self.model = "crnn_ctc"
        self.use_gpu = True
        self.model_path = model_path
        self.image_path = None
        #########
        self.batch_size = 1
        self.input_images_dir = None
        self.input_images_list = None
        self.iterations = 0
        self.dict = None
        self.skip_batch_num = 0


# 定义 并且收集参数
args = Arg()
get_feeder_data = None
place = None
exe = None
ids = None


def binarizing(im, threshold=200):
    im = im.convert("L")
    pixdata = im.load()
    w, h = im.size
    for j in range(h):
        for i in range(w):
            if pixdata[i, j] < threshold:
                pixdata[i, j] = 0
            else:
                pixdata[i, j] = 255
    return im


def crop(im, box=(0, 0, 160, 48)):
    box = (0, 0, 160, 48)
    return im.crop(box)


def prepare_inferenc():
    global get_feeder_data, place, exe, ids
    infer = ctc_infer
    get_feeder_data = get_ctc_feeder_data

    eos = 1
    sos = 0
    num_classes = 95
    data_shape = [1, 48, 160]    # [1, 48, 512]

    # define network
    images = fluid.layers.data(name='pixel', shape=data_shape, dtype='float32')
    ids = infer(images, num_classes, use_cudnn=True)

    # prepare environment
    place = fluid.CUDAPlace(0)
    exe = fluid.Executor(place)
    exe.run(fluid.default_startup_program())

    # load init model
    filename = "/home/zzccchen/peggy/PAPI/ocr_paddle/models/model_14000"
    model_dir = "/home/zzccchen/peggy/PAPI/ocr_paddle/models"
    fluid.io.load_params(exe, dirname=model_dir, filename=filename)
    print("Init model from: %s." % filename)


prepare_inferenc()


def inference(img):
    """OCR inference"""

    # prepare data
    def load_image(img):
        im = crop(img)
        img = binarizing(img)
        img = img.filter(ImageFilter.MaxFilter(3))
        img = img.filter(ImageFilter.MedianFilter(5))
        for i in range(5):
            img = img.filter(ImageFilter.MedianFilter(3))
        img = np.array(img) - 127.5
        img = img[np.newaxis, ...]
        return [(img, [[0]])]   # 注意，此处必须是 list，在 list 里面包含一个 tuple
    data = load_image(img)

    feed_dict = get_feeder_data(data, place, need_label=False)  # pixel

    start = time.time()
    result = exe.run(fluid.default_main_program(),
                     feed=feed_dict,
                     fetch_list=[ids],
                     return_numpy=False)
    # 将预测结果处理为 list 形式
    indexes = prune(np.array(result[0]).flatten(), 0, 1)

    # deal with result
    batch_time = time.time() - start
    return indexes, batch_time


dict_map = {31: '0', 32: '1', 33: '2', 34: '3', 35: '4',
            36: '5', 37: '6', 38: '7',
            39: '8', 40: '9'}


def deal_with_result(indexes, batch_time, dict_map_path=None):
    # load dictionary
    # dict_map = {}
    # if dict_map_path is not None and os.path.isfile(dict_map_path):
    #     with open(dict_map_path) as dict_file:
    #         for i, word in enumerate(dict_file):
    #             dict_map[i] = word.strip()
    #     print("Loaded dict from %s" % dict_map_path)

    temp_list = []
    if len(dict_map) != 0:    # 如果 dict 不空，那么就做映射
        temp_list = []
        keys = dict_map.keys()
        for i in indexes:
            if i in keys:
                word = dict_map[i]
                temp_list.append(word)
            else:
                temp_list.append('*')
    else:
        temp_list = indexes
    print("latency: %.5f s, result: %s" % (
        batch_time,
        temp_list))
    result = {"index": indexes, "mapped": temp_list, "batch_time": batch_time}
    return result


def prune(words, sos, eos):
    """Remove unused tokens in prediction result."""
    start_index = 0
    end_index = len(words)
    if sos in words:
        start_index = np.where(words == sos)[0][0] + 1
    if eos in words:
        end_index = np.where(words == eos)[0][0]
    return words[start_index:end_index]


def real_infer(img):
    # 预测并且整理结果
    indexes, batch_time = inference(img)
    print(indexes, batch_time)
    string = ""
    for i in indexes:
        string += dict_map[i]
    return string


if __name__ == "__main__":
    real_infer()