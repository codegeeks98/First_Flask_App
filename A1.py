from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is my webpage!</h1>'

@app.route('/info')
def info():
    return '<h1>This is the First info page</h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)    

if __name__ == '__main__':
    app.run() 