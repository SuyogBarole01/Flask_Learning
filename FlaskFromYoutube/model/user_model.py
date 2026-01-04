import mysql.connector
import json

class user_model():
    def __init__(self):
        #Connection Establishment Code
        try:
            self.con = mysql.connector.connect(host='localhost',username = 'root', password ="Yashi@07", database = 'Flask_learning')
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary = True)
            print('MySQL connection successful')
        except:
            print('Mysql connection error')

    def user_getall_model(self):
        #Query Execution Code
        self.cur.execute('SELECT * FROM users')
        result = self.cur.fetchall()


        # result will contain list of dictionaries. These dictionaries will have are rows of table in database.
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
    
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['password']}')")
        return "User Created Successfully"