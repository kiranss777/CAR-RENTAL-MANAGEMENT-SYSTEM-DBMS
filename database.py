import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="car_showroom"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS SHOWROOM (NAME varchar(30),SID  varchar(13) PRIMARY KEY, STATE varchar(20),CITY varchar(20),EMAIL varchar(50),PHNO varchar(10))')
    c.execute('CREATE TABLE IF NOT EXISTS CARS (ID varchar(30) PRIMARY KEY, MAKE  varchar(30), MODEL varchar(30),YEAR varchar(4),PRICE varchar(20),SIDD varchar(13),FOREIGN KEY(SIDD) REFERENCES SHOWROOM(SID))')
    c.execute('CREATE TABLE IF NOT EXISTS SPECS (MAKEOFCAR varchar(10),MODELOFCAR varchar(30),YEAROFCAR varchar(4),TYPE varchar(10),DISP varchar(20),POWER varchar(20),FUELTYPE varchar(20),FUELCONS varchar(20))')
    c.execute('CREATE TABLE IF NOT EXISTS CUSTOMER (CUSTID varchar(10),CUSTNAME varchar(30),EMAIL varchar(40),PHNO varchar(10),CARBOUGHT varchar(20),CARBOUGHTID varchar(20),FOREIGN KEY(CARBOUGHTID) REFERENCES CARS(ID))')

def add_data_to_customer(cid,cname,email,phno,car,carid):
    c.execute('INSERT INTO CUSTOMER (CUSTID ,CUSTNAME, EMAIL, PHNO, CARBOUGHT,CARBOUGHTID) VALUES (%s,%s,%s,%s,%s,%s);',
              (cid,cname,email,phno,car,carid))
    mydb.commit()
def add_data_to_showroom(name,sid, state, city,email,phno):
    c.execute('INSERT INTO SHOWROOM (NAME ,SID, STATE, CITY, EMAIL,PHNO) VALUES (%s,%s,%s,%s,%s,%s);',
              (name,sid, state, city,email,phno))
    mydb.commit()

def add_data_to_cars(id,make,model,year,price,sid):
    c.execute('INSERT INTO CARS (ID , MAKE  , MODEL ,YEAR,PRICE ,SIDD ) VALUES (%s,%s,%s,%s,%s,%s);',
              (id,make,model,year,price,sid))
    mydb.commit()
def add_data_to_car_details(make,model,year,type,disp,power,fueltype,fuelcons):
    c.execute('INSERT INTO SPECS ( MAKEOFCAR, MODELOFCAR,YEAROFCAR,TYPE,DISP,POWER,FUELTYPE,FUELCONS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
              (make,model,year,type,disp,power,fueltype,fuelcons))
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM SHOWROOM')
    c.execute('SELECT * FROM CARS')
    c.execute('SELECT * FROM SPECS')
    c.execute('SELECT * FROM CUSTOMER')
    data = c.fetchall()
    return data

def view_showroom():
    c.execute('SELECT * FROM SHOWROOM')
    data = c.fetchall()
    return data
def view_showroom_name():
    c.execute('SELECT NAME FROM SHOWROOM')
    data = c.fetchall()
    return data

def view_cars():
    c.execute('SELECT * FROM CARS')
    data = c.fetchall()
    return data
def view_cars_id():
    c.execute('SELECT ID FROM CARS')
    data = c.fetchall()
    return data

def view_cust():
    c.execute('SELECT * FROM CUSTOMER')
    data = c.fetchall()
    return data

def view_cust_id():
    c.execute('SELECT CUSTID FROM CUSTOMER')
    data = c.fetchall()
    return data

def view_cars_specs():
    c.execute('SELECT * FROM SPECS')
    data = c.fetchall()
    return data
def view_cars_specs_model():
    c.execute('SELECT MODELOFCAR FROM SPECS')
    data = c.fetchall()
    return data

def view_cust_name():
    c.execute('SELECT CUSTNAME FROM CUSTOMER')
    data = c.fetchall()
    return data

def get_details_showroom(name):
    c.execute('SELECT * FROM SHOWROOM WHERE Name="{}"'.format(name))
    data = c.fetchall()
    return data
def get_cars(id):
    #c.execute('SELECT * FROM SHOWROOM WHERE Name="{}"'.format(name))
    c.execute('SELECT * FROM CARS WHERE ID="{}"'.format(id))
    data = c.fetchall()
    return data

def get_cust(id):
    #c.execute('SELECT * FROM SHOWROOM WHERE Name="{}"'.format(name))
    c.execute('SELECT * FROM CUSTOMER WHERE CUSTID="{}"'.format(id))
    data = c.fetchall()
    return data

def get_car_specs(model):
    #c.execute('SELECT * FROM SHOWROOM WHERE Name="{}"'.format(name))
    c.execute('SELECT * FROM SPECS WHERE MODEL="{}"'.format(model))
    data = c.fetchall()
    return data

def edit_showroom(newname,newsid, newstate, newcity,newemail,newphno,name,sid, state, city,email,phno):
    c.execute("UPDATE SHOWROOM SET NAME=%s, SID=%s, STATE=%s,CITY=%s,EMAIL=%s,PHNO=%s WHERE NAME=%s AND SID=%s AND STATE=%s AND CITY=%s AND EMAIL=%s AND PHNO=%s", (newname,newsid, newstate, newcity,newemail,newphno,name,sid, state, city,email,phno))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_cars(newid,newmake,newmodel,newyear,newprice,newsid,id,make,model,year,price,sid):
    c.execute("UPDATE CARS SET ID=%s,MAKE=%s, MODEL=%s, YEAR=%s,PRICE=%s,SIDD=%s WHERE ID=%s AND MAKE=%s AND MODEL=%s AND YEAR=%s AND PRICE=%s AND SIDD=%s", (newid,newmake,newmodel,newyear,newprice,newsid,id,make,model,year,price,sid))
    mydb.commit()
    data = c.fetchall()
    return data
def edit_customer(newcustid,newcustname,newcustemail,newcustphno,newcarbought,newcarboughtid,CUSTID,CUSTNAME,CUSTEMAIL,CUSTPHNO,CARBOUGHT,CARBOUGHTID):
    c.execute("UPDATE CUSTOMER SET CUSTID=%s,CUSTNAME=%s, CUSTEMAIL=%s, CUSTPHNO=%s,CARBOUGHT=%s,CARBOUGHTID=%s WHERE CUSTID=%s AND CUSTNAME=%s AND CUSTEMAIL=%s AND CUSTPHNO=%s AND CARBOUGHT=%s AND CARBOUGHTID=%s", (newcustid,newcustname,newcustemail,newcustphno,newcarbought,newcarboughtid,CUSTID,CUSTNAME,CUSTEMAIL,CUSTPHNO,CARBOUGHT,CARBOUGHTID))
    mydb.commit()
    data = c.fetchall()
    return data
    
   
def delete_showroom(name):
    c.execute('DELETE FROM SHOWROOM WHERE NAME="{}"'.format(name))
    mydb.commit()
def delete_car(model):
    c.execute('DELETE FROM CARS WHERE ID="{}"'.format(model))
    mydb.commit()
def delete_specs(model):
    c.execute('DELETE FROM SPECS WHERE MODELOFCAR="{}"'.format(model))
    mydb.commit()
def delete_cust(name):
    c.execute('DELETE FROM CUSTOMER WHERE CUSTNAME="{}"'.format(name))
    mydb.commit()
def disp_query(query):
    c.execute('{}'.format(query))
    data = c.fetchall()
    return data

