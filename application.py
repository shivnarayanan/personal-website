from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def start():
    return home()

@application.route('/home')
def home():
    return render_template('home.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
   application.run(debug=True)