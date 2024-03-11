from .user import *

class Client():
    info:       User;
    def __init__(self, username: str, socket):
        ## TODO: STORE USER CLASS INTO AN OBJECT
        self.username = username;
        self.socket = socket;
        
