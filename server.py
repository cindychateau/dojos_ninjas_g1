from flask_app import app
from flask_app.controllers import dojos_controller, ninjas_controller

if __name__=="__main__":
    app.run(debug=True)
