"""Appdriver for Assignment 2 book management
Honestly, i would put this in the same file as the BMS
But i'm copying the assignment 2 format
"""

def main():
    from BookManagementSystem import BookManagementSystem
    m = BookManagementSystem()
    m.displayMenu()
    
if __name__ == '__main__':
    main()
    