import psycopg2
from psycopg2 import OperationalError
def main():


    try:
        driver = psycopg2.connect(
        database="d1st1ft1hrd1fi",
        user="qwhcvforvbglsi",
        password="fb61a22f6457f9b74cb9b1270f7ed14bbfb6f4f66517fdccb56782dc96b47b87",
        host="ec2-44-196-170-156.compute-1.amazonaws.com",
        port=5432
        );
        driver.autocommit = True
        print("Connected!");
        cursor = driver.cursor()
        year = 2000
        cursor.execute(f"SELECT * FROM moviemanagementdb.movies WHERE YEAR = {year};");
        rs = cursor.fetchall()
        
        for r in rs:        
            ids, mins, name, year = r
            print("{:<5}{:<10}{:<6}{}".format( ids, mins, year, name))
        
        
        
        driver.close()
    except OperationalError as e:
        e.printStackTrace()
    
    
    
if __name__ == '__main__':
    main()
    