import json
import pandas as pd
import mysql.connector
from mysql.connector import Error

from pymongo import MongoClient
def fetch_data(payload):
    type = payload["type"]
    if(type == "mongodb"):
        getDataFromMongoDB(payload)
    elif type == "mysql":
        getDataFromMySQLDB(payload)

def getDataFromMongoDB(payload):

    username = payload.get("username")
    password = payload.get("password")
    cluster_url = payload.get("cluster_url")
    database_name = payload.get("database_name")
    collection = payload.get("collection")

    connection_string = "mongodb+srv://"+ username+":"+password+"@"+cluster_url

    client = MongoClient(connection_string)

    db = client[database_name]
    collection = db[collection]
    documents = collection.find()

    df = pd.DataFrame(list(documents))
    client.close()
    return df

def getDataFromMySQLDB(payload):

    host =  payload.get("host")
    database =  payload.get("database")
    user =  payload.get("user")
    password =  payload.get("password")
    table_name =  payload.get("table_name")

    connection = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        print(f"Connected to MySQL database '{database}'")

        # Use pandas to execute the query and fetch data into a DataFrame
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, connection)
        return df
    except Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
