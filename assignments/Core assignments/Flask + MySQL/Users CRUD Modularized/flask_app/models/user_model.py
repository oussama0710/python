from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('users_schema').query_db(query)
        print(f" ====== \n {result} \n ======== \n")
        user_list = []
        if result:

            for row in result:
                one_movie = cls(row)
                user_list.append(one_movie)

            return user_list


    @classmethod
    def save(cls, data):

        q = """
        INSERT INTO users_schema.users (first_name, last_name, email, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());
        """
        result = connectToMySQL('users_schema').query_db(q, data)
        print(f" ******** {result} ********")
        return result

    @classmethod
    def delete(cls, data):

        q = """
        DELETE FROM `users_schema`.`users` WHERE (id = %(id)s);
        """
        result = connectToMySQL('users_schema').query_db(q, data)
        print(f" ******** {result} ********")
        return result
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])
        
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
