from Books import Books

class Paperback(Books):
    """A Paperback. This extends the Books object"""
    def __init__(self, ISBN: int,
                call: str,
                available: int,
                total: int,
                title: str,
                genre:str,
                authors:str,
                year:int ):
        """Create a new Paperback object

        Args:
            ISBN (int): The international standard book number
            call (str): Number to call book
            available (int): How many are available
            total (int): The total number of this book
            title (str): The title of the book
            Genre (str): What kind of Genre it follows
            authors (str): Who published it
            year (int): What year it was published
        """
        super().__init__(ISBN, call, available, total, title)
        self.genre = genre
        self.authors = authors
        self.year = year
        
    def __str__(self):
        doubleDecide = "Authors:" if self.getAuthors().find(",") else "Author:"
        return  "{:<18}{:<}\n"\
                "{:<18}{:<}\n"\
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
                            "Year", self.getYear(),
                            "Genre:", self.getGenreS());
                
    def formatForFile(self):
        return "{};{};{};{};{};{};{};{}".format(self.getISBN(),
                                            self.getCallNumber(),
                                            self.getAvailable(),
                                            self.getTotal(),
                                            self.getTitle(),
                                            self.getAuthors(),
                                            self.getYear(),
                                            self.getGenreL());
    

    def getGenreL(self) :
        """Gets Genre letter
        A = Adventure
        D = Drama
        E = Education
        C = Classic
        F = Fantasy
        S = Science Fiction

        Returns:
            str: The Genre letter
        """
        return self.genre;

    
    def getGenreS(self):
        """Gets Genre string
        A = Adventure
        D = Drama
        E = Education
        C = Classic
        F = Fantasy
        S = Science Fiction

        Returns:
            str: Expanded version of the Genre letter
        """
        caseFormat ="";
        c = self.getGenreL()
        if c == 'A':
            caseFormat = "Adventure";
        elif c == 'D':
            caseFormat = "Drama";
        elif c == 'E':
            caseFormat = "Education";
        elif c == 'C':
            caseFormat = "Classic";
        elif c == 'F':
            caseFormat = "Fantasy";
        elif c == 'S':
            caseFormat = "Science Fiction";
        return caseFormat;

    

    def setGenre(self,genre) :
        """Sets Genre
        A = Adventure
        D = Drama
        E = Education
        C = Classic
        F = Fantasy
        S = Science Fiction

        Args:
            Genre (str): Type of Genre
        """
        self.genre = genre;


    def getAuthors(self) :
        """Returns the authors

        Returns:
            str: The authors
        """
        return self.authors;


    def setAuthors(self, authors) :
        """Set the authors

        Args:
            authors (str): The authors
        """
        self.authors = authors;

    def getYear(self):
        """Returns the year the book was published

        Returns:
            int: the year the book was published

        """
        return self.year

    def setYear(self,year):
        """Sets the year the book was published

        Args:
            year (int): the year the book was published

        """
        self.year = year


