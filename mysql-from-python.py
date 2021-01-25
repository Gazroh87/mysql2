import os
import datetime
import pymysql

# Get username from GitPod workspace
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        # sql = "SELECT * FROM Genre;"
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 13:12:45"),
                ("Fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
        # result = cursor.fetchall()
        # for row in cursor:
            # print(row)
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
