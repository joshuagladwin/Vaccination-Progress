#!/usr/bin/python

import psycopg2

from connect_db import connect_db
from latest_data import latest_data


def update_table():
    """Takes the latest data and upserts to PostgreSQL database."""

    df = latest_data()

    conn = connect_db()

    tuples = [tuple(x) for x in df.to_numpy()]

    query = """
            INSERT INTO vaccination_data (date, yesterday_1st_doses, yesterday_2nd_doses, yesterday_booster_doses, 
            yesterday_total_doses, total_1st_vaccinated, total_2nd_vaccinated, total_booster_doses, pc_1st_vaccinated, 
            pc_2nd_vaccinated, pc_booster_vaccinated, seven_d_avg_partial, seven_d_avg_full, seven_d_avg_booster, 
            seven_d_avg_total)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (date) DO UPDATE SET 
            (yesterday_1st_doses, yesterday_2nd_doses, yesterday_booster_doses, yesterday_total_doses, 
            total_1st_vaccinated, total_2nd_vaccinated, total_booster_doses, pc_1st_vaccinated, pc_2nd_vaccinated,
            pc_booster_vaccinated, seven_d_avg_partial, seven_d_avg_full, seven_d_avg_booster, seven_d_avg_total)
            = (EXCLUDED.yesterday_1st_doses, EXCLUDED.yesterday_2nd_doses, EXCLUDED.yesterday_booster_doses, 
            EXCLUDED.yesterday_total_doses, EXCLUDED.total_1st_vaccinated, EXCLUDED.total_2nd_vaccinated, 
            EXCLUDED.total_booster_doses, EXCLUDED.pc_1st_vaccinated, EXCLUDED.pc_2nd_vaccinated, 
            EXCLUDED.pc_booster_vaccinated, EXCLUDED.seven_d_avg_partial, EXCLUDED.seven_d_avg_full, 
            EXCLUDED.seven_d_avg_booster, EXCLUDED.seven_d_avg_total)
            """ # TODO: Parameterize Query
    
    cursor = conn.cursor()
    try:
        cursor.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()


if __name__ == '__main__':

    update_table()
