class User():
    def __init__(self,ids,name,email,password):
        self.id = ids;
        self.name = name;
        self.email = email;
        self.password = password;
    
    
    def getID(self):
        return self.id
    
    def getEmail(self):
        return self.email
    
    def getName(self):
        return self.name
    
    def isCorrectPassword(self,password):
        return self.password == password

    def __eq__(self, o: object):
        if not isinstance(o,User):
            return False
        return self.getID() == o.getID() \
           and self.getEmail() == o.getEmail() \
           and self.getName() == o.getName() 