# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:28:34 2018

@author: Matthew
"""


import pymysql.cursors

#Create Database
connection = pymysql.connect(host='localhost', 
                             user = 'root',
                             db='database1',
                             port = 3306,
                             password = '')
                            
try:  
    

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@gmail.org',))
        result = cursor.fetchone()
        print(result)     
        
        
finally:
            connection.close()


