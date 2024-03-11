import os

class User():
    idx:                    int;
    name:                   str;
    ip:                     str;
    pw:                     str;
    plan:                   int;
    max_cons:               int;
    max_time:               int;
    cons:                   int;
    expiry:                 int;
    rank:                   int;

    def __init__(self, arr: list[str]):
        
        if len(arr) != 9:
            return
        
        self.name           = arr[0];
        self.ip             = arr[1];
        self.pw             = arr[2];
        self.plan           = int(arr[3]);
        self.max_cons       = int(arr[4]);
        self.max_time       = int(arr[5]);
        self.cons           = int(arr[6]);
        self.expiry         = arr[7];
        self.rank           = arr[8];
    
    def validateAttackCon(self):
        pass

    def isPremium(self):
        pass

    def isAdmin(self):
        pass