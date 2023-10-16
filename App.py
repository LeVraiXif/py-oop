import hashlib

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.__salt = hashlib.sha256().hexdigest()[:20]
        self.__password = self.__crypt_pwd(password)

    def __crypt_pwd(self, password):
        return hashlib.sha256((password + self.__salt).encode()).hexdigest()

    def user_check_pwd(self, password):
        if self.password == password:
            print('Password is correct.')
            return True
        else:
            print('Password is incorrect.')
            print(f'you typed {password} for user {self.name}')
            print()
            return False

john = User(1, "john", "12345")

print(f'Hello, I am {john.name}.')
print(f'My password is {john.__password}.') 
print(f'My id is {john.id}.')

# del john.password
# AttributeError: 'User' object has no attribute 'password'
# print('My password is {}.'.format(john.password)) 

john.user_check_pwd("12345")