import pymysql
import datetime

conn = pymysql.connect(
    user='root',
    password='lisai430094',
    database='user'
)
cursor = conn.cursor()

def select_user(id,key)->str:
    sql_select_id = f"select {key} from users_info \
        where id={id}"
    cursor.execute(sql_select_id)
    res = cursor.fetchone()
    return res

def select_record(id):
    sql_select_record_byId = f"select ISBN,number,record_time,operation \
        from record where user_id={id}"
    cursor.execute(sql_select_record_byId)
    res = cursor.fetchall()
    record_array = []

    if res:
        for record_sql in res:
            record_dict = {}
            record_dict['ISBN'] = record_sql[0]
            record_dict['number'] = record_sql[1]
            record_dict['record_time'] = record_sql[2].strftime('%Y-%m-%d %H:%M:%S')
            record_dict['operation'] = record_sql[3]
            record_array.append(record_dict)       
    return record_array

def select_books_info():
    sql_select_books_info = "select *from books_info;"
    cursor.execute(sql_select_books_info)
    res = cursor.fetchall()
    return res

def select_book_detail(ISBN):
    sql_select_book_detail = f'select *from books_info where ISBN="{ISBN}";'
    cursor.execute(sql_select_book_detail)
    res = cursor.fetchone()
    return res

def select_book_store(ISBN):
    sql_select_book_store = f'select lib,shelf,state from books_list where ISBN="{ISBN}"'
    cursor.execute(sql_select_book_store)
    res = cursor.fetchall()
    return res
