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

@app.route('/user/update', methods = ['PUT'])
def user_update_controller():
    return u_model.user_update_model(request.form)

@app.route('/user/delete/<id>', methods = ['DELETE'])
def user_delete_controller(id):
    return u_model.user_delete_model(id)

@app.route('/user/patch/<id>', methods = ['PATCH'])
def user_patch_controller(id):
    return u_model.user_patch_model(request.form, id)

@app.route('/user/getall/limit/<limit>/page/<page>', methods = ['GET'])
def user_pagination_controller(limit, page):
    return u_model.user_pagination_model(limit, page)