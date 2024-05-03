import sqlite3 as sql
import csv

def write_from_data(data):
    '''
    This is used to write rows from a csv (data) to the database.

    :param: data: what has been read in from a csv file
    :return: None
    '''

    try:
        with sql.connect('question_answer.db') as con:
            cur = con.cursor()
            for row in data:
                cur.execute("INSERT INTO QA VALUES (?,?,?)",(row[0],row[1],row[2]))
            con.commit()
    except Exception as error:
        print("There was an error adding the data")
        print(error)
    finally:
        con.close()


def write_from_csv(csvpath = "question_answer.csv"):
    '''
    This is used to write a csv to the database

    :param: csvpath: the path to the CSV
    :return: None
    '''
    with open(csvpath) as csvfile:
        datareader = csv.reader(csvfile)
        write_from_data(datareader)