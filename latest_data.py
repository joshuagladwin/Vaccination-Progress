import pandas as pd
import numpy as np

POPULATION_GERMANY = 83_129_285


def latest_data():
    """Returns the latest data from the German Corona Impfdashboard"""

    df = pd.read_csv('https://impfdashboard.de/static/data/germany_vaccinations_timeseries_v2.tsv', sep='\t')

    columns = ['date', 'dosen_erst_differenz_zum_vortag', 'dosen_zweit_differenz_zum_vortag',
               'dosen_dritt_differenz_zum_vortag', 'dosen_differenz_zum_vortag',
               'personen_erst_kumulativ', 'personen_voll_kumulativ', 'dosen_dritt_kumulativ']

    df = df.loc[:, columns]
    df.rename(columns={'date': 'date', 'dosen_erst_differenz_zum_vortag': 'yesterday_1st_doses',
                       'dosen_zweit_differenz_zum_vortag': 'yesterday_2nd_doses',
                       'dosen_dritt_differenz_zum_vortag': 'yesterday_booster_doses',
                       'dosen_differenz_zum_vortag': 'yesterday_total_doses',
                       'personen_erst_kumulativ': 'total_1st_vaccinated',
                       'personen_voll_kumulativ': 'total_2nd_vaccinated',
                       'dosen_dritt_kumulativ': 'total_booster_doses'},
              inplace=True)
    df.dropna(subset=['yesterday_total_doses'], inplace=True)

    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    df['pc_1st_vaccinated'] = round((df.total_1st_vaccinated / POPULATION_GERMANY) * 100, 2)
    df['pc_2nd_vaccinated'] = round((df.total_2nd_vaccinated / POPULATION_GERMANY) * 100, 2)
    df['pc_booster_vaccinated'] = round((df.total_booster_doses / POPULATION_GERMANY) * 100, 2)

    df['seven_d_avg_partial'] = round(df['yesterday_1st_doses'].rolling(window=7).mean())
    df['seven_d_avg_full'] = round(df['yesterday_2nd_doses'].rolling(window=7).mean())
    df['seven_d_avg_booster'] = round(df['yesterday_booster_doses'].rolling(window=7).mean())
    df['seven_d_avg_total'] = round(df['yesterday_total_doses'].rolling(window=7).mean())
    df.replace(np.nan, 0, inplace=True)

    return df


if __name__ == '__main__':

    df = latest_data()
    print(df)
