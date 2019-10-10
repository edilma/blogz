import hashlib
import string
import random

def make_salt():
    salt = ''.join([random.choice(string.ascii_letters) for i in range(5)])
    return salt


def make_pw_hash(password):
    salt = make_salt()
    hash = hashlib.sha256( str.encode( password + salt)).hexdigest()
    return '{0},{1}'.format(hash,salt)   

def check_pw_hash(password,hash):
    salt = hash.split(',')[1]
    if make_pw_hash(password) == hash:
        return True
    return False
