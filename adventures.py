adventures={}
import pymysql
#establecemos conneccion
conn=pymysql.connect(host='52.148.209.79',user='cym',password='password',db='CHOOSE_ADVENTURE')
#consultas
cur=conn.cursor()
query="select id_adventures,name,description from ADVENTURES where id_adventures='1'"
query2="select id_adventures,name,description from ADVENTURES where id_adventures='2'"
query3="select id_adventures,name,description from ADVENTURES where id_adventures='3'"
cur.execute(query)
cur.execute(query2)
cur.execute(query3)
rows=cur.fetchall()
rows2=cur.fetchall()
rows3=cur.fetchall()
adventures={'id_adventures':rows[0]}
print(adventures)
adventures={'id_adventures':rows[0],'name':rows[1],'description':rows[2]}
