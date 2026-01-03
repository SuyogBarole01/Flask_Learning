from app import app
from model.user_model import user_model

u_model = user_model()

@app.route('/user/signup')
def signup():
    return u_model.user_signup_model() + '\n signup controller operation'