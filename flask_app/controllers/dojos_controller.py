from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojos import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    todos_dojos = Dojo.get_all()
    return render_template('index.html', todos_dojos=todos_dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    #request.form = {name:"Dojo1"}
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>') #/dojo/1
def show_dojo(id): #id = 1
    data = {
        "id":id
    }
    dojo = Dojo.get_with_ninja(data)
    return render_template('dojo.html', dojo=dojo)