from app import app
from model.user_model import user_model
from flask import request

u_model = user_model()

@app.route('/user/getall')
def user_getall_controller():
    return u_model.user_getall_model()

@app.route('/user/addone', methods = ['POST'])
def user_addone_controller():
    return u_model.user_addone_model(request.form)