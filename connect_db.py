import sys
from config import config
import psycopg2


def connect_db():
    """Connects to the PostgreSQL database server and returns the connection."""

    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        params_dic = config()
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")

    return conn


if __name__ == '__main__':
    connect_db()
