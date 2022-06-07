import pymysql
import datetime
from data import data

def get_cursor():
    conn = pymysql.connect(
        user=data.database_user,
        password=data.database_password,
        database=data.database_table
    )
    cursor = conn.cursor()
    return cursor

def select_user(id,key)->str:
    cursor = get_cursor()
    sql_select_id = f"select {key} from users_info where id={id}"
    cursor.execute(sql_select_id)
    res = cursor.fetchone()
    return res

def select_record(id):
    cursor = get_cursor()
    sql_select_record_byId = f"select ISBN,number,record_time,estimated_return_time,operation from record where user_id={id}"
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
            record_dict['number'] = record_sql[1]
            record_dict['record_time'] = record_sql[2].strftime('%Y-%m-%d %H:%M:%S')
            if record_sql[3] == None:
                record_dict['estimated_return_time'] = record_sql[3]
            else:
                record_dict['estimated_return_time'] = record_sql[3].strftime('%Y-%m-%d %H:%M:%S')
            record_dict['operation'] = record_sql[4]
            record_list.append(record_dict)       
    return record_list

def select_books_info():
    cursor = get_cursor()
    sql_select_books_info = "select *from books_info;"
    cursor.execute(sql_select_books_info)
    res = cursor.fetchall()
    return res

def select_book_detail(ISBN):
    cursor = get_cursor()
    sql_select_book_detail = f'select *from books_info where ISBN="{ISBN}";'
    cursor.execute(sql_select_book_detail)
    res = cursor.fetchone()
    return res

def insert_book_detail(book):
    cursor = get_cursor()
    book_str = f'("{book["ISBN"]}","{book["category"]}","{book["cover_img"]}","{book["name"]}","{book["press"]}","{book["author"]}")'
    sql_insert_book_detail = "insert into books_info (ISBN,category,cover_img,name,press,author)values" + book_str
    cursor.execute(sql_insert_book_detail)
    conn.commit()
    return None

def insert_book_list(book):
    cursor = get_cursor()
    book_str = f'("{book["ISBN"]}","{book["lib"]}","{book["shelf"]}","可借")'
    sql_insert_book_list = "insert into books_list (ISBN,lib,shelf,state)values" + book_str
    cursor.execute(sql_insert_book_list)
    conn.commit()
    return None

def select_book_store(ISBN):
    cursor = get_cursor()
    sql_select_book_store = f'select lib,shelf,state from books_list where ISBN="{ISBN}"'
    cursor.execute(sql_select_book_store)
    res = cursor.fetchall()
    return res

def select_book_state(ISBN,number):
    cursor = get_cursor()
    sql_select_book_state = f'select state from books_list where ISBN="{ISBN}" and number = {number}'
    cursor.execute(sql_select_book_state)
    res = cursor.fetchone()
    return res[0]

def insert_lend_record(ISBN,number,id):
    cursor = get_cursor()
    now = datetime.datetime.now()
    return_time = now + datetime.timedelta(days=30)

    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    return_time_str = return_time.strftime('%Y-%m-%d %H:%M:%S')
    sql_insert_record = f'insert into record values ("{ISBN}",{number},{id},"{now_str}","{return_time_str}","借")'
    cursor.execute(sql_insert_record)
    conn.commit()
    return None

def insert_return_record(ISBN,number,id):
    cursor = get_cursor()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql_insert_record = f'insert into record (ISBN,number,user_id,record_time,operation) values ("{ISBN}",{number},{id},"{now}","还")'
    cursor.execute(sql_insert_record)
    # 把之前的借书记录删掉。
    sql_delete_record = f'delete from record where (ISBN = "{ISBN}" and number = {number} and user_id = {id} and operation = "借")'
    cursor.execute(sql_delete_record)
    conn.commit()
    return None
# 续借一本书，将其预计归还时间+30 day
def renew_book(ISBN,number,id):
    cursor = get_cursor()
    sql_select_lend_record = f'select estimated_return_time from record \
        where (ISBN = "{ISBN}" and number = {number} and user_id = {id} and operation = "借")'
    cursor.execute(sql_select_lend_record)
    res = cursor.fetchone()
    estimated_return_time = (res[0] + datetime.timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
    sql_update_lend_record = f'update record set estimated_return_time="{estimated_return_time}"\
        where (ISBN = "{ISBN}" and number = {number} and user_id = {id} and operation = "借")'
    cursor.execute(sql_update_lend_record)
    conn.commit()
    return None
