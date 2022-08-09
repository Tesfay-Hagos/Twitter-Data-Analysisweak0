class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print(self.df.head())
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        column=df.columns
        for col in column:
            df=df[df[col] !=col]
        return df
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        df = df.drop_duplicates(inplace=True)
        
        return df
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        
        df['created_at'] = pd.to_datetime(df['created_at'],format='%y%m%d')
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc. to numbers
        """
        df[['polarity',"retweet_count",'favorite_count','subjectivity']] = df['polarity'].apply(pd.to_numeric)
        
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        column = df.columns
        for col in column:
            df[df[col].map(lambda x: x.isascii())]


        
        return df