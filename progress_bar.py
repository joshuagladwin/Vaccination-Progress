from datetime import datetime
from get_data import get_data


def progress_bar(df):
    """Creates JSON with the latest vaccination data for the website to display."""

    latest_data = df.iloc[-1].copy()
    date = df.index[-1]
    latest_data['date'] = date.strftime("%d.%m.%Y")
    last_updated = datetime.now()
    last_updated = last_updated.strftime("%Y-%m-%d %H:%M:%S")
    latest_data['last_updated'] = last_updated

    latest_data.to_json('vaccinationdata.json')


if __name__ == '__main__':

    df = get_data()

    progress_bar(df)
