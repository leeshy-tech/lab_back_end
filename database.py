import pymysql
import datetime
import data

conn = pymysql.connect(
    user=data.database_user,
    password=data.database_password,
    database=data.database_table
)
cursor = conn.cursor()

def select_user(id,key)->str:
    sql_select_id = f"select {key} from users_info where id={id}"
    cursor.execute(sql_select_id)
    res = cursor.fetchone()
    return res

def select_record(id):
    sql_select_record_byId = f"select ISBN,record_time,operation from record where user_id={id}"
    cursor.execute(sql_select_record_byId)
    res = cursor.fetchall()
    record_list = []

    if res:
        for record_sql in res:
            record_dict = {}
            book_detail = select_book_detail(record_sql[0])
            record_dict['cover_img'] = book_detail[2]
            record_dict['name'] = book_detail[3]
            record_dict['ISBN'] = record_sql[0]
            record_dict['record_time'] = record_sql[1].strftime('%Y-%m-%d %H:%M:%S')
            record_dict['operation'] = record_sql[2]
            record_list.append(record_dict)       
    return record_list

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

def select_book_state(ISBN,number):
    sql_select_book_state = f'select state from books_list where ISBN="{ISBN}" and number = {number}'
    cursor.execute(sql_select_book_state)
    res = cursor.fetchone()
    return res[0]

def insert_record(ISBN,number,id,operation):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql_insert_record = f'insert into record values ("{ISBN}",{number},{id},"{time}","{operation}")'
    cursor.execute(sql_insert_record)
    # 如果是还书，就把之前的借书记录删掉。
    if operation == "还":
        sql_delete_record = f'delete from record where (ISBN = "{ISBN}" and number = {number} and user_id = {id} and operation = "借")'
        cursor.execute(sql_delete_record)
    conn.commit()
    return None
