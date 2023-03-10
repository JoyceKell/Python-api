from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
       return render_template('logout.html')
    
@auth.route('/sign-up',methods=['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) <4:
            flash('Email must be greater than 3 characters',category='error')
        elif len(firstname)<2:
             flash('Firstname must be greater than 2 characters',category='error')
        elif password1 != password2:
            flash('Passwords dont match',category='error')
        elif len(password1)<7:
            flash('Passwords must be at least 7 characters',category='error')
        else:
            flash('Account created!', category='success')

    return render_template('signup.html')
