import tweepy
import pandas as pd

credentials = pd.read_json('twitter_credentials.json', typ='series', orient='records')
consumer_key = credentials['API Key']
consumer_secret = credentials['API Key Secret']
access_token = credentials['Access Token']
access_token_secret = credentials['Access Token Secret']
user_id = credentials['User ID']
screen_name = credentials['Screen Name']


def post_tweets(tweets):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # Retrieve screenshots
    first_tweet_image = "Twitter Images/Progress Bar.png"
    second_tweet_image = "Twitter Images/Line Graph.png"

    # Post 1st tweet
    api.update_status_with_media(status=tweets[0], filename=first_tweet_image)

    # Retrieve 1st Tweet as Posted
    first_tweet = api.user_timeline(user_id=user_id, screen_name=screen_name,
                                    include_rts=False)[0]
    # Access 1st tweet_id
    first_tweet_id = first_tweet.id

    # Post 2nd Tweet in reply to 1st Tweet
    api.update_status_with_media(status=tweets[1], filename=second_tweet_image,
                                 in_reply_to_status_id=first_tweet_id)


if __name__ == '__main__':

    tweets = ['TEST TWEET', 'BEEP BOOP']
    post_tweets(tweets)
