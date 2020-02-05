#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:02:47 2020

@author: fabian
"""

import pymysql

connection = pymysql.connect(host='localhost',
                             user='anon',
                             password='@Patata23',
                             db='clustomics',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    

def get_info_from_project(name):
    pass

def create_new_project(user, name, group):
    path = "%s_%s" % (name, group)
    print(path)
    sql = "INSERT INTO projects (project_name, user, id_group, file_path) VALUES ( %s, %s, %s, %s);"
    # If mirando si ese project name esta cogido ya para su user o su grupo
    with connection.cursor() as cursor:
        cursor.execute(sql, (name, user, group, path))
        connection.commit()
    return 0
        
def create_new_user():
    pass

def get_user_info(user):
    with connection.cursor() as cursor:
        sql = 'SELECT email FROM user_info where username=%s;'
        cursor.execute(sql, (user, ))
        result = tuple(cursor)
    return result


def get_groups_of_user(user):
    sql = "SELECT group_name FROM member_group WHERE username=%s;"
    with connection.cursor() as cursor:
        cursor.execute(sql, (user, ))
        result = tuple(cursor)
    return result
    pass

def get_group_info():
    pass

def save_result():
    with connection.cursor() as cursor:
        sql = 'SELECT email FROM user_info where username=%s;'
        cursor.execute(sql, (user, ))
        result = tuple(cursor)
    return result
    pass

def get_user_result(datetime, user):
    sql = "SELECT * FROM project_result where username=%s;"
    with connection.cursor() as cursor:
        cursor.execute(sql, (user, ))
        result = tuple(cursor)
    return result
    pass

def get_projects_from_user(user):
    with connection.cursor() as cursor:
        sql = 'SELECT * FROM projects WHERE user=%s;'
        cursor.execute(sql, (user, ))
        result = cursor.fetchall()
    return tuple(result)

def delete_project():
    pass