from flask import Flask, render_template, redirect

application = Flask(__name__)

@application.route('/')
def start():
    return home()

@application.route('/home')
def home():
    return render_template('home.html')

@application.route('/experience')
def experience():
    return render_template('experience.html')

@application.route('/blog')
def testing():
    return render_template('blog.html')

if __name__ == "__main__":
   application.run(debug=True)