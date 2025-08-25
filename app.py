from flask import Flask, render_template, request, redirect, session, flash, url_for
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to something secure in production

# 🧠 In-memory user store
users = {}

# 🌟 Splash Page
@app.route('/')
def splash():
    return render_template('splash.html')

# 📝 Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        contact = request.form['contact']
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists. Try another.')
            return redirect('/register')

        users[username] = {
            'fullname': fullname,
            'contact': contact,
            'password': password
        }

        flash('Registration successful! Please log in.')
        return redirect('/login')

    return render_template('register.html')

# 🔐 Manual Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['name'] = users[username]['fullname']
            flash('Login successful!')
            return redirect('/dashboard')
        else:
            flash('Invalid username or password.')
            return redirect('/login')

    return render_template('login.html')

# 🏠 Dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('index.html', username=session['username'], name=session.get('name'))
    else:
        flash('Please log in first.')
        return redirect('/login')

# 🌐 Other Pages
@app.route('/pastcrime')
def past_crime():
    return render_template('pastcrime.html')

@app.route('/saferoute')
def safe_route():
    return render_template('saferoute.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/sos')
def sos():
    return render_template('sos.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/setting')
def setting():
    return render_template('setting.html')

# 🔓 Logout
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect('/login')

# 🚀 Run the app (Render compatible)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
