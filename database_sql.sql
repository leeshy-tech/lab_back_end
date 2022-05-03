/* 避免乱码：mysql -u root -p --default-character-set=utf8 */
drop database user;
create database user;
use user;

/* 用户账号信息表 */
create table users_info(
    id int not null primary key,
    pwd varchar(20) not null,
    name varchar(50) not null,
    headphoto varchar(50)
);	

insert into users_info values
(2019210774,'lisai','user','http://124.223.167.22:8080/pictures/1.jpg'),
(2019000774,'admin','admin','http://124.223.167.22:8080/pictures/2.jpg');

/* 图书类别表 */
create table books_info(
    ISBN varchar(30) primary key,
    category varchar(10),
    cover_img varchar(100),
    name varchar(20),
    press varchar(20),
    author varchar(20),
    collection int default 0,
    can_borrow int default 0
);	

insert into books_info (ISBN,category,cover_img,name,press,author)values
("978-7-03-025415-3","TN","http://124.223.167.22:8080/pictures/book/dsp.png","数字信号处理","科学出版社","门爱东,苏菲"),
("978-7-04-039663-8","01","http://124.223.167.22:8080/pictures/book/高等数学第七版.jpg","高等数学第七版","同济大学出版社","同济大学数学系"),
("978-7-56-354427-1","TN","http://124.223.167.22:8080/pictures/book/通信原理.jpg","通信原理","北邮出版社","周炯槃");

/* 图书表 */
create table books_list(
    ISBN varchar(30) not null ,
    number int,
    lib varchar(20) not null check(lib='西土城图书馆' or lib='沙河图书馆'),
    shelf varchar(50) not null,
    state varchar(10) check(state='借出' or state='可借' or state='遗失'),
    primary key(ISBN,number),
    foreign key(ISBN) references books_info(ISBN)
);
/* 触发器
1 插入新的书籍时，自动累加其编号
2 插入新的书籍时，更新类别表的可借和馆藏数
3 更新书籍表时，更新类别表的可借和馆藏数
 */
delimiter $$
create trigger trigger_insert_blist before insert on books_list for each row
begin
    declare number_count int;
    select count(*) into number_count from books_list where ISBN=new.ISBN;
    set new.number=number_count;
end $$ 

create trigger trigger_insert_blist2 after insert on books_list for each row
begin
    declare book_collection int;
    declare book_can_borrow int;
    select count(*) into book_collection from books_list where ISBN=new.ISBN;
    select count(*) into book_can_borrow from books_list where ISBN=new.ISBN and state="可借";
    update books_info set can_borrow = book_can_borrow where ISBN=new.ISBN;
    update books_info set collection = book_collection where ISBN=new.ISBN; 
end $$ 

create trigger trigger_update_blist after update on books_list for each row
begin
    declare book_collection int;
    declare book_can_borrow int;
    select count(*) into book_collection from books_list where ISBN=new.ISBN;
    select count(*) into book_can_borrow from books_list where ISBN=new.ISBN and state="可借";
    update books_info set can_borrow = book_can_borrow where ISBN=new.ISBN;
    update books_info set collection = book_collection where ISBN=new.ISBN; 
end $$ 
delimiter ;

insert into books_list (ISBN,lib,shelf,state)values
("978-7-03-025415-3",'西土城图书馆','1','可借'),
("978-7-03-025415-3",'西土城图书馆','1','可借');

/* 借还书记录表 */
create table record(
    ISBN varchar(30) not null,
    number int not null,
    user_id int not null,
    record_time datetime not null,
    estimated_return_time datetime,
    operation varchar(10) not null check(operation='借' or operation='还'),
    foreign key (ISBN,number) references books_list (ISBN,number),
    foreign key (user_id) references users_info (id)   
);	

/* 触发器：插入借还书记录时，更新该书籍的借阅状态 */
delimiter $$
create trigger trigger_insert_record after insert on record for each row
begin
if new.operation='借' then
update books_list set state='借出' where ISBN=new.ISBN and number=new.number;
else
update books_list set state='可借' where ISBN=new.ISBN and number=new.number;
end if;
end $$ 
delimiter ;
