import mysql.connector

cnx = mysql.connector.connect(user='ivan', password='password',
                              host='127.0.0.1',
                              database='team_members')
cnx.close()