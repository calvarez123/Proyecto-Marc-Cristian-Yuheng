import pymysql
def getUser():
    conn=pymysql.connect(host='52.148.209.79', user= 'cym', passwd='password', db='CHOOSE_ADVENTURE')
    cur=conn.cursor()
    query='select * from USER'
    cur.execute(query)
    rows=cur.fetchall()
    dic={}
    v=1
   
    dic[rows[0][1]]={}
    dic[rows[0][1]]['password']=rows[0][2]
    dic[rows[0][1]]['userId']=rows[0][0]
    return dic