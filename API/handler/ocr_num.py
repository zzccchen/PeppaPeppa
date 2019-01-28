# -*- coding: utf-8 -*-
# 此接口为OCR数字接口

import traceback

from handler import BaseHandler
from log import LogBase
from route import app
logger = LogBase().get_logger("OcrNumD")


@app.route(r'/ocrNum')
class OcrNumDHandler(BaseHandler):
    """一卡通号转QQ handler."""
    INFO = {"author": "zzccchen", "version": "2.0"}

    def get(self, *args, **kwargs):
        cardno = self.get_argument_cardno()
        if not cardno:
            return self.finish()
        try:
            return self.write_json_f(500)
        except Exception as e:
            logger.error(traceback.format_exc())
            return self.write_error_f(5001)
