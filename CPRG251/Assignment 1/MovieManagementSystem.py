from InputVerify import intInputCheck
from Movie import Movie
from random import shuffle
class MovieManagementSystem():
    """Movie Management system redone in python
    """
    __FILE_NAME = "res/movies.txt"
    
    def __init__(self):
        """Constructor that creates a blank list for movies, 
        then loads all movies from __FILE_NAME
        """
        self.movies = []
        self.loadMovieList()    
    
    def displayMenu(self):
        """Displays menu and calls each method depending on choice
        """
        option = -1
        
        while (option != 4):
            print("Movie management system")
            print("1. Add new movie")
            print("2. Generate list of movies released in a year")
            print("3. Generate list of random movies")
            print("4. Exit")
            
            option = intInputCheck("Enter an option: ")
            
            
            if option == 1:
                self.addMovie()
            elif option == 2:
                self.generateMovieListInYear()
            elif option == 3:
                self.generateRandomMovieList()
            elif option == 4:
                self.saveMovieList() #passes in false to finalize txt file
            else:
                print("Invalid input, please try again.")

    def addMovie(self):
        """Creates a new movie object from input
        """

        name = ""

        while name == "": 
            name = input("Enter title of movie: ")
        year = intInputCheck("Enter year of movie: ")
        mins = intInputCheck("Enter length of movie(In minutes): ")
        tmpMovie = Movie(mins,name,year)
        self.movies.append(tmpMovie)
        print("\nMovie added\n")
            
    
    def generateMovieListInYear(self):
        """Outputs text after finding a movie with matching input year
        """
        duration = 0
        year = intInputCheck("Enter year: ")
        print("Movie list")
        print("{:<15s}{:<6}{}".format( "Duration","Year","Title"))
        for tmpMovie in self.movies:
            if (tmpMovie.year == year):
                duration += tmpMovie.mins
                print(tmpMovie)
        #Duration could be done with a genorater if not for the need to print
        #duration = sum(x.year for x in self.movies if isinstance(x,Movie) and x.year == year)
        
        print(f"\nTotal Duration: {duration}")
        print()
    
    def generateRandomMovieList(self):
        """Outputs text after shuffling the arraylist that contains all of them,
        checking if movie has already been outputted, then shuffling again if
        needs to
        """
        duration = 0
        num = intInputCheck("Enter number of movies: ")
        print("Movie list")
        print("{:<15s}{:<6}{}".format( "Duration","Year","Title"))
        randomCheck = [] #holds outputted movie
        shuffle(self.movies)
        for _ in num+1:
            while (self.movies[3] in randomCheck): # reshuffles if already outputted
                shuffle(self.movies)
            randomCheck.append(self.movies[3])
            duration += self.movies[3].mins # 
            print(self.movies[3])
            num -= 1
        
        print(f"\nTotal Duration: {duration}")
        print()
    
    def loadMovieList(self):
        """Input movies from __FILE_RES
        """
        with open(MovieManagementSystem.__FILE_NAME,"r") as f:
            for curLine in f.readlines():
                splitLine = curLine.split(",")
                tmpMovie = Movie(int(splitLine[0]),splitLine[1],int(splitLine[2]))
                self.movies.append(tmpMovie)
        print("File Loaded")
        
    def saveMovieList(self): #outputs
        """Output movies to __FILE_RES
        """
        with open(MovieManagementSystem.__FILE_NAME,"w+") as f:
            for tmpMovies in self.movies:
                f.write(tmpMovies.formatForFile())
        print("Saved changes")

        
    
