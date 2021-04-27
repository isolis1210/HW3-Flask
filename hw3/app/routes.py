from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages
# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route("/", methods=["GET", "POST"])
def home():
    form=MessageForm()
    if form.validate_on_submit():   
        # check if user exits in database
        ##db.create_all()
        ##users = user.query.all()
        user= User.query.filter_by(username=form.username.data).first()
        # if not create user and add to database
        if user is None or not user.check_password(form.password.data):
            flash ('Invalid username or password')
            return redirect('/login')
        # create row in Message table with user (created/found) add to ta database
        login_user(user, remember=form.remember_me.data) 
    return render_template('home.html', form=form)
    posts = [
    # output all messages
    
    # create a list of dictionaries with the following structure
    # [{'author':'carlos','message':'Yo! Where you at?'},
        {
            'author':'carlos',
            'message':'Yo! Where you at?!'
        },
        {
            'author':'Jerry',
            'message':'Home. You?'
        }
    ]
    return render_template('home.html', posts=posts, form=form)

