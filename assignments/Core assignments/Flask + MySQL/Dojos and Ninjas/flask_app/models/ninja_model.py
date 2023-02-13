from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import dojo_model

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM ninja;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(f" ====== \n {result} \n ======== \n")
        ninja_list = []
        if result:
            for row in result:
                one_ninja = cls(row)
                ninja_list.append(one_ninja)
        return ninja_list

    @classmethod
    def add_ninja(cls,data):
        q = "INSERT INTO `dojos_and_ninjas_schema`.`ninja` (first_name, last_name,age,dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(q,data)