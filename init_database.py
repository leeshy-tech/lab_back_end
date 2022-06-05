import json
import data
import database
import random
import os

def init_tables():
    # 下面这条命令在win的powershell报错，cmd正常
    os.system(f"mysql -u{data.database_user} -p{data.database_password} --default-character-set=utf8 < database_sql.sql")
    print("init tables")

def insert_books():
    with open('book.json','r',encoding='utf-8') as f:
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
    
    print("insert ")
        
if __name__=="__main__":
    init_tables()
    insert_books()