import os
try:
    import mysql.connector
    import pandas as pd
except ImportError:
    os.system("pip install mysql.connector")
    os.system("pip install pandas")

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

# Establish a connection to the MySQL server
def connect_to_database():
    try:
        conn = mysql.connector.connect(**db_config, database = "weather")
        if conn is not None:
            return conn  # Return the connection without executing "USE datasense"
    except mysql.connector.Error as err:
        print("Error:", err)
    return None

conn = connect_to_database()

def save_excel(table):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE weather")
            query = f"SELECT * FROM {table}"
            try:
                data = pd.read_sql(query, conn)
                data.to_excel(f"{table}.xlsx", index=False)
            except pd.errors.DatabaseError:
                print("Incorrect Query")
        except Warning:
            pass

def save_csv(table):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE weather")
            query = f"SELECT * FROM {table}"
            try:
                data = pd.read_sql(query, conn)
                data.to_csv(f"{table}.csv", index=False)
            except pd.errors.DatabaseError:
                print("Incorrect Query")
        except Warning:
            pass

def custom_query_save_csv(query):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE weather")
            try:
                data = pd.read_sql(query, conn)
                data.to_csv("Custom Table.csv", index=False)
            except pd.errors.DatabaseError:
                print("Incorrect Query")
        except Warning:
            pass


def custom_query_save_excel(query):
    conn = connect_to_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("USE weather")
            try:
                data = pd.read_sql(query, conn)
                data.to_excel("Custom Table.xlsx", index=False)
            except pd.errors.DatabaseError:
                print("Incorrect Query")
        except Warning:
            pass

def close_connection():
    if conn is not None:
        conn.close()
        
# Execute a SQL query and return the result
def execute_query(query):
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            if query.strip().lower().startswith('select') or query.strip().lower().startswith('show'):
                r = cursor.fetchall()
                conn.commit()
                return r
            else:
                conn.commit()  # For insert queries, commit the transaction
        except mysql.connector.Error as err:
            print("Error:", err)
