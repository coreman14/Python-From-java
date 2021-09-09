class Node:
    def __init__(self,o, n = None):
        self.element = o
        self.successor = n
    def getElement(self) -> object:
        return self.element
    
    def setElement(self,o):
        self.element = o
    
    def getSuccessor(self) -> "Node":
        return self.successor
    
    def setSuccessor(self,node):
        self.successor = node