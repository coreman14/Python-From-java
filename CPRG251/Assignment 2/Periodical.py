from Books import Books

class Periodical(Books):
    """A periodical. This extends the Books object"""
    def __init__(self, ISBN: int,
                call: str,
                available: int,
                total: int,
                title: str,
                frequency:str):
        """Create a new periodical object

        Args:
            ISBN (int): The international standard book number
            call (str): Number to call book
            available (int): How many are available
            total (int): The total number of this book
            title (str): The title of the book
            frequency (str): What kind of format (Length/difficulty)
        """
        super().__init__(ISBN, call, available, total, title)
        self.frequency = frequency
        
    def __str__(self):
        return  "{:<18}{:<}\n"\
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
                            "Format:", self.getfrequencyS());
                
    def formatForFile(self):
        return "{};{};{};{};{};{}".format(self.getISBN(),
                                            self.getCallNumber(),
                                            self.getAvailable(),
                                            self.getTotal(),
                                            self.getTitle(),
                                            self.getfrequencyL());
    

    def getfrequencyL(self) :
        """Gets frequency letter
        D = Daily
        W = Weekly
        M = Monthly
        B = BiMonthly
        Q = Quarterly

        Returns:
            str: The frequency letter
        """
        return self.frequency;

    
    def getfrequencyS(self):
        """Gets frequency string
        D = Daily
        W = Weekly
        M = Monthly
        B = BiMonthly
        Q = Quarterly


        Returns:
            str: Expanded version of the frequency letter
        """
        caseFormat ="";
        c = self.getfrequencyL()
        if c == 'D':
            caseFormat = "Daily";    
        elif c == 'W':
            caseFormat = "Weekly";    
        elif c == 'M':
            caseFormat = "Monthly";    
        elif c == 'B':
            caseFormat = "BiMonthly";    
        elif c == 'Q':
            caseFormat = "Quarterly";    
        return caseFormat;

    

    def setfrequency(self,frequency) :
        """Sets frequency
        P = Picture Book
        E = Early Readers
        C = Chapters

        Args:
            frequency (str): Type of frequency
        """
        self.frequency = frequency;





