#!/usr/bin/python

import pandas as pd
import psycopg2
import numpy as np

from connect_db import connect_db


def get_data():

    table = 'vaccination_data'

    conn = connect_db()
    # SQL query to execute
    query = """SELECT column_name
            FROM information_schema.columns 
            WHERE table_name = 'vaccination_data';""" # TODO: Parameterize Query
    cursor = conn.cursor()
    try:
        cursor.execute(query, table)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    column_tuples = cursor.fetchall()

    columns = []

    for t in column_tuples:
        columns.append(t[0])

    query = """SELECT * FROM vaccination_data;"""  # TODO: Parameterize Query

    try:
        cursor.execute(query, table)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    data = cursor.fetchall()

    cursor.close()

    df = pd.DataFrame(data, columns=columns)
    df.set_index('date', inplace=True)
    df.sort_index(inplace=True)



    return df


if __name__ == '__main__':

    df = get_data()

    print(df)
