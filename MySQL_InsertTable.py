# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:24:27 2018

@author: Matthew
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             db='database1',
                             charset='utf8mb4',                           
                             user = 'root',
                             port = 3306,
                             password = '')
                            
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@gmail.org', 'secret'))

    connection.commit()

finally:
    connection.close()