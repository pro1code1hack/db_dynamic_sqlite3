
import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

# DB sql query interaction 
# cur.execute("CREATE TABLE movie(title, year, score)")

# # SELECT

# res = cur.execute("SELECT name FROM sqlite_master")
# row1 = res.fetchone()
# print(row1)     # ('movie',)

# res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# print(res.fetchone())      # <sqlite3.Cursor object at 0x78cdd58bf240>


# INSERT

# %s        --> correct approach
# f{}       --> SQL INJECTION

# movie = "DROP * FROM TABLE movie;"

# cur.execute(f"""
#     INSERT INTO {movie} VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)


# INSERT
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()        # if it's possible --> insert data (if not --> відкатується)


# FETCH ALL

# res = cur.execute("SELECT title, year, score FROM movie")
# rows = res.fetchall()

# print(rows)

"""
ONE TRANSACTION

# 1 - SELECT 
# 2 - INSERT
# 3 - UPDATE
"""


# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]

# cur.executemany("INSERT INTO movie VALUES(?, ?, ?,)", data)
# con.commit()  # Remember to commit the transaction after executing INSERT.


# for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
#     print(row)


# UPDATE 
cur.execute("UPDATE movie SET title = ?, year = ?, score = ?", ("new_title", 2012, 12.0))
con.commit()

# DELETE
cur.execute("DELETE FROM movie WHERE title = ?", "new_title")
con.commit()

# rows = res.fetchall()


# CRUD operations



"""

Operation with SQLite


1) class DB:
    def connect()                       --> done
    def @property get_cusror()          --> done
    def @property get_connection_obj()
    def get_data()                      --> done
    def update_data()
    def insert_data()                   --> done
    def delete_data()

2) class Cars/Customers/Orders
    def __init__
    def __dict__()
    def serialise()
    def print_data()
    def insert_data()
    ....

3) Test joins in sqlalchemy
"""