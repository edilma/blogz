

def validateUserinfo(infoUser):
    username= infoUser[0]
    password= infoUser[1]
    verifyPassword = infoUser[2]
    # email = infoUser[3]
    errors=["","","",""]
    #Typographical errors in the fields
    if (len(username)<=3) or (len(username)>=20) or (' ' in username):
        errors[0]= 'Incorrect Username: Please use 3 or more letters and not spaces'

    if (len(password)<=3) or (len(password)>=20) or (' ' in password):
        errors[1]= 'Incorrect Password: Please use 3 or more letters and not spaces'
        
    # if (email.count('@')>1) or (email.count('.')>1):
    #     errors[3]='Incorrect Password. Please write your password again.'
    
    # if (len(email)>0 and ( (len(email)<=3) or (len(email)>=20)  or (' ' in email))):
    #     errors[3]='Incorrect email. Please write your email again.'

    #Password and verification don't match
    if password != verifyPassword:
        errors[2] = 'We could not verify the password. Passwords do NOT match'

    #error when fields are left  empty
    if username=='':
        errors[0]='Username can NOT be empty.  Please provide a username '
    if password=='':
        errors[1]='Password can NOT be empty.  Please provide a password '    
    if verifyPassword=='':
        errors[2]='Please write your password again.  We could not verify it'
    return errors


# def validateLogin(user_login, user):
#     username= infoUser[0]
#     password= infoUser[1]
#     errors=["","",]
#     existing_user = user
#     if not existing_user:
#         errors[0]='Username DO NOT exits.  Please enter a correct username '
#     else:
#         if not check_pw_hash(password,user.pw_hash):
#             error[1] = 'Incorrect Password'
#         else: 
#             existing_user = [username,password]
#             return existing_user
#     return errors
    




    #Typographical errors in the fields
    if (len(username)<=3) or (len(username)>=20) or (' ' in username):
        errors[0]= 'Incorrect Username: Please use 3 or more letters and not spaces'

    if (len(password)<=3) or (len(password)>=20) or (' ' in password):
        errors[1]= 'Incorrect Password: Please use 3 or more letters and not spaces'
        
    # if (email.count('@')>1) or (email.count('.')>1):
    #     errors[3]='Incorrect Password. Please write your password again.'
    
    # if (len(email)>0 and ( (len(email)<=3) or (len(email)>=20)  or (' ' in email))):
    #     errors[3]='Incorrect email. Please write your email again.'

    #Password and verification don't match
    if password != verifyPassword:
        errors[2] = 'We could not verify the password. Passwords do NOT match'

    #error when fields are left  empty
    if username=='':
        errors[0]='Username can NOT be empty.  Please provide a username '
    if password=='':
        errors[1]='Password can NOT be empty.  Please provide a password '    
    if verifyPassword=='':
        errors[2]='Please write your password again.  We could not verify it'
    return errors