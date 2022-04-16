from flask import Flask,request,jsonify
from flask_cors import CORS
from gevent import pywsgi
import database
from aToken import token_encode,token_decode

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
        books_info = []
        try:
            books_info_list = database.select_books_info()
            for books in books_info_list:
                book = {
                    "ISBN": books[0],
                    "cover_img": books[1],
                    "name": books[2],
                    "press": books[3],
                    "author": books[4],
                    "collection": books[5],
                    "can_borrow": books[6]
                }
                books_info.append(book)
            msg = "success"
        except:
            msg = "error"
        response_msg = {
            "msg":msg,
            "books_info":books_info
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
        books_info = []
        try:
            book_detail = database.select_book_detail(ISBN)
            book = {
                "ISBN": book_detail[0],
                "cover_img": book_detail[1],
                "name": book_detail[2],
                "press": book_detail[3],
                "author": book_detail[4],
                "collection": book_detail[5],
                "can_borrow": book_detail[6]
            }
            books_info.append(book)
            msg = "success"
        except:
            msg = "error"
        response_msg = {
            "msg":msg,
            "books_info":books_info
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

if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0',port),app)
    server.serve_forever()
    print("end")
