from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        #data = {Diccionario con todos los datos}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        result = connectToMySQL('dojos_ninjas_flask').query_db(query, formulario)
        return result