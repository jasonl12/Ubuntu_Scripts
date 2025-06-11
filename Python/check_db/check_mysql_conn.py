import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables from .env file
load_dotenv()

# Access environment variables
db_host = os.getenv("DATABASE_HOST")
db_user = os.getenv("DATABASE_USER")
db_pass = os.getenv("DATABASE_PASS")
db_name = os.getenv("DATABASE_NAME")


try:
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        database=db_name,
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print(f"Test query successful: {result}")

    cursor.execute("SELECT version();")
    result = cursor.fetchone()
    print(result[0])
    mydb.close()

except mysql.connector.Error as err:
    print(f"Error '{err}'")
