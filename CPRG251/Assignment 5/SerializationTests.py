import unittest
from unittest.main import main
from SLL import SLL
from User import User
import pickle
import sys
class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.users = SLL()
        self.users.append(User(1, "Joe Blow", "jblow@gmail.com", "password"))
        self.users.append(User(2, "Joe Schmoe", "joe.schmoe@outlook.com", "abcdef"))
        self.users.append(User(3, "Colonel Sanders", "chickenlover1890@gmail.com", "kfc5555"))
        self.users.append(User(4, "Ronald McDonald", "burgers4life63@outlook.com", "mcdonalds999"))
        
        
    def tearDown(self):
        self.users.clear()
        
    def testSerialize(self):
        b = pickle.dumps(self.users)
        self.assertTrue(isinstance(b,bytes))
        self.assertTrue(sys.getsizeof(b) > 0)
    
    def testDeserialize(self):
        b = pickle.dumps(self.users)
        b2 = pickle.loads(b)
        
        self.assertFalse(self.users.isEmpty());
        
        expectedUser1 = User(1, "Joe Blow", "jblow@gmail.com", None);
        actualUser1 = self.users.retrieve(0);
        
        self.assertEqual(expectedUser1, actualUser1);
        self.assertTrue(actualUser1.isCorrectPassword("password"));
        
        expectedUser2 = User(2, "Joe Schmoe", "joe.schmoe@outlook.com", None);
        actualUser2 = self.users.retrieve(1);
        
        self.assertEqual(expectedUser2, actualUser2);
        self.assertTrue(actualUser2.isCorrectPassword("abcdef"));
        
        expectedUser3 = User(3, "Colonel Sanders", "chickenlover1890@gmail.com", None);
        actualUser3 = self.users.retrieve(2);
        
        self.assertEqual(expectedUser3, actualUser3);
        self.assertTrue(actualUser3.isCorrectPassword("kfc5555"));
        
        expectedUser4 = User(4, "Ronald McDonald", "burgers4life63@outlook.com", None);
        actualUser4 = self.users.retrieve(3);
        
        self.assertEqual(expectedUser4, actualUser4);
        self.assertTrue(actualUser4.isCorrectPassword("mcdonalds999"));
        
if __name__ == '__main__':
    unittest.main()
    