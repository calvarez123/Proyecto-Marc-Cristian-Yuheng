import pymysql


conn=pymysql.connect(host='52.148.209.79', user= 'cym', passwd='password', db='CHOOSE_ADVENTURE')
cur=conn.cursor()
name=input('Introduce el nombre del personaje: ')
description=input('Introduce una peuqeña desceripcion del personaje: ')
query="INSERT INTO CHARACTERS(name, description) VALUES(%s, %s)"
val =(name,description)
cur.execute(query,val)
conn.commit()
query='select * from CHARACTERS'
cur.execute(query)
rows=cur.fetchall()
print(rows)
