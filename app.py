from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # This is your homepage

@app.route('/get-started')
def get_started():
    return render_template('get_started.html')  # Page with "Let's Begin" button

@app.route('/lets-begin')
def lets_begin():
    return render_template('lets_begin.html')  # Page with "Get Started" button

@app.route('/third')
def third():
    return render_template('third.html')

@app.route('/fourth')
def fourth():
    return render_template('fourth.html')  # Create this page too!

@app.route('/five')
def five():
    return render_template('five.html')  # Create this page too!



if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

