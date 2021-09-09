from ChildrensBook import ChildrensBook
from Cookbook import Cookbook
from Paperback import Paperback
from Periodical import Periodical
from InputVerify import intInputCheck
from random import shuffle
class BookManagementSystem:
    __FILE_NAME__ = "res/books.txt";
    
    def __init__(self):
        self.books = []
        self.loadBookList()
        
    def displayMenu(self):
        
        option = -1;
        
        while (option != 5) :
            print("Book management system");
            print("1. Checkout Book");
            print("2. Find Books by Title");
            print("3. Display Books by type");
            print("4. Produce Random Book List");
            print("5. Save & Exit");
            option = intInputCheck("Enter an option:");

            if option ==1:
                self.checkoutBook();
            elif option ==2:
                self.findBooksByTitle();
            elif option ==3:
                self.displayBooksByType();
            elif option ==4:
                self.generateRandomBookList();
            elif option ==5:
                self.saveBookList(); #passes in false to finalize txt file
            else:
                print("Invalid input, please try again.");
            
        
        
    def displayBooksByType(self) :
        print("\nEnter number of type");
        print("\n1. Children's Books");
        print("2. Cookbooks");
        print("3. Paperbacks");
        print("4. Periodicals");
        num = intInputCheck("\nEnter type of book: ");
        if num == 1:
            t = input("Enter Format of the book (P for Picture Book, E for Early Readers, or C for Chapters):");
        elif num == 2:
            t = input("Enter Format of the book (D for Diabetic, V for Vegetarian, G for Gluten-free, I for International, or N for None):");
        elif num == 3:
            t = input("Enter Format of the book (A for Adventure, D for Drama, E for Education, C for Classic, F for Fantasy, or S for Science Fiction):");
        elif num == 4:
            t = input("Enter Format of the book (D for Daily, W for Weekly, M for Monthly, B for BiMonthly,or Q for Quarterly):");
        found = False
        t = t.lower()
        for book in self.books:
            if num==1 and isinstance(book,ChildrensBook) and book.getFormatL().lower() == t:
                print(book);
                found = True;
            
            elif (num==2 and isinstance(book,Cookbook) and book.getDietL().lower() == t):
                print(book);
                found = True;
        
            elif (num==3 and isinstance(book,Paperback) and book.getGenreL().lower() == t):
                print(book);
                found = True;
            
            elif (num==4 and isinstance(book,Periodical) and book.getFrequencyL().lower() == t):
                print(book);
                found = True
        
        if(not found) :
            print("\nCould not find a book matching the criteria");
        
    def checkoutBook(self) :
        check = True
        isbn = intInputCheck("Enter ISBN of book: ");
        for book in self.books:
            if(isbn == book.getISBN()) :
                print("The book \"" + str(book.getTitle()) + "\" has been checked out." );
                print("It can be located using the call number: " + str(book.getCallNumber()));
                book.setAvailable(book.getAvailable() -1);
                check = False;
                break;
            
        if(check) :
            print("Couldn't find ISBN:" + str(isbn) +". Please check the number and try again");
        
            
    def findBooksByTitle(self):
        search = input("Enter title to search for: ").lower()
        found = False;
        for book in self.books:
            if search in book.getTitle().lower():
                print(book);
                found = True
        if(not found):
            print("\nCould not find a book matching the criteria");        

    def generateRandomBookList(self):
        num = intInputCheck("Enter number of books: ");
        print("Random book:");
        randomCheck = set(); #holds outputted book
        shuffle(self.books)
        while (num != 0) :
            while (self.books[3] in randomCheck): # reshuffles if already outputted
                shuffle(self.books);
            randomCheck.add(self.books[3])
            print(self.books[3]);
            num -= 1;

    def loadBookList(self):
        with open(self.__FILE_NAME__,"r") as f:
                for curLine in f.readlines():
                    splitLine = curLine.split(";");
                    isbn = int(splitLine[0][-1])
                    if isbn in {1,0}:
                        tmpBook = ChildrensBook(int(splitLine[0]), splitLine[1], int(splitLine[2]), int(splitLine[3]), splitLine[4], splitLine[6][0], splitLine[5]);
                    elif isbn in {2,3}:
                        tmpBook = Cookbook(int(splitLine[0]), splitLine[1], int(splitLine[2]), int(splitLine[3]), splitLine[4], splitLine[6][0], splitLine[5]);
                    elif isbn in {4,5,6,7}:
                        tmpBook = Paperback(int(splitLine[0]), splitLine[1], int(splitLine[2]), int(splitLine[3]), splitLine[4], splitLine[7][0], splitLine[5],int(splitLine[6]));
                    elif isbn in {8,9}:
                        tmpBook = Periodical(int(splitLine[0]), splitLine[1], int(splitLine[2]), int(splitLine[3]), splitLine[4], splitLine[5][0]);
                    
                    self.books.append(tmpBook);

                
                print("File Loaded");
    
    def saveBookList(self):
        with open(self.__FILE_NAME,"w+") as f:
            for tmpMovies in self.books:
                f.write(tmpMovies.formatForFile()+"\n")
        print("Saved changes")