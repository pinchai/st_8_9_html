from app import app, request, render_template, session, url_for, redirect, flash

# @app.before_request
# def before_request_func():
#     session['auth'] = 'no'


@app.route('/')
def index_home():
    # session['a'] = 1
    # session['a'] = 2
    # session_data = dict(session)
    # return str(session_data)
    #test 1234

    if session['auth'] is None:
        session['auth'] = 'no'

    if session['auth'] == 'yes':
        return render_template('index.html')
    else:
        return redirect(url_for("index_login"))


@app.route('/login')
def index_login():
    session['auth'] = 'no'
    # session['username'] = 'hello_world'
    return render_template('login.html')


@app.route('/do_login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '123':
        session['auth'] = 'yes'
        return redirect(url_for("index_home"))
    else:
        session['auth'] = 'no'
        flash('Pleas check you username')
        flash('Pleas check you password')
        return redirect(url_for("index_login"))


@app.route('/logout', methods=['GET'])
def logout():
    if session['auth'] == 'yes':
        # session['auth'] = 'no'
        session.pop('auth', None)
        return redirect(url_for("index_login"))
