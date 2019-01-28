#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from handler import BaseHandler
from log import LogBase
from route import app

logger = LogBase().get_logger("Main")


def main():
    try:
        logger.info("Api start")

        app.listen(8896)
        IOLoop.current().start()

    except KeyboardInterrupt:
        logger.info("Api exit")


if __name__ == '__main__':
    main()
