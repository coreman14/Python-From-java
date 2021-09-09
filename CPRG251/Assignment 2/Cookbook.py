from Books import Books

class Cookbook(Books):
    """A Cookbook. This extends the Books object"""
    def __init__(self, ISBN: int,
                call: str,
                available: int,
                total: int,
                title: str,
                diet:str,
                publisher:str):
        """Create a new cookbook object

        Args:
            ISBN (int): The international standard book number
            call (str): Number to call book
            available (int): How many are available
            total (int): The total number of this book
            title (str): The title of the book
            diet (str): What kind of diet it follows
            publisher (str): Who published it
        """
        super().__init__(ISBN, call, available, total, title)
        self.diet = diet
        self.publisher = publisher
        
    def __str__(self):
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
                            "Publisher:", self.getPublisher(),
                            "Diet:", self.getDietS());
                
    def formatForFile(self):
        return "{};{};{};{};{};{};{}".format(self.getISBN(),
                                            self.getCallNumber(),
                                            self.getAvailable(),
                                            self.getTotal(),
                                            self.getTitle(),
                                            self.getPublisher(),
                                            self.getDietL());
    

    def getDietL(self) :
        """Gets diet letter
        D = Diabetic 
        V = Vegetarian 
        G = Gluten-free
        I = International 
        N = None

        Returns:
            str: The diet letter
        """
        return self.diet;

    
    def getDietS(self):
        """Gets diet string
        D = Diabetic 
        V = Vegetarian 
        G = Gluten-free
        I = International 
        N = None

        Returns:
            str: Expanded version of the diet letter
        """
        caseFormat ="";
        c = self.getDietL()
        if c == 'D':
            caseFormat = "Diabetic";
        elif c == 'G':
            caseFormat = "Gluten-free";
        elif c == 'I':
            caseFormat = "International";
        elif c == 'N':
            caseFormat = "None"
        elif c == 'V':
            caseFormat = "Vegetarian";
        return caseFormat;

    

    def setDiet(self,diet) :
        """Sets diet
        D = Diabetic 
        V = Vegetarian 
        G = Gluten-free
        I = International 
        N = None

        Args:
            diet (str): Type of diet
        """
        self.diet = diet;


    def getPublisher(self) :
        """Returns the publisher

        Returns:
            str: The publisher
        """
        return self.publisher;


    def setPublisher(self, publisher) :
        """Set the publisher

        Args:
            publisher (str): The publisher
        """
        self.publisher = publisher;




