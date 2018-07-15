from flask import request, session, render_template, redirect, url_for, make_response, send_from_directory
from app import app, socketio
import app.modules.database as db
from app.modules import strings
import config
import time

#print('views.py')

@app.route('/')
def index():
    if 'username' in session:
        #return 'Logged in as %s' % escape(session['username'])
        print('Auth successfull for user:', session['username'])
        return render_template('layout.html')
    return redirect(url_for('auth'))

@app.route('/auth', methods=['GET','POST'])
def auth():
    msg = ''
    if request.method == 'POST':
        u = db.get_user(request.form['username'], request.form['password'])
        if u != None:
            session['username'] = u.username
        else:
            time.sleep(1) #to prevent bruteforce attack
        print(strings.encode(config.SECRET_KEY, request.form['password']))
        return redirect(url_for('index'))
    return render_template('auth.html', message=msg)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    return render_template('logout.html')

