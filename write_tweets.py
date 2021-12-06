from get_data import get_data
from datetime import timedelta


def write_tweets(df):

    latest_data = df.iloc[-1]
    date = latest_data.name

    last_week = date - timedelta(7)
    last_week_data = df.loc[last_week]

    difference = latest_data - last_week_data
    difference = difference.loc[difference.index.str.startswith("yesterday")]
    difference = difference.rename(lambda x: "difference" + x[9:])

    for i, d in enumerate(difference):
        if d < 0:
            trend = "DOWN \N{Downwards Black Arrow}"
        elif d > 0:
            trend = "UP \N{Upwards Black Arrow}"
        else:
            trend = "impossibly exactly the same?"
        difference[i] = f"{trend} {abs(int(d)):,}"

    difference['date'] = last_week.strftime("%d.%m.%Y")
    difference['day'] = last_week.strftime("%A")

    tweets = [
    f"""VACCINATION PROGRESS BAR UPDATE ({date.strftime("%d.%m.%Y")}):

Partial Vaccinations: {int(latest_data['yesterday_1st_doses']):,}
Total Partial: {int(latest_data['total_1st_vaccinated']):,}
Minimum %Vaccinated: {latest_data['pc_1st_vaccinated']}%

Full Vaccinations: {int(latest_data['yesterday_2nd_doses']):,}
Total Full: {int(latest_data['total_2nd_vaccinated']):,}
Minimum %Vaccinated: {latest_data['pc_2nd_vaccinated']}%

Plus {int(latest_data['yesterday_booster_doses']):,} Booster Vaccinations

vaccinationprogress.joshuagladwin.de""",

    f"""COMPARED TO LAST {difference.day.upper()} ({difference.date}):

Partial Vaccinations are {difference.difference_1st_doses} doses.
Full Vaccinations are {difference.difference_2nd_doses} doses.
Booster Vaccinations are {difference.difference_booster_doses} doses.
Overall, the total number of vaccinations is {difference.difference_total_doses} doses.

vaccinationprogress.joshuagladwin.de
"""
    ]

    for tweet in tweets:
        print(tweet, end='\n\n\n')

    return tweets

if __name__ == '__main__':

    df = get_data()
    write_tweets(df)
