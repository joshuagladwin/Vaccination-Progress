# Vaccination Progress

These Python scripts update the data used on the [Vaccination Progress](https://vaccinationprogress.joshuagladwin.de/) site, which reports the progress of the COVID-19 vaccination rollout in Germany. 

The file `main.py` runs through the following steps:

1. Retrieve the latest data release from the German [Impfdashboard](https://impfdashboard.de/), processing the data and updating the PostgreSQL database.
2. Queries the database and returns the data in a Pandas dataframe.
3. Produces a JSON file to be used to generate the Progress Bars on the site.

<img alt="Progress Bars showing the percentage of people vaccinated against COVID-19 in Germany" height="50%" src="Images/Progress Bar.png" width="50%"/>

4. Produces a Line Graph, using the [Plotly Python library](https://plotly.com/python/).

<img alt="Line graph showing the daily vaccinations since the start of Germany&#39;s vaccination rollout." height="50%" src="Images/Line Graph.png" width="50%"/>

5. The JSON and the Line Graph are pushed to the website.
6. (After screenshots of the site are taken manually,) writes two tweets describing the progress bar and line graph.
7. Posts the tweets and accompanying images to Twitter.

## TODO List:
* [ ] Find a way to save the images for the tweets programmatically, without needing to take the site screenshots manually.
* [ ] Explore different implementations of the Progress Bars and Line Graphs.
  * [ ] Create Progress Bars in Python. (Using what libraries?)
  * [x] ~~Create Line Graphs using the Plotly JS library.~~
  * [ ] What pros/cons are there to using Python-built graphs over JS-built?


## Project Requirements

### Python 3.9

| Package | Version |
|---------|---------|
| certifi|2021.10.8 |
| charset-normalizer | 2.0.9 |
| idna | 3.3 |
| numpy | 1.21.4 |
| oauthlib | 3.1.1 |
| pandas | 1.3.4 |
| plotly | 5.4.0 |
| psycopg2 | 2.9.2 |
| python-dateutil | 2.8.2 |
| pytz | 2021.3 |
| requests | 2.26.0 |
| requests-oauthlib | 1.3.0 | 
| six | 1.16.0 |
| tenacity | 8.0.1 |
| tweepy | 4.4.0 |
| urllib3 | 1.26.7 |