# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : postgres
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : test py<->postgreSQL link
---------------------------------------
"""


# History:
# 2021/8/4: Create


import psycopg2


def select_all():
    # 创建连接对象
    conn = psycopg2.connect(database="test", user="kyzang", password="sqlpass", host="localhost", port="5432")
    cur = conn.cursor()  # 创建指针对象

    # # 创建表
    # cur.execute("CREATE TABLE student(id integer,name varchar,sex varchar);")
    #
    # # 插入数据
    # cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)", (1, 'Aspirin', 'M'))
    # cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)", (2, 'Taxol', 'F'))
    # cur.execute("INSERT INTO student(id,name,sex)VALUES(%s,%s,%s)", (3, 'Dixheral', 'M'))

    # 获取结果
    cur.execute('SELECT * FROM test1')
    results = cur.fetchall()
    print(results)

    # 关闭连接
    conn.commit()
    cur.close()
    conn.close()



if __name__ == '__main__':
    select_all()
