from flask import Flask,request, abort, render_template, url_for,redirect 
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from nav_links import how_it_works, budget_uni_bp, stocks_bp, resources_bp
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def getUser():
    configure()
    return str(os.getenv('user'))

def getPasswd():
    configure()
    return str(os.getenv('passwd'))

app = Flask(__name__)
app.register_blueprint(how_it_works)
app.register_blueprint(budget_uni_bp)
app.register_blueprint(stocks_bp)
app.register_blueprint(resources_bp)
#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{getUser()}:{getPasswd()}@localhost/our_users'

# #Secret Key
app.config['SECRET_KEY'] = 'secret key'
#Initialize Database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False, unique=True)
    password = db.Column(db.String(80),nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(
        min=4,max=20)],render_kw={"placeholder":"Username"})
    
    password = PasswordField(validators=[InputRequired(),Length(
        min=4,max=20)],render_kw={"placeholder":"Password"})
    
    submit = SubmitField("Register")

    def validate_username(self,username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        
        if existing_user_username:
            raise ValidationError("That username already exists. Please choose a different one.")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(
        min=4,max=20)],render_kw={"placeholder":"Username"})
    
    password = PasswordField(validators=[InputRequired(),Length(
        min=4,max=20)],render_kw={"placeholder":"Password"})
    
    submit = SubmitField("Login")

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html',form=form)

@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user
    return redirect(url_for('login'))

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html',form=form)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
