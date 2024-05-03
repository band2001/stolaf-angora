import sqlite3 as sql
import csv

def read_csv(path = "question_answer.csv"):
    '''
    This funciton is used to read in our data from a CSV file and return a list with the data placed into dictionaries representing each question/answer pair.

    :param path - the path to the question_answer.csv, the default file path is included
    :return list - a list containing dictionaries; each dictionary represents a question/answer pair where there is an 'instruction', a 'response', and a 'link'.
    '''

    data = []

    with open(path) as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            data.append({"instruction": row[0], "response": row[1], "link": row[2]})
    
    data = data[1:]

    return data

def read_database(database = "question_answer.db"):
    '''
    This function is used to read in data from the database with a QA table and return a list with the data placed into dictionaries representing each question/answer pair.

    :param database - the path to the question_answer.db, the default file path is included
    :return list - a list containing dictionaries; each dictionary represents a question/answer pair where there is an 'instruction', a 'response', and a 'link'.
    '''

    data = []

    con = sql.connect(database)
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * FROM QA")

    rows = cur.fetchall()
    for row in rows:
        data.append({"instruction": row["instruction"], "response": row["response"], "link": row["link"]})
    
    return data[1:]