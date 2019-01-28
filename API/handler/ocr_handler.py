# -*- coding: utf-8 -*-
# 此接口为OCR数字接口

import platform

import requests
from PIL import Image

from handler import BaseHandler
from log import LogBase
from ocr_paddle import real_infer
from route import app

logger = LogBase().get_logger("OcrD")

if ('2.' in platform.python_version()):
    from StringIO import StringIO as Bytes2Data
else:
    from io import BytesIO as Bytes2Data


@app.route(r'/api/ocr')
class OcrDHandler(BaseHandler):
    """OCR数字 handler."""
    INFO = {"author": "zzccchen", "version": "1.0"}

    def post(self, *args, **kwargs):
        file_metas = self.request.files["file"]
        # print(file_metas)
        for meta in file_metas:
            im = Image.open(Bytes2Data(meta['body']))

            def crop():
                list = []
                img_size = im.size
                if img_size[0] == 320:
                    # 第一块
                    x = 0
                    y = 0
                    w = img_size[0]/2.0
                    h = img_size[1]
                    region = im.crop((x, y, x + w, y + h))
                    # region.save("./c1.png")
                    # print("图片宽度和高度分别是{}".format(region.size))
                    list.append(region)
                    # 第二块
                    x = w
                    y = 0
                    region = im.crop((x, y, x + w, y + h))
                    # region.save("./c2.png")
                    # print("图片宽度和高度分别是{}".format(region.size))
                    list.append(region)
                    # print(list)
                else:
                    # print(im)
                    list.append(im)
                return list
            list = crop()
            string = ""
            for im in list:
                string += real_infer(im)
        return self.write_json_f({"ocr_data": string})

    def get(self, *args, **kwargs):
        file_url = self.get_argument("address", str)
        r = requests.get(file_url)
        im = Image.open(Bytes2Data(r.content))
        # im.save("1.png", "png")
        string = real_infer(im)
        return self.write_json_f({"ocr_data": string})
