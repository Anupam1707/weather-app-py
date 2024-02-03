#Installer for Weather App
from sql_scripts import *
try:
    with open("weather_creds.tiak") as f:
        creds = f.read()
        creds = creds.split(",")
except FileNotFoundError:
    import mysql.connector
    import os
    import time
    from tkinter import simpledialog
    connection = None

    user = simpledialog.askstring(title="Global Weather Buttetin",prompt="SQL Username")
    if user is not None:
        password = simpledialog.askstring(title="Global Weather Buttetin",prompt="SQL Password", show = "*")
        if password is not None:
            host = simpledialog.askstring(title="Global Weather Buttetin",prompt="SQL Hostname")
            if host is not None:
                creds = [user + ",", password+",", host]
                with open("weather_creds.tiak","w") as f:
                    pass
                with open("weather_creds.tiak", "a") as f:
                    for i in creds:
                        f.write(i)
