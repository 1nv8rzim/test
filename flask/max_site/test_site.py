from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')


@app.route('/resume')
def resume():
    return render_template('resume.html', title='Resume')


if __name__ == '__main__':
    app.run()
