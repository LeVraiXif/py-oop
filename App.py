class User:
    pass

john = User()

def user_check_pwd(user, password):
    if user.password == password:
        print('Password is correct.')
        return True
    else:
        print('Password is incorrect.')
        print('you typed {}.'.format(password))
        return False

john.id = 1
john.name = "John"
john.password = "12345"

print('Hello, I am {}.'.format(john.name))
print('My password is {}.'.format(john.password)) 
print('My id is {}.'.format(john.id))

# del john.password
# AttributeError: 'User' object has no attribute 'password'
# print('My password is {}.'.format(john.password)) 

user_check_pwd(john, '123465')