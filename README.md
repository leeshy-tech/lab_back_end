# lab_back_end
图书馆项目的后端接口
## 项目结构
```
├─ interface.py：接口文件
├─ data
│  ├─ data.py：数据，包括数据库名、密码、书籍分类标准
│  └─ book.json：书籍数据，用于books_detail表
├─ database
│  ├─ init_database.py：初始化数据库，包含初始化表和插入book.json数据
│  ├─ database.py：集成一些数据库操作
│  └─ database_sql.sql：sql脚本，初始化数据库中的表和触发器
└─ utils
   ├─ keyword_search.py：关键词搜索
   └─ aToken.py：Token的加密和解密
```
## 运行项目
### 准备
- 确保你的主机IP能被访问：`ping <IP>`
- 确保端口号为interface.port的端口上没有进程占用，占用的话修改即可
- 下载mysql：[https://leeshy-tech.github.io/mysql_install/](https://leeshy-tech.github.io/mysql_install/)
- 在data.py中修改数据库名称、密码

### 运行
- 运行并初始化数据库： `python interface.py -i`
- 或：`python interface.py`  

如果是windows，需要在cmd而不是powershell运行，否则会报错。
### 访问
使用url：`http://<IP>:<port><route>`访问接口  
请求体使用json格式