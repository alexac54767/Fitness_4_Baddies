from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

class User:    

    def __init__(self, name, uid, password, workouts):
        self._name = name    # variables with self prefix become part of the object, 
        self._uid = uid
        self.set_password(password)
        self._workouts = workouts
    
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
    # a getter method, extracts email from object
    @property
    def uid(self):
        return self._uid
    
    # a setter function, allows name to be updated after initial object creation
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, uid):
        return self._uid == uid
    
    
    @property
    def workouts(self):
        return self._workouts
    
    # a setter function, allows name to be updated after initial object creation
    @workouts.setter
    def workouts(self, workouts):
        self._workouts = workouts

    
    
    # dictionary is customized, removing password for security purposes
    @property
    def dictionary(self):
        dict = {
            "name" : self.name,
            "uid" : self.uid,
            "workouts" : self.workouts
        }
        return dict
    
    # update password, this is conventional setter
    def set_password(self, password):
        """Create a hashed password."""
        self._password = generate_password_hash(password, method='sha256')

    # check password parameter versus stored/encrypted password
    def is_password(self, password):
        """Check against hashed password."""
        result = check_password_hash(self._password, password)
        return result
    
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.dictionary)
    
    # output command to recreate the object, uses attribute directly
    def __repr__(self):
        return f'User(name={self._name}, uid={self._uid}, password={self._password}, workouts={self._workouts})'
        
def tester(users, uid, psw):
    result = None
    for user in users:
        # test for match in database
        if user.uid == uid and user.is_password(psw): # check for match
            print("* ", end="")
            result = user
        # print using __str__ method
        print(str(user))
    return result    

if __name__ == "__main__":
    u1 = User(name='Thomas Edison', uid='toby', password='123toby', workouts='burpees, swimming')
    u2 = User(name='Ava Carlson', uid='coolcat', password='welovecoolcats4', workouts='sprinting, cheer')
    u3 = User(name='Tom Holland', uid='thebestspiderman', password='peter1', workouts='climbing, boxing')

    # put user objects in list for convenience
    users = [u1, u2, u3]

    # Find user
    print("Test 1, find user 3")
    u = tester(users, u3.uid, "peter1")

    # Change user
    print("Test 2, change user 3")
    u.name = "Andrew Garfield"
    u.uid = "spidermanalso"
    u.workouts = "punching"
    u.set_password("peter3")
    u = tester(users, u.uid, "peter3")




    print("JSON ready string:\n", u1, "\n") 
    print("Raw Variables of object:\n", vars(u1), "\n") 
    print("Raw Attributes and Methods of object:\n", dir(u1), "\n")
    print("Representation to Re-Create the object:\n", repr(u1), "\n") 

    print("JSON ready string:\n", u2, "\n") 
    print("Raw Variables of object:\n", vars(u2), "\n") 
    print("Raw Attributes and Methods of object:\n", dir(u2), "\n")
    print("Representation to Re-Create the object:\n", repr(u2), "\n") 