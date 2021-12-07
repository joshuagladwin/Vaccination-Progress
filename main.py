from update_table import update_table
from get_data import get_data
from progress_bar import progress_bar
from line_graph import line_graph
from write_tweets import write_tweets
from post_tweets import post_tweets
from push_files_to_web import push_files_to_web


def main():
    """Updates website with latest data from database and sends two tweets about the update."""

    print('Updating Database Table...')
    update_table()
    print('Database Update Complete!')

    print('Getting Data from Database Table...')
    df = get_data()
    print('Data Successfully Retrieved!')

    print('Creating JSON file for Progress Bar...')
    progress_bar(df)
    print('JSON Successfully Created!')

    print('Creating Line Graph...')
    line_graph(df)
    print('Line Graph Successfully Created!')

    print('Transferring Files to vaccinationprogress...')
    push_files_to_web()
    print('Transfer Complete!')

    while True:
        print('Do you also want to tweet this update? (y/n):')
        response = input('> ')
        if response.lower().startswith('y'):
            print('Writing Tweets...')
            tweets = write_tweets(df)

            while True:
                print('WARNING: Have you saved the latest Screenshots for the Tweets? (y/n):')
                response = input('> ')
                if response.lower().startswith('y'):
                    print('Posting Tweets...')
                    post_tweets(tweets)
                    print("Tweets Sent!")
                    break
                elif response.lower().startswith('n'):
                    print('You must save the latest screenshots for the tweets'
                          ' or else the data will not match the images.')
            break

        elif response.lower().startswith('n'):
            print('The Update was not tweeted.')
            break
        else:
            print('Please Enter y or no.')

    print("Update Complete!")


if __name__ == '__main__':
    main()
