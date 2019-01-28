LOG
======

日志存放文件夹
--------

日志记录配置文件路径:
> ./log/logging.yaml

说明：
> info和error日志文件将分别于每天午夜创建新文件，并保存7天，超时将自动删除
> 如需修改日志配置，请修改日志配置文件

TODO：
> 由于logging.handlers.TimedRotatingFileHandler的问题，将在第一次运行时创建一份无时间后缀的文件，且无法自动删除，并不影响使用