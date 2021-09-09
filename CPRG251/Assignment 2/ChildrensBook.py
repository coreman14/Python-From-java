from Books import Books

class ChildrensBook(Books):
    """A ChildrensBook. This extends the Books object"""
    def __init__(self, ISBN: int,
                call: str,
                available: int,
                total: int,
                title: str,
                formats:str,
                authors:str):
        """Create a new ChildrensBook object

        Args:
            ISBN (int): The international standard book number
            call (str): Number to call book
            available (int): How many are available
            total (int): The total number of this book
            title (str): The title of the book
            formats (str): What kind of format (Length/difficulty)
            authors (str): Who are the authors
        """
        super().__init__(ISBN, call, available, total, title)
        self.format = formats
        self.authors = authors
        
    def __str__(self):
        doubleDecide = "Authors:" if self.getAuthors().find(",") else "Author:"
        return  "{:<18}{:<}\n"\
                "{:<18}{:<}\n"\
                "{:<18}{:<}\n"\
                "{:<18}{:<}\n"\
                "{:<18}{:<}\n"\
                "{:<18}{:<}\n"\
                "{:<18}{:<}\n\n".format(
                            "ISBN:", self.getISBN(),
                            "Call Number:", self.getCallNumber(),
                            "Available:", self.getAvailable(),
                            "Total:", self.getTotal(),
                            "Title:", self.getTitle(),
                            doubleDecide, self.getAuthors(),
                            "Format:", self.getFormatS());
                
    def formatForFile(self):
        return "{};{};{};{};{};{};{}".format(self.getISBN(),
                                            self.getCallNumber(),
                                            self.getAvailable(),
                                            self.getTotal(),
                                            self.getTitle(),
                                            self.getAuthors(),
                                            self.getFormatL());
    

    def getFormatL(self) :
        """Gets format letter
        P = Picture Book
        E = Early Readers
        C = Chapters

        Returns:
            str: The format letter
        """
        return self.format;

    
    def getFormatS(self):
        """Gets format string
        P = Picture Book
        E = Early Readers
        C = Chapters

        Returns:
            str: Expanded version of the format letter
        """
        caseFormat ="";
        c = self.getFormatL()
        if c == 'P':
            caseFormat = "Picture Book";
        elif c == 'E':
            caseFormat = "Early Readers";
        elif c == 'C':
            caseFormat = "Chapters";
        return caseFormat;

    

    def setFormat(self,formats) :
        """Sets format
        P = Picture Book
        E = Early Readers
        C = Chapters

        Args:
            format (str): Type of format
        """
        self.format = formats;


    def getAuthors(self) :
        """Returns the Authors

        Returns:
            str: The Authors
        """
        return self.authors;


    def setAuthors(self, authors) :
        """Set the Authors

        Args:
            Authors (str): The Authors
        """
        self.authors = authors;




