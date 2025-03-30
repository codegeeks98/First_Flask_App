from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is my webpage!</h1>'

@app.route('/info')
def info():
    return '<h1>This is the info page</h1>'

if __name__ == '__main__':
    app.run() 