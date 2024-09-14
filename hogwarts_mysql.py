# 20240714 SMW
# show score of 4 Harry Potter houses. 
# able to add and remove points from each house
# modified version to save scores in a mysql db

import mysql.connector
import configparser

# connect to mysql db
def connect_to_mysql():
    config = configparser.ConfigParser()
    config.read('C:\\ProgramData\\MySQL\\MySQL Server 9.0\\mypw.ini')

    # define db values
    db_host = "localhost"
    db_name = "hp"
    db_user = "root"
    db_password = config['client']['password']

    # connect to mysql db. show error if it fails to connect
    try:
        connection = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        cursor = connection.cursor()
    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        exit()
    return cursor, connection

# define function to get points from db
def get_house_points(cursor):
    cursor.execute("SELECT name, score FROM houses")
    results = cursor.fetchall()
    house_points = {}
    for column in results:
        house_points[column[0]] = column[1]
    return house_points

# define a function to initialize scores
def initialize_score(cursor, connection):
    # check if table exists
    cursor.execute(f"SHOW TABLES LIKE 'houses'")
    table_exists = cursor.fetchone() is not None
    # update values in exisiting table
    if table_exists:
        table_exists = 1
        cursor.execute("UPDATE houses SET score = %s WHERE name = %s", (170, "Gryffindor"))
        cursor.execute("UPDATE houses SET score = %s WHERE name = %s", (250, "Hufflepuff"))
        cursor.execute("UPDATE houses SET score = %s WHERE name = %s", (130, "Ravenclaw"))
        cursor.execute("UPDATE houses SET score = %s WHERE name = %s", (140, "Slytherin"))
        connection.commit()

    # create table if it does not exist  
    else:
        table_exists = 0
        cursor.execute("CREATE TABLE IF NOT EXISTS houses (name VARCHAR(50), score VARCHAR(50))")
        cursor.execute("INSERT INTO houses (name, score) VALUES ('Gryffindor', 170)", )
        cursor.execute("INSERT INTO houses (name, score) VALUES ('Hufflepuff', 250)", )
        cursor.execute("INSERT INTO houses (name, score) VALUES ('Ravenclaw', 130)", )
        cursor.execute("INSERT INTO houses (name, score) VALUES ('Slytherin', 140)", )
        connection.commit()

### main ###
if __name__ == "__main__":
    cursor, connection = connect_to_mysql()
    initialize_score(cursor, connection)

    # loop until quit selected
    end=0
    while(end == 0):
        print("\n\n----------------------")
        house_points = get_house_points(cursor)
        print("Gryffindor=",house_points["Gryffindor"])
        print("Hufflepuff=",house_points["Hufflepuff"])
        print("Ravenclaw=",house_points["Ravenclaw"])
        print("Slytherin=",house_points["Slytherin"])
        print("----------------------\n")
        print("1) Change Points for Gryffindor")
        print("2) Change Points for Hufflepuff")
        print("3) Change Points for Ravenclaw")
        print("4) Change Points for Slytherin")
        print("5) Declare house winner and quit program")
        print("6) Reset all scores to end of first book")
        selected=input()
        if selected == "1":
            print("\nAdd/Remove how many points to Gryffindor: ")
            points=int(input())
            print("Professor Mcgonagall: ",points," points to Gryffindor")
            cursor.execute("UPDATE houses SET score = score + %s WHERE name = %s", (points, "Gryffindor"))
            connection.commit()  # Save changes to the database
        if selected == "2":
            print("\nAdd/Remove how many points to Hufflepuff: ")
            points=int(input())
            print("Professor Sprout: ",points," points to Hufflepuff")
            cursor.execute("UPDATE houses SET score = score + %s WHERE name = %s", (points, "Hufflepuff"))
            connection.commit()  # Save changes to the database
        if selected == "3":
            print("\nAdd/Remove how many points to Ravenclaw: ")
            points=int(input())
            print("Professor Flitwick: ",points," points to Ravenclaw")
            cursor.execute("UPDATE houses SET score = score + %s WHERE name = %s", (points, "Ravenclaw"))
            connection.commit()  # Save changes to the database
        if selected == "4":
            print("\nAdd/Remove how many points to Slytherin: ")
            points=int(input())
            print("Professor Snape: ",points," points to Slytherin")
            cursor.execute("UPDATE houses SET score = score + %s WHERE name = %s", (points, "Slytherin"))
            connection.commit()  # Save changes to the database
        if selected == "5":
            # check to see which house won
            house_points = get_house_points(cursor)
            if (house_points["Gryffindor"] > house_points["Slytherin"]) and (house_points["Gryffindor"] > house_points["Ravenclaw"]) and (house_points["Gryffindor"] > house_points["Hufflepuff"]):
                print("Professor Mcgonagall: Gryffindor wins the house cup!")
            elif (house_points["Slytherin"] > house_points["Gryffindor"]) and (house_points["Slytherin"] > house_points["Ravenclaw"]) and (house_points["Slytherin"] > house_points["Hufflepuff"]):
                print("Professor Snape: Slytherin wins the house cup!")
            elif (house_points["Ravenclaw"] > house_points["Slytherin"]) and (house_points["Ravenclaw"] > house_points["Gryffindor"]) and (house_points["Ravenclaw"] > house_points["Hufflepuff"]):
                print("Professor Flitwick: Ravenclaw wins the house cup!")
            elif (house_points["Hufflepuff"] > house_points["Slytherin"]) and (house_points["Hufflepuff"] > house_points["Gryffindor"]) and (house_points["Hufflepuff"] > house_points["Ravenclaw"]):
                print("Professor Sprout: Hufflepuff wins the house cup!")
            end=1
        if selected == "6":
            initialize_score()
