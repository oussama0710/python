from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja_model

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninja=[]
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM dojo;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(f" ====== \n {result} \n ======== \n")
        dojo_list = []
        if result:

            for row in result:
                one_dojo = cls(row)
                dojo_list.append(one_dojo)

            return dojo_list

    @classmethod
    def add_dojo(cls,data):

        q = """
            INSERT INTO `dojos_and_ninjas_schema`.`dojo` (`name`) VALUES (%(name)s);
            """
        result = connectToMySQL(DATABASE).query_db(q, data)
        return result

    @classmethod
    def join_dojo(cls,data):

        q = """
            SELECT * FROM dojos_and_ninjas_schema.dojo
            LEFT JOIN ninja ON dojo.id = ninja.dojo_id
            WHERE dojo.id = %(id)s;
            """
        results = connectToMySQL(DATABASE).query_db(q, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            rows = {
                'id': row['ninja.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninja.created_at'],
                'updated_at': row['ninja.updated_at']
            }
            dojo.ninja.append(ninja_model.Ninja(rows))
        return dojo