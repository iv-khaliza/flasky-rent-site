from app import app, db
from flask import render_template, flash, url_for, redirect
from flask_login import current_user, login_user, logout_user
from app.models import Company
from app.forms import LoginForm
import sqlalchemy as sa

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        name = db.session.scalar(sa.select(Company).where(Company.name == form.name.data))
        if name is None or not name.check_password(form.password.data):
            flash('Invalid name or password')
            return redirect(url_for('login'))
        login_user(name, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
