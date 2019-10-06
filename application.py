from flask import Flask, render_template, redirect, url_for
from wtform_fields import * 
from models import *

#configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zbytcmxkhiggzp:02e5675a8aff5bc4419533ee202700058159332473fa690c5e33049346c7c576@ec2-174-129-227-128.compute-1.amazonaws.com:5432/del0nnt046csgm'
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
   reg_form = RegistrationForm();
   if reg_form.validate_on_submit():
      username = reg_form.username.data
      password = reg_form.password.data
      
      #Hash password
      hashed_pswd = pbkdf2_sha256.hash(password)

      #Add user to DB
      user = User(username=username, password=hashed_pswd)
      db.session.add(user)
      db.session.commit()
      return redirect(url_for('login'))

   return render_template("index.html", form=reg_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
   login_form = LoginForm();
   if login_form.validate_on_submit():
      return "logged in finally"
   
   return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)

