class User:
    def __init__(self, id, name):
        self.id =id
        self.name =name
        self.followers = 0
        self.following = 0

    def follow_user(self,user):
        self.following += 1
        user.followers += 1

# list_of_names = names = ["Orion", "Lyra", "Zephyr", "Nova", "Atlas", "Echo", "Kairos", "Selene", "Dorian", "Cypher"]
# list_of_users = []
# for create_new_users in range(0, len(list_of_names)-1):
#     list_of_users.append(User(create_new_users,list_of_names[create_new_users]))
#     print(list_of_users[create_new_users].name,list_of_users[create_new_users].id )
# print(list_of_users[0].name, list_of_users[0].id )

user1 = User("001","Przemek")
user2 = User("002","Kiki")
user1.follow_user(user2)
print(user1.followers, user1.following)
print(user2.followers, user2.following)
