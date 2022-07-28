from flask_app.config.mysqlconnection import connectToMySQL
from .ninjas import Ninja

class Dojo:

    def __init__(self, data):
        #data = {id: 1, name:"Colombia", created_at:"0000-00-00", updated_at:"0000-00-00"}
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, formulario):
        #formulario = {name: "Dojo1"}
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        #INSERT INTO dojos (name) VALUES ("Dojo1")
        result = connectToMySQL('dojos_ninjas_flask').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojos_ninjas_flask').query_db(query)
        #results me regresa una LISTA de diccionarios
        #results = [
        #   {id: 1, name:"Colombia", created_at:"0000-00-00", updated_at:"0000-00-00"} 
        #   {id: 2, name:"México", created_at:"0000-00-00", updated_at:"0000-00-00"} 
        #   {id: 3, name:"Perú", created_at:"0000-00-00", updated_at:"0000-00-00"} 
        #]
        dojos = []
        for d in results:
            #d = {id: 1, name:"Colombia", created_at:"0000-00-00", updated_at:"0000-00-00"}
            dojos.append( cls(d) ) #Dojo(d) -> Creas una instancia de Dojo
        return dojos

    @classmethod
    def get_with_ninja(cls, data):
        #data = {id: 1}
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_ninjas_flask').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }

            instancia_ninja = Ninja(n)
            dojo.ninjas.append(instancia_ninja)
        return dojo
