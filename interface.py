from flask import Flask,request,jsonify
from flask_cors import CORS
from gevent import pywsgi
import sys
from utils.aToken import token_encode,token_decode
from utils.keyword_search import search_by_keyword
from database.init_database import init_tables,insert_books
from database import database
from data import data
port = 9900
app = Flask(__name__)
CORS(app,resource=r'/*')

@app.route('/user/login',methods=['POST'])
def user_login():
    """
    用户登陆
    in:id,pwd
    out:token,msg
    """
    if request.method == "POST":
        id = request.json.get("user_id")
        pwd = request.json.get("user_pwd")
        token = None
        msg = ""

        try:
            pwd_sql = database.select_user(id,"pwd")[0]
            if pwd == pwd_sql:
                msg = "log in success"
                token = token_encode(id)
            else:
                msg = "password error"
        except:
            msg = "id not exist"

        print(id + msg)
        response_msg = {
            "msg":msg,
            "token":token
        }
        return response_msg

@app.route('/user/info',methods=['GET'])
def get_info():
    """
    获取用户信息：账号、类型、头像和借阅记录
    in:token
    out:response_msg
    """
    if request.method == "GET":
        token = request.headers["token"]
        msg = ""
        user_type = None
        img_url = None
        lend_record = None
        id = None
        try:
            id = token_decode(token)
            user_name,img_url = database.select_user(id,"name,headphoto")
            lend_record = database.select_record(id)
            msg = "get info success"
        except:
            msg = "token error"

        print(id + msg)
        response_msg = {
            "msg":msg,
            "id":id,
            "user_name":user_name,
            "img_url":img_url,
            "lend_record":lend_record
        } 
        
        return response_msg

@app.route('/book/recommended',methods=['GET','POST'])
def get_books():
    """
    图书推荐
    返回5个书籍信息
    in:index(int or None)
    GET POST
    """
    msg = None
    book_info_list = []
    if request.method == "GET":
        index = 0
    else:
        index = int(request.json.get("index"))
    try:
        books_info_list = database.select_books_info()
        for books in books_info_list[index:index+5]:
            book = {
                "ISBN": books[0],
                "category":books[1],
                "cover_img": books[2],
                "name": books[3],
                "press": books[4],
                "author": books[5],
                "collection": books[6],
                "can_borrow": books[7]
            }
            book_info_list.append(book)
        msg = "recommend success"
    except:
        msg = "error"
    response_msg = {
        "msg":msg,
        "book_info_list":book_info_list
    }
    return response_msg

@app.route('/book/detail',methods=['POST'])
def get_book_detail():
    """
    获取书籍详细信息
    POST
    in:ISBN
    """
    if request.method == "POST":
        ISBN = request.json.get("ISBN")
        msg = None
        book_info_list = []

        book_detail = database.select_book_detail(ISBN)
        book = {
            "ISBN": book_detail[0],
            "category":book_detail[1],
            "cover_img": book_detail[2],
            "name": book_detail[3],
            "press": book_detail[4],
            "author": book_detail[5],
            "collection": book_detail[6],
            "can_borrow": book_detail[7]
        }
        book_info_list.append(book)
        msg = "get detail success"
        response_msg = {
            "msg":msg,
            "book_info_list":book_info_list
        }
        return response_msg

@app.route('/book/store',methods=['POST'])
def get_book_store():
    """
    获取馆藏信息
    POST
    in:ISBN
    """
    if request.method == "POST":
        ISBN = request.json.get("ISBN")
        msg = None
        books_store = []
        try:
            book_store_list = database.select_book_store(ISBN)
            for book_store in book_store_list:
                book_store_set = {
                    "lib":book_store[0],
                    "shelf":book_store[1],
                    "state":book_store[2]
                }
                books_store.append(book_store_set)
            msg = "get store success"
        except:
            msg = "error"
        response_msg = {
            "msg":msg,
            "books_store":books_store
        }
        return response_msg

@app.route('/book/category',methods=['GET'])
def get_book_category():
    """
    获取书籍分类
    GET
    """
    if request.method == "GET":
        msg = None
        book_category = []  

        try:
            for category1 in data.category.keys():
                category12 = {
                    "category1":"",
                    "category2":[]
                }
                category12["category1"] = category1
                category2_list = data.category[category1]
                for (id,category2) in category2_list:
                    category12["category2"].append(category2)
                book_category.append(category12)
            msg = "get category success"

        except:
            msg = "error"
            
        response_msg = {
            "msg":msg,
            "book_category":book_category
        }
        return response_msg

@app.route('/book/search',methods=['POST'])
def search_book():
    """
    关键字搜索
    POST
    in:keyword
    """
    if request.method == "POST":
        keyword = request.json.get("keyword")
        print("keyword=" + keyword)
        msg = None
        search_result = []
        
        book_info_list = database.select_books_info()
        # 数据库查询的结果是一个元组，不是dict
        book_dict_list = []
        for book_info in book_info_list:
            book = {
                "ISBN":book_info[0],
                "name":book_info[3]
            }
            book_dict_list.append(book)
        # 搜索
        ISBN_list = search_by_keyword(keyword,book_dict_list)
        # 构造返回数据
        for ISBN in ISBN_list:
            book_detail = database.select_book_detail(ISBN)
            book = {
                "ISBN": book_detail[0],
                "category":book_detail[1],
                "cover_img": book_detail[2],
                "name": book_detail[3],
                "press": book_detail[4],
                "author": book_detail[5],
                "collection": book_detail[6],
                "can_borrow": book_detail[7]
            }
            search_result.append(book)
        msg = "search success"
        response_msg = {
            "msg":msg,
            "book_info_list":search_result
        }
        return response_msg

@app.route('/book/search_category',methods=['POST'])
def search_book_category():
    """
    分类搜索
    POST
    in:category
    """
    if request.method == "POST":
        category = request.json.get("category")
        print("category=" + category)
        for category_item in data.category.keys():
            for (id,category2) in data.category[category_item]:
                if category2 == category:
                    print("id=" + id)
                    category = id

        msg = None
        book_info_list = []
        books_info_list = database.select_books_info()
        for books in books_info_list:
            if books[1] == category:
                book = {
                    "ISBN": books[0],
                    "category":books[1],
                    "cover_img": books[2],
                    "name": books[3],
                    "press": books[4],
                    "author": books[5],
                    "collection": books[6],
                    "can_borrow": books[7]
                }
                book_info_list.append(book)
        msg = "search category success"
        response_msg = {
            "msg":msg,
            "book_info_list":book_info_list
        }
        return response_msg

@app.route('/book/lend',methods=['POST'])
def lend_book():
    """
    借还书
    POST
    in:ISBN,number,operation,token
    """
    if request.method == "POST":
        msg = None
        token = request.headers["token"]
        ISBN = request.json.get("ISBN")
        number = request.json.get("number")
        operation = request.json.get("operation")

        try:
            id = token_decode(token)
        except:
            msg == "token error"
            return msg
        print(f"id:{id} {operation} book:{ISBN} number:{number}")
        book_state = database.select_book_state(ISBN, number)
        if operation == "借":
            if book_state == "借出":
                msg = "书籍已借出"
            elif book_state =="可借":
                database.insert_lend_record(ISBN, number, id)
                msg = "借书成功"
        elif operation == "还":
            if book_state == "借出":
                database.insert_return_record(ISBN, number, id)
                msg = "还书成功"
            elif book_state =="可借":
                msg = "书籍未借出，不可还"
        elif operation=="续":
            if book_state == "借出":
                database.renew_book(ISBN, number, id)
                msg = "续借成功"
            elif book_state =="可借":
                msg = "书籍未借出，不可续借"
                
        return msg


if __name__ == "__main__":

    # 使用参数-i来初始化数据库
    if "-i" in sys.argv:
        init_tables()
        insert_books()

    print(f"start sever in port {port}")    
    server = pywsgi.WSGIServer(('0.0.0.0',port),app)
    server.serve_forever()
    print("end")
