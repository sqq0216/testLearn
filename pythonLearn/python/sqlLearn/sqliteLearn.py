import sqlite3

def insert():
    conn =sqlite3.connect("D:\\TestProjects\\testLearn\\pythonLearn\\python\\sqlLearn\\test.db")
    cursor = conn.cursor()
    sql = "create table user (id varchar(20) primary key, name varchar(20))"
    cursor.execute(sql)
    sql_insert = "insert into user (id, name) values (\'1\', \'qianqian\')"
    cursor.execute(sql_insert)
    #print('rowcount = ', cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()

def select():
    # 查询记录：
    conn = sqlite3.connect('D:\\TestProjects\\testLearn\\pythonLearn\\python\\sqlLearn\\test.db')
    cursor = conn.cursor()
    # 执行查询语句:
    cursor.execute('select * from user where id=?', '1')
    # 获得查询结果集:
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    select()
