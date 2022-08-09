
import json
import pandas as pd
from textblob import TextBlob


def read_json(json_file: str) -> list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file

    Returns
    -------
    length of the json file and a list of json
    """

    tweets_data = []
    for tweets in open(json_file, 'r'):
        tweets_data.append(json.loads(tweets))

    return len(tweets_data), tweets_data


class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe

    Return
    ------
    dataframe
    """

    def __init__(self, tweets_list):

        self.tweets_list = tweets_list

    # an example function
    def find_statuses_count(self) -> list:
        statuses_count = statuses_count = [x['user']['statuses_count'] for x in self.tweets_list]
        return statuses_count

    def find_full_text(self) -> list:
        text = [x['full_text'] for x in self.tweets_list]
        return text

    def find_sentiments(self, text) -> list:
        text = self.find_full_text()
        polarity = []
        subjectivity = []
        for t in text:
            sentiment = TextBlob(t).sentiment
            polarity.append(sentiment.polarity)
            subjectivity.append(sentiment.subjectivity)
        return polarity, subjectivity

    def find_created_time(self) -> list:
        created_at = [x['user']['created_at'] for x in self.tweets_list]
        return created_at

    def find_source(self) -> list:
        source = [x['source'] for x in self.tweets_list]

        return source

    def find_screen_name(self) -> list:
        screen_name = [x['user']['screen_name'] for x in self.tweets_list]
        return screen_name

    def find_followers_count(self) -> list:
        followers_count = [x['user']['followers_count'] for x in self.tweets_list]
        return followers_count

    def find_friends_count(self) -> list:
        friends_count = [x['user']['friends_count'] for x in self.tweets_list]
        return friends_count

    def is_sensitive(self) -> list:
        is_sensitive = []
        try:
            is_sensitive = [x['possibly_sensitive'] for x in self.tweets_list]
        except KeyError:
            is_sensitive.append(None)

        return is_sensitive

    def find_favourite_count(self) -> list:
        favourite_count = [x['user']['favourites_count'] for x in self.tweets_list]
        return favourite_count

    def find_retweet_count(self) -> list:
        retweet_count = [x['retweet_count'] for x in self.tweets_list]
        return retweet_count

    def find_hashtags(self) -> list:
        hashtags=[tweet['entities']['hashtags'] for tweet in self.tweets_list]
        return hashtags
    def find_mentions(self) -> list:
        mentions = [x['entities']['user_mentions']for x in self.tweets_list]
        return mentions

    def find_location(self) -> list:
        try:
            location = [x['user']['location'] for x in self.tweets_list]
        except TypeError:
            location = 'None'

        return location

    def find_lang(self) -> list:
        lang = [x['lang'] for x in self.tweets_list]
        return lang


    def get_tweet_df(self, save=False) -> pd.DataFrame:
        """required column to be generated you should be creative and add more features"""

        columns = ['created_at', 'source', 'original_text', 'polarity', 'subjectivity', 'lang', 'favorite_count',
                   'retweet_count',
                   'original_author', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags',
                   'user_mentions', 'place']

        created_at = self.find_created_time()
        print(f"createdat:{type(created_at)}")
        source = self.find_source()
        print(f"source:{type(source)}")
        text = self.find_full_text()
        print(f"text:{type(text)}")
        polarity, subjectivity = self.find_sentiments(text)
        print(f"polarity:{type(polarity)},subjectivity:{type(subjectivity)}")
        lang = self.find_lang()
        print(f"lang:{type(lang)}")
        fav_count = self.find_favourite_count()
        print(f"fav_count:{type(fav_count)}")
        retweet_count = self.find_retweet_count()
        print(f"retweat_count:{type(retweet_count)}")
        screen_name = self.find_screen_name()
        print(f"screen_name:{type(screen_name)}")
        follower_count = self.find_followers_count()
        print(f"follower_count:{type(follower_count)}")
        friends_count = self.find_friends_count()
        print(f"friends_count:{type(friends_count)}")
        sensitivity = self.is_sensitive()
        print(f"sensitvity:{type(sensitivity)}")
        hashtags = self.find_hashtags()
        print(f"Hashtags:{type(hashtags)}")
        mentions = self.find_mentions()
        print(f"mentions:{type(mentions)}")
        location = self.find_location()
        print(f"location:{type(location)}")
        data = zip(created_at, source, text, polarity, subjectivity, lang, fav_count, retweet_count, screen_name,
                   follower_count, friends_count, sensitivity, hashtags, mentions, location)
        df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')

        return df


if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
    columns = ['created_at', 'source', 'original_text', 'clean_text', 'sentiment', 'polarity', 'subjectivity', 'lang',
               'favorite_count', 'retweet_count',
               'original_author', 'screen_count', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags',
               'user_mentions', 'place', 'place_coord_boundaries']
    _, tweet_list = read_json("data/africa_twitter_data.json")
    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df()
    print(tweet_df.head())


    # use all defined functions to generate a dataframe with the specified columns above