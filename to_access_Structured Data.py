import mysql.connector

##CREATING DATABASE##

#conn = mysql.connector.connect(host="localhost",user="root",password="")
#bridge = conn.cursor()
#bridge.execute("create database food")


##CREATING TABLE_NAME AND COLUMN_FEATURES##
    
conn = mysql.connector.connect(host="localhost",user="root",password="",database="food")
bridge = conn.cursor()
#bridge.execute("create table breakfast (name varchar(15) primary key , rating int)")



##INSERTING RECORDS/ROWS##

#bridge.execute("insert into breakfast (name,rating) values ('pizza',4),('burger',5)")
#conn.commit()




##TO DISPLAY THE DATA IN PYTHON ITSELF##

#bridge.execute("select * from breakfast")
#result = bridge.fetchall()
#for i in result:
#    print(i)



##COLUMN WISE FILTERATION##    

#bridge.execute("select name from breakfast")
#result = bridge.fetchall()
#for i in result:
#    print(i)



##COLUMN AND ROW WISE FILTERATION##   

#bridge.execute("select name from breakfast where rating < 6")
#result = bridge.fetchall()
#for i in result:
#    print(i)



##TO UPDATE DATA##    

#bridge.execute("update breakfast set rating=7 where name='pizza'")
#conn.commit()





