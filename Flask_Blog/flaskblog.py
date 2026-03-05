from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm

app=Flask(__name__)

app.config['SECRET_KEY'] = 'e16f1d19e64364b44b4d5d0c6f803b61'

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

if __name__ == '__main__':
    app.run(debug=True)