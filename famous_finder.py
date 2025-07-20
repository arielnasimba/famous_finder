import wikipedia
import sqlite3

def connect_execute_to_db(sql_req, params=()):
    # connect to database
    con = sqlite3.connect("test_snel.db")
    cur = con.cursor()
    
    # execute sql request
    cur.execute(sql_req, params)
    con.commit()
    print(cur.execute("SELECT COUNT(*) FROM famous_people;").fetchall())
    print(cur.execute("SELECT ID as 'ID', name 'Name' FROM famous_people;").fetchall())
    con.close()

def create_db():
    # create database
    sql_req = '''CREATE TABLE IF NOT EXISTS famous_people(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(255),
                        summary TEXT);'''
    connect_execute_to_db(sql_req)
    
def insert_to_db(famous_name, famous_summary):
    # insert into database
    sql_req = "INSERT INTO famous_people(name, summary) VALUES (?, ?);"
    connect_execute_to_db(sql_req, (famous_name, famous_summary))

def famous_people_asking():
    name = input("Can you give me the name of a famous person?\n>>> ").strip()

    try:
        # Check search results
        search_results = wikipedia.search(name)
        if not search_results:
            print("Sorry there are no results for that.")
            return
        #Get first result
        first_match = search_results[0]

        if first_match.lower() != name.lower():
            print("I don’t know this person.")
            if wikipedia.suggest(name):
                print(f"Did you mean: {wikipedia.suggest(name)}?")
            else:
                print("No suggestion found.")
            return

        # If exact match, continue
        summary = wikipedia.summary(name)
        insert_to_db(name, summary)

    except wikipedia.exceptions.DisambiguationError as e:
        print("Multiple results found. Try one of these:")
        print(e.options[:3])
    except wikipedia.exceptions.PageError:
        print("I don’t know this person.")
        
        
# Run program
create_db()
famous_people_asking()