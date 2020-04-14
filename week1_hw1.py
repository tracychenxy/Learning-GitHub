new_dict = {'ap':'1','ba':'2','ca':'3','du':'4','ef':'5'}
def passwordEval (username, password):
    """
    passwordEval checks if the input username and password matches the dictionary documenting them
    
    parameters: 
        username: the type-in username from the user
        password: the type-in password from the user
    
    output:
        A line to tell the user if what they typed in exactly matches entries in the dictionary
    
    """
    message1 = new_dict.get(username,'not found username')
    if message1 == 'not found username':
        print('Username/password not found!')
    elif new_dict[username] == password:
        print("Username and password accepted!")
    else:
        print('Username/password not found!')