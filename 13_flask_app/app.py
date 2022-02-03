from flask import Flask, redirect, url_for, render_template

# Create an object of this class
app = Flask(__name__)  # to create an app instance


# connect the function below to the browser using a decorator
@app.route("/")
# create a function to link our homepage
def index():
    return 'Homepage!'

# `flask run` in terminal


# create welcome message page
@app.route("/welcome/")  # It is convention add to forward slash at the end
def welcome():
    return render_template('welcome.html')


# create login page; display the 2 messages in form of h1 and h2
@app.route("/login/")  # It is convention add to forward slash at the end
def login():
    # return '<h1>Login page!</h1><h2>Sign up or register.</h2>'

    # if the page is unavailable, we need to redirect them
    return redirect(url_for('welcome/'))


if __name__ == '__main__':
    app.run(debug=True)

