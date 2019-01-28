#coding:utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import distutils.util
import numpy as np
from paddle.fluid import core
import paddle.fluid as fluid
import six


def print_arguments(args):
    """Print argparse's arguments.
    Usage:

    .. code-block:: python

        parser = argparse.ArgumentParser()
        parser.add_argument("name", default="Jonh", type=str, help="User name.")
        args = parser.parse_args()
        print_arguments(args)

    :param args: Input argparse.Namespace for printing.
    :type args: argparse.Namespace
    """
    print("-----------  Configuration Arguments -----------")
    for arg, value in sorted(six.iteritems(vars(args))):
        print("%s: %s" % (arg, value))
    print("------------------------------------------------")


def add_arguments(argname, type, default, help, argparser, **kwargs):
    """Add argparse's argument.

    Usage:

    .. code-block:: python

        parser = argparse.ArgumentParser()
        add_argument("name", str, "Jonh", "User name.", parser)
        args = parser.parse_args()
    """
    type = distutils.util.strtobool if type == bool else type
    argparser.add_argument(
        "--" + argname,
        default=default,
        type=type,
        help=help + ' Default: %(default)s.',
        **kwargs)


def to_lodtensor(data, place):
    seq_lens = [len(seq) for seq in data]
    cur_len = 0
    lod = [cur_len]
    for l in seq_lens:
        cur_len += l
        lod.append(cur_len)
    flattened_data = np.concatenate(data, axis=0).astype("int32")
    flattened_data = flattened_data.reshape([len(flattened_data), 1])
    res = core.LoDTensor()
    res.set(flattened_data, place)
    res.set_lod([lod])
    return res


def get_ctc_feeder_data(data, place, need_label=True):
    pixel_tensor = core.LoDTensor()
    pixel_data = None
    pixel_data = np.concatenate(
        list(map(lambda x: x[0][np.newaxis, :], data)), axis=0).astype("float32")
    pixel_tensor.set(pixel_data, place)
    label_tensor = to_lodtensor(list(map(lambda x: x[1], data)), place)
    if need_label:
        return {"pixel": pixel_tensor, "label": label_tensor}
    else:
        return {"pixel": pixel_tensor}