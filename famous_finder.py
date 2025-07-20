import wikipedia
import sqlite3

def connect_execute_to_db(sql_req):
    con = sqlite3.connect("test_snel.db")
    cur = con.cursor()
    cur.execute(sql_req)
    con.commit()
    con.close()

def create_db():
    con = sqlite3.connect("test_snel.db")
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS famous_people(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(255),
                        summary TEXT);''')
    con.commit()
    con.close()
    
