#Uninstaller
import os
import mysql.connector
from tkinter import messagebox

with open("weather_creds.tiak") as f:
        creds = f.read()
        creds = creds.split(",")

user = creds[0]
password = creds[1]
host = creds[2]

db_config = {
        'user': user,
        'password': password,
        'host': host,
        'auth_plugin':'mysql_native_password'
}
conn = mysql.connector.connect(**db_config, database = "weather")
cursor = conn.cursor() 
cursor.execute("drop database weather")
os.remove("weather_creds.tiak")
print("Uninstalled Successfully")
messagebox.showinfo("Information", "Uninstalled Global Weather Bulletin")
