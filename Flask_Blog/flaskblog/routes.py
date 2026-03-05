from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.model import User, Post

posts=[
    {
        'author' : 'krishna',
        'title' : 'Python',
        'content' : 'This is Python content',
        'date_posted' : 'Feb 05, 2026'

    },
    {
        
        'author' : 'Sathish',
        'title' : 'Python-2',
        'content' : 'This is Python content',
        'date_posted' : 'Feb 05, 2026'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Login success-ful', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login failed! ', 'danger')
    return render_template('login.html', title='Login', form=form)
