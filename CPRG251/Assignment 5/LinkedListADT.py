from abc import ABC, abstractmethod

"""
Note for ABC interfaces. 

If you have to use all of the @abstractmethods or else it wont allow you to initiate the class

Otherwise, just make this class with no @ and you do about the same thing. It's get complicated when you need to subclass out without it being a type of this subclass



"""

class LinkedListADT(ABC):
    @abstractmethod
    def isEmpty(self):
        pass
    @abstractmethod
    def clear(self):
        pass
    @abstractmethod
    def append(self, data):
        pass
    @abstractmethod
    def prepend(self, data):
        pass
    @abstractmethod
    def insert(self, data, index):
        pass
    @abstractmethod
    def replace(self, data, index):
        pass
    @abstractmethod
    def size(self):
        pass
    @abstractmethod
    def delete(self, index):
        pass
    @abstractmethod
    def retrieve(self, index):
        pass
    @abstractmethod
    def indexOf(self, data):
        pass
    @abstractmethod
    def contains(self, data):
        pass