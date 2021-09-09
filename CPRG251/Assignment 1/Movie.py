class Movie():
    __slots__ = ["mins","year","name"] #An actually way to make a class somewhat not as big
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
        
    #Removed getters and setters as theres is nothing fancy going on with them
    
    


    def __str__(self):
        """Returns a formatted string for output
        Returns in order of (Mins,Year,Name)
        Returns:
            str: A string for output in a list (Mins,Year,Name)
        """
        return f"{self.mins:<15}{self.year:<6}{self.name}"

    

    def formatForFile(self):
        """Returns the movie in a csv format
        Returns in order of (Mins,Name,Year)
        Returns:
            str: The movie in a CSV format (Mins,Name,Year)
        """
        return f"{self.mins},{self.name},{self.year}\n"
    
    
    