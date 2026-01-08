import mysql.connector
import json
from flask import make_response

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
            res = make_response({'payload': result},200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
        else:
            return make_response({'message':"No data found"}, 204)
    
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['password']}')")
        return make_response({'message':"User Created Successfully"},201)
    
    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET name = '{data['name']}', email = '{data['email']}', phone = '{data['phone']}', password = '{data['password']}' where id = '{data['id']}' ")
        if self.cur.rowcount > 0:
            return make_response({'message':"User Updated Successfully"},201)
        else:
            return make_response({'message':"Nothing to update"},202)
    
    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users where id = {id}")
        if self.cur.rowcount > 0:
            return make_response({'message':"User delete Successfully"},200)
        else:
            return make_response({'message':"Nothing to delete"},204)
    
    def user_patch_model(self, data, id):
        qry = 'UPDATE users SET '
        for key in data:
            qry += f"{key} = '{data[key]}',"
        qry = qry[:-1]
        qry += f" WHERE id = {id}"
        
        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({'message':"User Updated Successfully"},201)
        else:
            return make_response({'message':"Nothing to update"},202)
    
    def user_pagination_model(self, limit, page):
        limit = int(limit)
        page = int(page)
        start = (page * limit) - limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()


        # result will contain list of dictionaries. These dictionaries will have are rows of table in database.
        if len(result)>0:
            res = make_response({'payload': result},200)
            return res
        else:
            return make_response({'message':"No data found"}, 204)