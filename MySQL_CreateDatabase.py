# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 23:49:42 2018

@author: Matthew
"""

import pymysql.cursors

#Create Database
connection = pymysql.connect(host='localhost', 
                             user = 'root',
                             port = 3306,
                             password = '')

try:  
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE database1')
        
        
finally:
            connection.close()