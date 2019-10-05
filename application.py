from flask import Flask, render_template
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
      
      user = User(username=username, password=password)
      db.session.add(user)
      db.session.commit()
      return "inserted into db"

   return render_template("index.html", form=reg_form)

if __name__ == "__main__":
    app.run(debug=True)

