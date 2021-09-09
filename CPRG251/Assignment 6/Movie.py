class Movie():
    def __init__(self, mins:int, name:str, year:int):
        """Creates an object and assign the respective args

        Args:
            mins (int): Length of the movie
            name (str): Name of the movie
            year (int): Year the movie was released
        """
        self.mins = mins
        self.year = year
        self.name = name
        
    def getYear(self):
        """Returns the year of the movie

        Returns:
            int: The year of the movie
        """
        return self.year;
    

    def setYear(self, year):
        """Sets the year of the movie

        Args:
            year (int): The year of the movie
        """
        self.year = year;
    

    def getMins(self):
        """Returns the length of the movie in minutes

        Returns:
            int: The length of the movie
        """
        return self.mins;
    

    def setMins(self,mins):
        """Sets the length of the movie in minutes

        Args:
            mins (int): The length of the movie
        """
        self.mins = mins;
    

    def getName(self):
        """Returns the name of the movie

        Returns:
            str: The name of the movie
        """
        return self.name;
    

    def setName(self, name):
        """Sets the name of the movie

        Args:
            name (str): The name of the movie
        """
        self.name = name;
    


    def __str__(self):
        """Returns a formatted string for output
        Returns in order of (Mins,Year,Name)
        Returns:
            str: A string for output in a list (Mins,Year,Name)
        """
        return f"{self.getMins():<15}{self.getYear():<6}{self.getName()}"

    

    def formatForFile(self):
        """Returns the movie in a csv format
        Returns in order of (Mins,Name,Year)
        Returns:
            str: The movie in a CSV format (Mins,Name,Year)
        """
        return f"{self.getMins()},{self.getName()},{self.getYear()}\n"
    
    
    