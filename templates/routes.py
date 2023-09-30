from flask import render_template

from app import app

@app.route('/index')
def main():
   LHS ={
      'instructors': ['Lori', 'chad'],
      'students': ['Kai','toby','soleigha','Ben']
   }
   return render_template('index.jinja', instructors=LHS['instructors'], students=LHS)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('sign_in.j2', form=form)

