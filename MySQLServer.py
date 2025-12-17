#!/usr/bin/python3
"""
Creates the database alx_book_store in MySQL server.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Open connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root"
        )

        cursor = connection.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()
