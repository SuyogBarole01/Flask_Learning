from app import app
from model.user_model import user_model

u_model = user_model()

@app.route('/user/getall')
def user_getall_controller():
    return u_model.user_getall_model()