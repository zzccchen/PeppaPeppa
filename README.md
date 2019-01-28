# PeppaPeppa

基于 PaddlePaddle 的 OCR 验证码识别模块

## 项目说明

本项目为参加 “东南大学百度人工智能冬令营“ 的大作业

所使用的深度学习框架为 `PaddlePaddle`，前端框架为 `VUE`，后端框架为 `Tornado`

训练模型为 `CRNN-CTC` 模型，参考自 PaddlePaddle 官网所提供的 [模型](https://github.com/PaddlePaddle/models/tree/develop/fluid/PaddleCV/ocr_recognition)

数据集为 4 位数字验证码，训练集大小为 9000 张，测试集大小为 1000 张

数据集下载链接为：[点我]()

## 代码结构

```shell
├── API # 后端 API 目录
│   ├── handler
│   ├── log
│   ├── ocr_paddle
│   │   ├── models
│   ├── route
│   └── test_images
├── frontpage # 前端目录
│   ├── dist
│   ├── node_modules
│   └── src
│       ├── config
│       ├── images
│       ├── libs
│       ├── styles
│       ├── template
│       └── views
└── plug-in # 插件目录
```

## 后端使用说明

```shell
cd API

python3 api.py
```

## 前端使用说明

```shell
cd frontpage

npm install # 首次启动需要执行该语句

npm run dev # debug 模式启动
# 或
npm run build # 部署模式启动
```

## 浏览器插件使用说明

1. 在 Chrome 浏览器地址栏中输入 `chrome://extensions`

2. 选择 `加载已解压的扩展程序` 加载 `plug-in` 文件夹

## 致谢 :heart:

感谢百度和东南大学为我们提供了本次学习机会，也感谢我的四位伙伴：

我们的组长 项目经理 贾同学 [@jhj101510](https://github.com/jhj101510)

我们的产品经理兼 UI 美工 袁同学 [@StudyingYuan](https://github.com/StudyingYuan)

的辛苦付出与努力，让我们的项目得以实现下去，给你们笔心 :kissing_heart:
