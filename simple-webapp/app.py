from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "Welcome, I'm Neila!"

@app.route('/how are you')
def hello():
    return 'I am fine, and you?'

if __name__ == "__main__":
    app.run()
