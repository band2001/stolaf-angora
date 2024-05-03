import sqlite3 as sql

def create_QA_table(database = 'question_answer.db'):
    '''
    This function is used to create a QA table in the desired database. If a database does not already exist, the database is created.
    
    :param database: the path to the database to create the table in (or create)

    :return None
    '''
    try:
        with sql.connect(database) as con:
            con.execute("CREATE TABLE QA (instruction TEXT, response TEXT, link TEXT)")
    except:
        print("Table exists")
    finally:
        con.close()