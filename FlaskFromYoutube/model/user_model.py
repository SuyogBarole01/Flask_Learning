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
            return {'payload': result}
        else:
            return {'message':"No data found"}
    
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['password']}')")
        return {'message':"User Created Successfully"}
    
    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET name = '{data['name']}', email = '{data['email']}', phone = '{data['phone']}', password = '{data['password']}' where id = '{data['id']}' ")
        if self.cur.rowcount > 0:
            return {'message':"User Updated Successfully"}
        else:
            return {'message':"Nothing to update"}
    
    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users where id = {id}")
        if self.cur.rowcount > 0:
            return {'message':"User delete Successfully"}
        else:
            return {'message':"Nothing to delete"}
    