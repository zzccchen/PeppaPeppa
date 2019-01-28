# -*- coding: utf-8 -*-
# 所有Handler基类

import copy

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """所有Handler基类.

    重载了输出方法，
    正确输出 (200) 使用 write_json_f 方法，错误输出使用 write_error_f 方法
    """

    # 输出模板
    RSP = {
        "code": "200",
        "message": "OK",
        "relationships": {
            "author": "null"
        },
        "jsonapi": {
            "version": "null"
        }}

    # 输出JSON
    rsp = dict

    pagination = None

    _ARG_DEFAULT = object()

    def get_argument_t(self, name, default=_ARG_DEFAULT, type=None, strip=True):
        """重载get_argument方法，并判断参数类型是否匹配.

        输出时如果满足参数类型要求，则按类型输出，否则输出None
        """
        arg = self.get_argument(name, default, strip)
        if type == int:
            if not isinstance(arg, int):
                arg = int(arg) if arg.isdigit() else None
        return arg

    def get_argument_cardno(self, default=0):
        """获取cardno参数，并校验."""
        cardno = self.get_argument_t('cardno', default, int)
        if not cardno or cardno < 213120000 or cardno > 213259999:
            return self.write_error(4001)
        return cardno

    def write_json_f(self, data=None):
        """重载write方法，并finish.

        Args:
            data: 输出JSON的data字段，默认为空
        """
        self.write_json(data)
        self.finish()

    def write_json(self, data=None):
        """重载write方法.

        Args:
            data: 输出JSON的data字段，默认为空
        """
        self.rsp = copy.deepcopy(self.RSP)
        if self.pagination:
            self.rsp["pagination"] = self.pagination
        self._write_json(data)

    def _write_json(self, data=None):
        """输出准备."""
        if data:
            self.rsp["data"] = data
        self.rsp["relationships"]["author"] = self.INFO["author"]
        self.rsp["jsonapi"]["version"] = self.INFO["version"]
        self.write(self.rsp)

    def write_error_f(self, status_code):
        """重载write_error方法，并finish.

        Args:
            status_code: HTTP状态码
        """
        self.write_error(status_code)
        self.finish()

    def write_error(self, status_code, **kwargs):
        """重载write_error方法.

        Args:
            status_code: HTTP状态码
        """
        self.rsp = copy.deepcopy(self.RSP)
        self._transforms = []
        self._write_error(status_code)

    def _write_error(self, status_code):
        """write_error输出的准备.

        Args:
            status_code: HTTP状态码，根据此参数配置输出内容
        """
        status_code = str(status_code)
        status_code_b, status_code_s = status_code[:3], status_code[3:]

        self.rsp["code"] = status_code_b

        response = {
            "400": {
                "message": "Bad Request",
                "errors": {
                    '1': {"code": 4001,
                          "message": "Wrong Type Of Cardno"}
                }
            },
            "405": {
                "message": "Method Not Allowed"
            },
            "500": {
                "message": "Internal Server Error",
                "errors": {
                    '1': {"code": 5001,
                          "message": "Unknown Server Error"}
                }
            }
        }
        self.set_status(int(status_code_b))
        self.rsp["message"] = response.get(status_code_b, {}).get(
            "message", "Undefined Error")
        self.rsp["errors"] = response.get(status_code_b, {}).get(
            "errors", {}).get(status_code_s, {"code": status_code,
                                              "message": "Undefined Error"})

        self._write_json()
