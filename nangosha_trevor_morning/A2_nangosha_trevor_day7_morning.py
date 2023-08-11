"""
Show a context manager for file handling that automatically opens and closes a file.
"""

class contextmanager:
     def __init__(self, filename, mode):
         self.filename = filename
         self.mode = mode
         self.file = None

     def __enter__(self):
         self.file = open(self.filename, self.mode)
         return self.file

     def __exit__(self, exc_type, exc_val, exc_tb):
         if self.file:
             self.file.close()


filename = "sample.txt"
 mode = "r"

 with contextmanager(filename, mode) as file:
     file.read()
     print("All Done")


"""
 Shows a context manager for managing a database connection.
"""
import sqlite3


class databasemanager:
    def __init__(self, database):
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)  # connecting to the database
        return self.connection
        print("Connection Made")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


# Example
database = "sample.db"

with databasemanager(database) as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

    # Inserting a row
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("John Snow",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Night Walker",))

    # Fetching all rows
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


"""
Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.
"""

import threading
import multiprocessing
import time

def function(name, duration):
    print(f"Thread/Process {name} started.")
    time.sleep(duration)
    print(f"Thread/Process {name} finished.")

# Multithreading example
def multithreadings():
    threads = []

    # Create and start multiple threads
    for i in range(5):
        thread = threading.Thread(target=function, args=(f"Thread-{i}", i))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("Multithreading finished.")

# Multiprocessing
def multiprocessings():
    processes = []

    # Create and start multiple processes
    for p in range(5):
        process = multiprocessing.Process(target=function, args=(f"Process-{p}",p))
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()


    print("Multiprocessing  finished.")

# Run the examples
print("Running multithreading ...")
multithreadings()

print()

print("Running multiprocessing ...")
multiprocessings()
