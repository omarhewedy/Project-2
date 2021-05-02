from flask import Flask, render_template, url_for, flash, session, request, redirect
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/whatwedo')
def whatwedo():
    return render_template('whatwedo.html')

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
