from flask import Flask, render_template
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html') #'Hello World!!'

@app.route('/about')
def about():
    return render_template('about.html') #'Hello World!!'

@app.route('/blog')
def blog_world():
    return 'Welcome to the blog world!!'


@app.route('/blog/2020/dogs')
def dogs_blog():
    return 'This is a blog on dogs!!'

