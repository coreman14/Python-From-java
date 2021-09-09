import unittest
from SLL import SLL

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linkedList = SLL()
        
    def tearDown(self):
        self.linkedList.clear()
        


    def testIsEmpty(self) :
        self.assertTrue(self.linkedList.isEmpty());
        self.assertEqual(0, self.linkedList.size());
    
    
    def testAppendNode(self) :
        self.linkedList.append("a");
        self.linkedList.append("b");
        self.linkedList.append("c");
        self.linkedList.append("d");
        
        # Test the linked list is not empty.
        
        self.assertFalse(self.linkedList.isEmpty());
        
        # Test the size is 4
        self.assertEqual(4, self.linkedList.size());

        # Test the first node value is a
        self.assertEqual("a", self.linkedList.retrieve(0));

        # Test the second node value is b
        self.assertEqual("b", self.linkedList.retrieve(1));
        
        # Test the third node value is c
        self.assertEqual("c", self.linkedList.retrieve(2));
        
        # Test the fourth node value is d
        self.assertEqual("d", self.linkedList.retrieve(3));
    

    def testPrependNodes(self) :
        self.linkedList.prepend("a");
        self.linkedList.prepend("b");
        self.linkedList.prepend("c");
        self.linkedList.prepend("d");

        
        # Test the linked list is not empty.
        self.assertFalse(self.linkedList.isEmpty());
        
        # Test the size is 4
        self.assertEqual(4, self.linkedList.size());

        # Test the first node value is a
        self.assertEqual("d", self.linkedList.retrieve(0));

        # Test the second node value is b
        self.assertEqual("c", self.linkedList.retrieve(1));
        
        # Test the third node value is c
        self.assertEqual("b", self.linkedList.retrieve(2));
        
        # Test the fourth node value is d
        self.assertEqual("a", self.linkedList.retrieve(3));
    
    

    def testInsertNode(self) :
        self.linkedList.append("a");
        self.linkedList.append("b");
        self.linkedList.append("c");
        self.linkedList.append("d");
        
        self.linkedList.insert("e", 2);

        
        # Test the linked list is not empty.
        self.assertFalse(self.linkedList.isEmpty());
        
        # Test the size is 4
        self.assertEqual(5, self.linkedList.size());

        # Test the first node value is a
        self.assertEqual("a", self.linkedList.retrieve(0));

        # Test the second node value is b
        self.assertEqual("b", self.linkedList.retrieve(1));
        
        # Test the third node value is e
        self.assertEqual("e", self.linkedList.retrieve(2));
        
        # Test the third node value is c
        self.assertEqual("c", self.linkedList.retrieve(3));
        
        # Test the fourth node value is d
        self.assertEqual("d", self.linkedList.retrieve(4));
    
    

    def testReplaceNode(self) :
        self.linkedList.append("a");
        self.linkedList.append("b");
        self.linkedList.append("c");
        self.linkedList.append("d");
        
        self.linkedList.replace("e", 2);

        
        # Test the linked list is not empty.
        self.assertFalse(self.linkedList.isEmpty());
        
        # Test the size is 4
        self.assertEqual(4, self.linkedList.size());

        # Test the first node value is a
        self.assertEqual("a", self.linkedList.retrieve(0));

        # Test the second node value is b
        self.assertEqual("b", self.linkedList.retrieve(1));
        
        # Test the third node value is e
        self.assertEqual("e", self.linkedList.retrieve(2));
        
        # Test the fourth node value is d
        self.assertEqual("d", self.linkedList.retrieve(3));
    
    

    def testDeleteNode(self) :
        self.linkedList.append("a");
        self.linkedList.append("b");
        self.linkedList.append("c");
        self.linkedList.append("d");
        
        self.linkedList.delete(2);
        
        # Test the linked list is not empty.
        self.assertFalse(self.linkedList.isEmpty());
        
        # Test the size is 4
        self.assertEqual(3, self.linkedList.size());

        # Test the first node value is a
        self.assertEqual("a", self.linkedList.retrieve(0));

        # Test the second node value is b
        self.assertEqual("b", self.linkedList.retrieve(1));
        
        # Test the fourth node value is d
        self.assertEqual("d", self.linkedList.retrieve(2));
    

    def testFindNode(self) :
        self.linkedList.append("a");
        self.linkedList.append("b");
        self.linkedList.append("c");
        self.linkedList.append("d");

        
        contains = self.linkedList.contains("b");
        self.assertTrue(contains);
        
        index = self.linkedList.indexOf("b");
        self.assertEqual(1, index);
        
        value = self.linkedList.retrieve(1);
        self.assertEqual("b", value);
    
if __name__ == '__main__':
    unittest.main()