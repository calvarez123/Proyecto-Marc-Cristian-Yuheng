from importlib import import_module
from re import T
import pymysql
import getUser
conn=pymysql.connect(host='52.148.209.79', user= 'cym', passwd='password', db='CHOOSE_ADVENTURE')
cur=conn.cursor()
figura=('''
**********************************************************************************************************************************************************
                                                ######  ######  ######  #######  ########  ######  
                                                ######  ######  ######  #######  ########  ######
                                                ##      ##      ##      ##   ##  ##        ##
                                                ##      ##      ##      ##   ##  ##        ##
                                                ######  ######  ##      ##   ##  ##        ######
                                                ######  ######  ##      ##   ##  ## #####  ######
                                                ##          ##  ##      ##   ##  ## #####  ##
                                                ##          ##  ##      ##   ##  ##    ##  ##
                                                ######  ######  ######  #######  ########  ######
                                                ######  ######  ######  #######  ########  ###### 
                            
                                                                ##########  ##   ##
                                                                ##########  ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      ##   ##
                                                                    ##      #######
                                                                    ##      #######
                            
                                    ########  ##      ##  ######  ###     ##  ########  ##   ##  ####     ########
                                    ########  ##      ##  ######  ###     ##  ########  ##   ##  #####    ########
                                    ##    ##  ##      ##  ##      ## ##   ##     ##     ##   ##  ##  ##   ##    ##
                                    ##    ##  ##      ##  ##      ## ##   ##     ##     ##   ##  ##   ##  ##    ##
                                    ########   ##    ##   ######  ##  ##  ##     ##     ##   ##  ##   ##  ########
                                    ########   ##    ##   ######  ##  ##  ##     ##     ##   ##  ######   ########
                                    ##    ##   ##    ##   ##      ##   ## ##     ##     ##   ##  #####    ##    ##
                                    ##    ##    ##  ##    ##      ##   ## ##     ##     ##   ##  ## ##    ##    ##
                                    ##    ##    ######    ######  ##    ####     ##     #######  ##  ##   ##    ##
                                    ##    ##     ####     ######  ##    ####     ##     #######  ##   ##  ##    ##
**********************************************************************************************************************************************************
''')
vali=True
while vali==True:
    print(figura)
    menu = '1) Login\n2) Create user\n3) Replay Adventure\n4) Reports\n5) Exit '
    print(menu)
    opc= input('Insert Option: ')
    if opc=='1':
        user=input('Input usersername: ')
        d=getUser.getUser()
        if user in d.keys():
            print('You have entered successfully')
            break
            
        else:
            print('The user is not found')     
    else:
        vali=False           
if opc=='2':
    validation = False
    while validation == False:
        user=input('Input User: ')
        pasos=0
        for i in user:
                pasos = pasos + 1
        if pasos > 5 and pasos < 11:
            validation = True
        else:
            print("USERNAME have to be longer than 5 and shorter than 11")
    validation1 = False
    validation2 = False
    salir12= False
    while True:

        while validation1 == False:
            password = input('Input Password: ')
            pasos = 0
            for i in password:
                pasos = pasos + 1
            if pasos > 7:
                validation2 = False
                validation1 = True
            else:
                print("PASSWORD have to be longer than 7")

            while validation2 == False:
                contador = 0
                for i in password:
                    if i.isdigit() == False and i.isalpha() == False:
                        contador = contador + 1
                if contador != 0:
                    validation2 = True
                    validation3 = False
                else:
                    print("PASSWORD need to contain special character")
                    validation1 = False
                    validation3 = True
                    validation4 = True
                    validation5 = True
                    break

            while validation3 == False:
                contador = 0
                for i in password:
                    if i.isspace() == True:
                        contador = contador + 1
                if contador == 0:
                    validation3 = True
                    validation4 = False
                else:
                    print("PASSWORD cannot have spaces")
                    validation1 = False
                    validation2 = False
                    validation4 = True
                    validation5 = True
                    break

            while validation4 == False:
                contador = 0
                for i in password:
                    if i.isdigit() == True:
                        contador = contador + 1
                if contador != 0:
                    validation4 = True
                    validation5 = False
                else:
                    print("PASSWORD has to contain numbers ")
                    validation1 = False
                    validation2 = False
                    validation3 = False
                    validation5 = True
                    break

            while validation5 == False:
                contadormayus = 0
                contadorminus = 0
                for i in password:
                    if i.isalpha() == True:
                        if i.isupper() == True:
                            contadormayus = contadormayus + 1
                        elif i.islower() == True:
                            contadorminus = contadorminus + 1
                if contadorminus != 0 and contadormayus != 0:
                    validation5 = True
                    salir12 = True
                else:
                    print("PASSWORD has to contain mayus and minus ")
                    validation1 = False
                    validation2 = False
                    validation3 = False
                    validation4 = False
                    break
            if salir12 == True:
                conn=pymysql.connect(host='52.148.209.79', user= 'cym', passwd='password', db='CHOOSE_ADVENTURE')
                cur=conn.cursor()
                print("USER CREATED")
                query="INSERT INTO USER(username,password) VALUES(%s,%s)"
                val =(user,password)
                cur.execute(query,val)
                conn.commit()
                validation1=True
    