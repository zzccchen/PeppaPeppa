# PeppaPeppa

An OCR captcha recognition module built with PaddlePaddle.

## Project Overview

This project was developed as part of a major assignment for the Southeast University Baidu AI Winter Camp.

The project utilizes PaddlePaddle as the deep learning framework, VUE for the frontend, and Tornado for the backend.

The model used for training is the CRNN-CTC architecture, inspired by the model available on the PaddlePaddle official GitHub repository [here](https://github.com/PaddlePaddle/models/tree/develop/fluid/PaddleCV/ocr_recognition).

The dataset consists of 4-digit numeric captcha images, with 9,000 images in the training set and 1,000 images in the test set.

The dataset can be downloaded using the following link: [Download](https://github.com/zzccchen/PeppaPeppa/blob/master/ocr_data.7z).

## Project Structure

```shell
├── API # Backend API directory
│   ├── handler
│   ├── log
│   ├── ocr_paddle
│   │   ├── models
│   ├── route
│   └── test_images
├── frontpage # Frontend directory
│   ├── dist
│   ├── node_modules
│   └── src
│       ├── config
│       ├── images
│       ├── libs
│       ├── styles
│       ├── template
│       └── views
└── plug-in # Plugin directory
```

## Backend Setup Instructions

```shell
cd API

python3 api.py
```

## Frontend Setup Instructions

```shell
cd frontpage

npm install # Run this command once to install dependencies

npm run dev # Start in debug mode
# or
npm run build # Start in production mode
```

## Browser Plugin Setup Instructions

1. In the Chrome browser address bar, type `chrome://extensions`.

2. Click "Load unpacked" and select the `plug-in` folder.

## Acknowledgements :heart:

We would like to thank Baidu and Southeast University for providing us with this learning opportunity, as well as our four teammates:

Our team leader and project manager, Mr. Jia [@jhj101510](https://github.com/jhj101510),

Our product manager and UI designer, Mr. Yuan [@StudyingYuan](https://github.com/StudyingYuan),

for their hard work and dedication, which made this project possible. We appreciate you both :kissing_heart:
