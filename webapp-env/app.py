import os
from flask import Flask

app = Flask(__name__)

txt = os.environ.get('APP_TXT')

@app.route('/')
def main():
    return txt

@app.route('/how are you')
def hello():
    return 'I am fine, and you?'

if __name__ == "__main__":
    app.run()
