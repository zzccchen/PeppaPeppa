# XAPI

_Xiaowei API Module (XAPI) is a web api module based on tornado framework._

**东大小微 XAPI 模块 (XAPI) 是一个基于 `tornado` 框架的 Http Api 模块。**

[**主要特性**](#主要特性) |
[**环境及依赖**](#环境及依赖) |
[**快速上手**](#快速上手) |
[**To Do List**](#To-Do-List) |
[**更新历史**](#更新历史)

## 主要特性

- 使用 `tornado` 框架和 `tormysql` 异步数据库，可轻易进行异步拓展

- 使用 `https` 和 `jwt` 身份验证以提高模块安全性

- 实现独立消息日志，日志定期覆盖

## 环境及依赖

你需要先安装 MySQL、Redis、tesseract-ocr

其他 Python 依赖包可通过以下命令安装：

```bash
pip3 install -r requirements.txt
```

或

```bash
pip3 install tornado
pip3 install pyjwt
pip3 install pymysql
pip3 install tormysql
pip3 install Pillow
pip3 install pytesseract
pip3 install redis
```

_开发环境： Ubuntu 18.04 LTS_
_Mysql: 8.0_

## 快速上手

### 初始化

- 在控制台执行以下代码进行初始化

  ```bash
  python3 .\util.py -f init
  ```

  或

  ```bash
  python3 .\util.py --fun=INI
  ```

### 运行

- 请运行 `xapi.py`

- 或在控制台执行以下代码启动模块

  ```bash
  python3 .\xapi.py
  ```

### 身份验证

- 调用申请：

  - access_token 获取：

  ```bash
  POST http://localhost:8895/xAuth?pass=pass*&word=*word
  ```

  - 每个 access_token 有效期为 6 个月，超时需重新申请。如需修改过期时间请修改 `/auth/auth_handler.cfg` 文件

  - jwt 身份验证在 `/auth/auth.cfg` 文件中实现

### 工具

- 提供的工具可以通过 `util.py` 辅以参数 `-f` 或 `--fun` 进行调用

- 可供选择的选项为：

  | 工具名               | 工具名缩写 | 工具说明                |
  | -------------------- | ---------- | ----------------------- |
  | init                 | INI        | 项目 config 文件初始化  |
  | privilege_escalation | PE         | 用户 xAuth 手动提权工具 |

- 示例：
  
  ```bash
  python3 .\util.py -f INI
  ```

  注：工具名和缩写名是完全等效的，即上语句也可写成

  ```bash
  python3 .\util.py --fun=init
  ```

### [XAPI 文档](doc/XAPI.md)

## To Do List

## 更新历史
