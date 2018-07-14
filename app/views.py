from flask import request, session, escape, render_template, redirect, url_for, make_response, send_from_directory
from app import app, socketio
from app.modules.database import db

#print('views.py')

@app.route('/')
def index():
    print('index')
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return redirect(url_for('auth'))

@app.route('/auth', methods=['GET','POST'])
def auth():
    print('auth')
    msg = ''
    """if request.method == 'POST':
        session['username'] = request.form['username']
        request.form['password']
        return redirect(url_for('index'))"""
    return render_template('auth.html', message=msg)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

