from LinkedListADT import LinkedListADT
from Node import Node

class SLL(LinkedListADT):
    def __init__(self):
        super().__init__()
        self.head = self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def clear(self):
        self.head = self.tail = None
    
    def append(self, data):
        temp = Node(data)
        if self.isEmpty():
            self.head = temp
            
        elif self.tail is None:
            self.tail = temp
            self.head.setSuccessor(temp)
        
        else:
            self.tail.setSuccessor(temp)
            self.tail = temp
            
    def prepend(self, data):
        temp = Node(data)
        if self.isEmpty():
            pass
        elif self.tail is None:
            temp.setSuccessor(self.head)
            self.tail = self.head
        else:
            temp.setSuccessor(self.head)
        self.head = temp
    
    def insert(self, data, index):
        size = self.size()
        if index < 0 or index >= size:
            raise IndexError()
        elif index == 0:
            self.prepend(data)
        elif index == self.size():
            self.append(data)
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.getSuccessor()
            temp.setSuccessor(Node(data,temp.getSuccessor()))
            
    def replace(self, data, index):
        size = self.size()
        if index < 0 or index >= size:
            raise IndexError()
        elif index == 0:
            self.prepend(data)
        elif index == self.size() -1:
            self.append(data)
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.getSuccessor()
            temp.setElement(data)
            
    def size(self):
        if self.isEmpty():
            return 0
        
        if self.tail is None:
            return 1
        temp = self.head
        size = 1
        while temp != None and temp.getElement() != self.tail.getElement():
            temp = temp.getSuccessor()
            if temp != None:
                size += 1
        return size
    
    def delete(self, index):
        prevsize = self.size() -1
        if index < 0 or index >= prevsize +1:
            raise IndexError()
        elif index == 0 and not self.isEmpty():
            self.head = self.head.getSuccessor()
        elif index == 0:
            self.head = None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.getSuccessor()
            temp.setSuccessor(temp.getSuccessor().getSuccessor())
            if index == prevsize:
                self.tail = temp
            
    def retrieve(self, index):
        size = self.size()
        if index < 0 or index >= size:
            raise IndexError()
        elif self.isEmpty():
            raise IndexError()
        elif index == 0:
            return self.head.getElement()
        elif index == size-1:
            return self.tail.getElement()
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.getSuccessor()
            return temp.getElement()
        
    def indexOf(self, data):
        if self.isEmpty():
            return -1
        if self.tail is None and self.head.getElement() == data:
            return 0
        if self.tail is None:
            return -1
        if self.tail.getElement() == data:
            return self.size()
        temp = self.head
        size = 0
        while temp != None and temp.getElement() not in [data, self.tail.getElement()]:
            temp = temp.getSuccessor()
            size += 1
        return size
    
    def contains(self, data):
        if self.isEmpty():
            return False
        if self.tail is None and self.head.getElement() == data:
            return True
        if self.tail is None:
            return False
        if self.tail.getElement() == data:
            return True
        temp = self.head

        while temp != None and temp.getElement() not in [self.tail.getElement()]:
            temp = temp.getSuccessor()
            if temp.getElement()== data:
                return True
        return False
            
class FailedSLL(LinkedListADT): #Will fail due to not having all ABC methods implamented
    def __init__(self):
        super().__init__()
        self.head = self.tail = None


def main():
    s = SLL()
    
if __name__ == '__main__':
    main()
    