
class UserList:
    def __init__(self, users_file):
        with open(users_file, 'r') as fp: users = fp.readlines()
        for i in range(len(users)):
            users[i]  = users[i].strip()
        self.users = users

    def get_users(self): return  self.users


