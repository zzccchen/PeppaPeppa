# -*- coding: utf-8 -*-

import tornado.web


class RouterConfig(tornado.web.Application):
    """重置Tornado自带的路由对象."""

    def route(self, url):
        """注册路由关系对应表的装饰器."""
        def register(handler):
            # URL和Handler对应关系添加到路由表中
            self.add_handlers(".*$", [(url, handler)])
            return handler
        return register


# 创建路由对象
app = RouterConfig()
