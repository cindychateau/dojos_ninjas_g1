from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/new/ninja')
def new_ninja():
    todos_dojos = Dojo.get_all()
    return render_template('new.html', todos_dojos=todos_dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')