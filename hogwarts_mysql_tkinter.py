# 20240711 SMW
# show score of 4 Harry Potter houses. 
# able to add and remove points from each house
# modified version to save scores in a mysql db

import mysql.connector
import configparser
import tkinter as tk

# read mysql password from config file
config = configparser.ConfigParser()
config.read('C:\\ProgramData\\MySQL\\MySQL Server 9.0\\mypw.ini')

# Database connection details (replace with your credentials)
db_host = "localhost"
db_name = "hp"
db_user = "root"
db_password = config['client']['password']

def get_house_points():
    connection = mysql.connector.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()
    cursor.execute("SELECT name, score FROM houses")
    results = cursor.fetchall()
    house_points = {}
    for row in results:
        house_points[row[0]] = row[1]
    connection.close()
    return house_points

def update_score(house, delta):
    connection = mysql.connector.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE houses SET score = score + %s WHERE name = %s", (delta, house))
    connection.commit()
    connection.close()
    house_points[house] += delta
    update_display()

def update_display():
    house_points = get_house_points()
    for house, score in house_points.items():
        house_labels[house].config(text=f"{house}: {score}")  # Update specific label using house name

# Main program
window = tk.Tk()
window.title("Hogwarts House Scores")
window.geometry("600x500")  # Adjust width and height as desired

house_points = get_house_points()

# House labels and scores
house_labels = {}  # Dictionary to store house labels
# House labels and scores
for house, score in house_points.items():
    house_label = tk.Label(window, text=f"{house}: {score}", font=("Arial", 18))
    house_label.pack()
    house_labels[house] = house_label  # Store label in dictionary with house name as key

# Button functions (lambda functions for brevity)
def on_up_click(house):
    house_points[house] += 10  # Update in-memory dictionary
    house_label.config(text=f"{house}: {house_points[house]}")  # Update label text

def on_down_click(house):
    house_points[house] -= 10  # Update in-memory dictionary
    house_label.config(text=f"{house}: {house_points[house]}")  # Update label text

# Bind click events to buttons
for house in house_points.keys():
    up_button = tk.Button(window, text="▲", command=lambda house=house: on_up_click(house))
    up_button.pack(side=tk.LEFT)
    
    down_button = tk.Button(window, text="▼", command=lambda house=house: on_down_click(house))
    down_button.pack(side=tk.LEFT)
    
    spacer = tk.Frame(window, width=20)  # Adjust the width as needed
    spacer.pack(side=tk.LEFT)

window.mainloop()