from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required
from models import User
from werkzeug.security import generate_password_hash
import sqlite3
from models import db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    surname = request.form.get('surname')
    hashed_password = generate_password_hash(password)

    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()

    c.execute('INSERT INTO users (email, password, name, surname) VALUES (?, ?, ?, ?)',
              (email, hashed_password, name, surname))

    conn.commit()
    conn.close()

    return redirect(url_for('auth.login'))

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@auth.route('/login', methods=['POST'])
def login_post():
    pass
    return redirect(url_for('main.index'))


@auth.route('/logout')
@login_required
def logout():
    pass
    return redirect(url_for('main.index'))
