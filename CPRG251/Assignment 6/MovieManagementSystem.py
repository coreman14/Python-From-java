from InputVerify import intInputCheck
from Movie import Movie
from random import shuffle
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import OperationalError
class MovieManagementSystem():
    """Movie Management system redone in python
    """
    
    def __init__(self):
        load_dotenv()
        """Constructor that creates a blank list for movies
        """
        
        
        self.movies = []
        self.driver = psycopg2.connect(
        database=os.getenv("DB"),
        user=os.getenv("ESER"),
        password=os.getenv("PASSWERD"),
        host=os.getenv("HEST"),
        port=5432
        );
        self.driver.autocommit = True
        
    
    def displayMenu(self):
        """Displays menu and calls each method depending on choice
        """
        option = -1
        
        while (option != 5):
            print("Movie management system")
            print("1. Add new movie")
            print("2. Generate list of movies released in a year")
            print("3. Generate list of random movies")
            print("4. Delete movie by id");
            print("5. Exit")
            
            option = intInputCheck("Enter an option: ")
            
            
            if option == 1:
                self.addMovie()
            elif option == 2:
                self.generateMovieListInYear()
            elif option == 3:
                self.generateRandomMovieList()
            elif option == 4:
                self.deleteMovieById()
            elif option == 5:
                self.driver.close()
                print("Closing.")
            else:
                print("Invalid input, please try again.")

    def deleteMovieById(self):
        
        num = intInputCheck("Enter id of movie to delete:");
        try:
            cursor = self.driver.cursor();
            cursor.execute("DELETE FROM moviemanagementdb.movies WHERE id ="+str(num)+";")
        except OperationalError as e:
            e.printStackTrace();
        
    

    def addMovie(self):
        """Creates a new movie object from input
        """

        name = ""

        while name == "": 
            name = input("Enter title of movie: ")
        year = intInputCheck("Enter year of movie: ")
        mins = intInputCheck("Enter length of movie(In minutes): ")
        try:
            cursor = self.driver.cursor()
            cursor.execute(f"INSERT INTO moviemanagementdb.movies (duration, title, year) VALUES ({mins}, '{name}', {year});")
        except OperationalError as e:
            e.printStackTrace()
        print("\nMovie added\n")
            
    
    def generateMovieListInYear(self):
        """Outputs text after finding a movie with matching input year
        """
        duration = 0
        year = intInputCheck("Enter year: ")
        print("Movie list")
        print("{:<5}{:<15s}{:<6}{}".format( "ID","Duration","Year","Title"))
        try:
            cursor = self.driver.cursor()
            cursor.execute(f"SELECT * FROM moviemanagementdb.movies WHERE YEAR = {year};");
            rs = cursor.fetchall()
            for r in rs:
                ids, mins, name, year = r
                print("{:<5}{:<15}{:<6}{}".format( ids, mins, year, name))
                duration += mins
            if len(rs) == 0:
                print("No movies were found with that year")
        except OperationalError as e:
            e.printStackTrace()   
        
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
        print("{:<5}{:<15s}{:<6}{}".format( "ID","Duration","Year","Title"))
        try:
            cursor = self.driver.cursor()
            cursor.execute(f"SELECT * FROM moviemanagementdb.movies;");
            rs = cursor.fetchall()
            shuffle(rs)
            shuffle(rs)
            for r in rs:
                ids, mins, name, year = r
                print("{:<5}{:<15}{:<6}{}".format( ids, mins, year, name))
                duration += mins
                if num < 1:
                    break;
                else:
                    num -= 1
        except OperationalError as e:
            e.printStackTrace()   
        
        print(f"\nTotal Duration: {duration}")
        print()
    
