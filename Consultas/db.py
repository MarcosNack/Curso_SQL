import mysql.connector

con = mysql.connector.connect(host='localhost', database='banco', user='root', password='MHnc@46501741')

if con.is_connected():
    db = con.get_server_info()
    print("Conectado ao servidor MYSQL Versão ", db)
    cursor = con.cursor()
    cursor.execute('Show tables;')
    mytables = cursor.fetchall()
    for i in mytables:
        print(i)
