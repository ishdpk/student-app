from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask import request
from __init__ import create_app, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home')
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)

app = create_app() 
if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True)