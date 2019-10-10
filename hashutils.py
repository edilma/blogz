import hashlib
import random
import string

def make_salt():
    return ''.join([ random.choice(string.ascii_letters) for i in range(5)])

def make_pw_hash(password):
    salt = make_salt()
    hash = hashlib.sha256(str.encode(password + salt)).hexdigest()
    # returns a tuple of 2 elements: pwh=(hash ,salt)
    return '{0},{1}'.format(hash, salt)


def check_password(password,hash):
    #requires a password and the hash
    salt = hash.split(',')[1]
    if make_pw_hash(password, salt) == hash:
        return True
    return False