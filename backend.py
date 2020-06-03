from flask import Flask, render_template, request
from sign_in import SignIn

app = Flask(__name__)

@app.route('/homepage')
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/project_directory')
def project_directory():
    return render_template('project_directory.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sign_in', methods=['POST'])
def sign_in():
    if(request.form.get('username') and request.form.get('password')):
        username = request.form['username']
        password = request.form['password']
        return render_template('sign_in.html', not_signed_in=False)
    return render_template('sign_in.html', not_signed_in=True)

if __name__ == "__main__":
    app.run()
