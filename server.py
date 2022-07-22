'''Blossom Website'''

from flask import Flask, render_template, redirect
from model import User, connect_to_db, db
from forms import RegisterForm, LoginForm
from model import User

app = Flask(__name__)

app.secret_key = "39p4uhgau-ewvhoruawe4-9gfhap34u9bp-upsdzv923"

@app.route('/')
def index():
    """Homepage."""

    return render_template("/home.html")

@app.route('/register', methods=['GET','POST'])
def register_user():
    '''Process Registration'''

    form = RegisterForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    return render_template('register.html',form=form)

@app.route('/login-page')
def login():
    """Process Login"""
    form = LoginForm()
 
    return render_template("login.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_process():
    """Process Login"""
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    user = User.query.filter_by(email=email).first()
    if not user: 
        return redirect("/login-page")
    if user.password != password:
        return redirect("/login-page")
    return render_template("/theclub.html")
    

if __name__ == "__main__":
    connect_to_db(app)  
    app.run()