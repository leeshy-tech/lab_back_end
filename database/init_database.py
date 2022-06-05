import json
import sys
import random
import os
from data import data
from database import database

def init_tables():
    # 下面这条命令在win的powershell报错，cmd正常
    os.system(f"mysql -u{data.database_user} -p{data.database_password} --default-character-set=utf8 < database/database_sql.sql")
    print("init tables")

def insert_books():
    with open('data/book.json','r',encoding='utf-8') as f:
        book_list = list(json.load(f))
        for book in book_list:
            # 插入 book_detail 表
            book = dict(book)
            database.insert_book_detail(book)
            # 插入 book_list 表
            book1 = {
                "ISBN":book["ISBN"],
                "lib":"西土城图书馆",
                "shelf":str(random.randint(0,10))
            }
            book2 = {
                "ISBN":book["ISBN"],
                "lib":"沙河图书馆",
                "shelf":str(random.randint(0,10))
            }
            database.insert_book_list(book1)
            database.insert_book_list(book2)
    
    print("insert book data")