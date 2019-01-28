# -*- coding: utf-8 -*-
# logging模块

import logging
import logging.config
import os

import yaml


class LogBase(object):
    """日志记录输出类."""
    __instance = None

    def __call__(self):
        pass

    def __new__(cls, *args, **kwargs):
        """单例模式实现."""
        if cls.__instance is None:
            cls.__instance = super(
                LogBase, cls).__new__(cls)
        return cls.__instance

    def __init__(self, default_path="./log/logging.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
        """初始化logging配置."""
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r") as f:
                config = yaml.load(f)
                logging.config.dictConfig(config)
        else:
            print("ERROR: FALSE READ logging.yaml")
            logging.basicConfig(level=default_level)

    def get_logger(self, moduleName):
        """获取logger."""
        return logging.getLogger(moduleName)
