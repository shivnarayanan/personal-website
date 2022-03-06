from flask import Flask

application = Flask(__name__)

@application.route('/')
def helloworld():
    return "Hello World! This is my first web application! I have removed some changes!"

if __name__ == "__main__":
    application.run(debug=True)