class Books:
    def __init__(self,ISBN:int, call:str, available:int, total:int, title:str):
        self.ISBN = ISBN;
        self.callNumber = call;
        self.available = available;
        self.total = total;
        self.title = title;
        
    def getISBN(self):
        return self.ISBN;
   
    def setISBN(self,iSBN:int):
        self.ISBN = iSBN;
   
    def getCallNumber(self):
        return self.callNumber;
   
    def setCallNumber(self,callNumber:str):
        self.callNumber = callNumber;
   
    def getAvailable(self):
        return self.available;
   
    def setAvailable(self,available:int):
        self.available = available;
   
    def getTotal(self):
        return self.total;
   
    def setTotal(self,total:int):
        self.total = total;
   
    def getTitle(self):
        return self.title;
   
    def setTitle(self,title:str):
        self.title = title;
    def formatForFile():
        pass
