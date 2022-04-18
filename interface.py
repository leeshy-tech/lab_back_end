from flask import Flask,request,jsonify
from flask_cors import CORS
from gevent import pywsgi
import database
from aToken import token_encode,token_decode
import data

port = 8899
app = Flask(__name__)
CORS(app,resource=r'/*')
"""
用户登陆
"""
@app.route('/user/login',methods=['POST'])
def user_login():
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

        response_msg = {
            "msg":msg,
            "token":token
        }
        return jsonify(response_msg)

"""
获取用户信息：账号、类型、头像和借阅记录
in:token
out:response_msg
"""
@app.route('/user/info',methods=['POST'])
def get_info():
    if request.method == "POST":
        token = request.headers["token"]
        msg = ""
        user_type = None
        img_url = None
        lend_record = None
        try:
            id = token_decode(token)
            user_type,img_url = database.select_user(id,"type,headphoto")
            #lend_record = database.select_record(id)
            msg = "success"
        except:
            msg = "token error"

        response_msg = {
            "msg":msg,
            "id":id,
            "user_type":user_type,
            "img_url":img_url
            #"lend_record":lend_record
        } 
        
        return jsonify(response_msg)
"""
图书推荐
GET
"""
@app.route('/book/recommended',methods=['GET'])
def get_books():
    if request.method == "GET":
        msg = None
        book_info_list = []
        try:
            books_info_list = database.select_books_info()
            for books in books_info_list:
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
            msg = "success"
        except:
            msg = "error"
        response_msg = {
            "msg":msg,
            "book_info_list":book_info_list
        }
        return response_msg

"""
获取书籍详细信息
POST
in:ISBN
"""
@app.route('/book/detail',methods=['POST'])
def get_book_detail():
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
        msg = "success"
        response_msg = {
            "msg":msg,
            "book_info_list":book_info_list
        }
        return response_msg

"""
获取馆藏信息
POST
in:ISBN
"""
@app.route('/book/store',methods=['POST'])
def get_book_store():
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
            msg = "success"
        except:
            msg = "error"
        response_msg = {
            "msg":msg,
            "books_store":books_store
        }
        return response_msg

"""
获取书籍分类
GET
"""
@app.route('/book/category',methods=['GET'])
def get_book_category():
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
            msg = "success"

        except:
            msg = "error"
            
        response_msg = {
            "msg":msg,
            "book_category":book_category
        }
        return response_msg
"""
关键字搜索
POST
in:keyword
"""
@app.route('/book/search',methods=['POST'])
def search_book():
    if request.method == "POST":
        keyword = request.json.get("keyword")
        print("keyword=" + keyword)
        msg = None
        book_info_list = []
        books_info_list = database.select_books_info()
        for books in books_info_list:
            if books[3] == keyword:
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
        msg = "success"
        response_msg = {
            "msg":msg,
            "book_info_list":book_info_list
        }
        return response_msg
"""
分类搜索
POST
in:category
"""
@app.route('/book/search_category',methods=['POST'])
def search_book_category():
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
        msg = "success"
        response_msg = {
            "msg":msg,
            "book_info_list":book_info_list
        }
        return response_msg


if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0',port),app)
    server.serve_forever()
    print("end")
