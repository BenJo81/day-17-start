class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name

user_1 = User("001", "Angela")

print(user_1.id)