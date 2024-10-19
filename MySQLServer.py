import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Your MySQL username
            password='NewStrongPassword123!'  # Your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as e:  # Catching specific MySQL connector error
        print(f"Error: {e}")
    
    except Exception as e:  # Optional: Catch any other exceptions
        print(f"An error occurred: {e}")
    
    finally:
        # Ensure the connection is closed if it was opened
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
