from ftplib import FTP
import pandas as pd

credentials = pd.read_json('ftp_credentials.json', typ='series', orient='records')
host = credentials['host']
user = credentials['user']
password = credentials['password']


def push_files_to_web():
    """Pushs the files for the Progress Bar (vaccinationdata.json)
    and the Line Graph (graph.html) to the website."""

    ftp = FTP(host, user, password)
    ftp.cwd('public_html')
    ftp.retrlines('LIST')

    with open('vaccinationdata.json', 'rb') as f:
        ftp.storbinary('STOR vaccinationdata.json', f)

    with open('graph.html', 'rb') as f:
        ftp.storbinary('STOR graph.html', f)

    ftp.retrlines('LIST')
    ftp.quit()
