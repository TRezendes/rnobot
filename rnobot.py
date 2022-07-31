from urllib.request import urlopen
from config import Config
import pandas as pd
import random
import tweepy
import json

# Tweepy client authorization
client = tweepy.Client(
    consumer_key=Config.API_KEY,
    consumer_secret=Config.API_SECRET,
    access_token=Config.ACCESS_TOKEN,
    access_token_secret=Config.ACCESS_SECRET
)
nytKey = Config.NYT_KEY
wordnikKey = Config.WORDNIK_KEY


# The grunt work
def RNoBot3():
    # Base URL for NYTimes Best Seller List API, unless an offset parameter is set, will return the first 20 results from a list of all NYTimes best sellers sorted alphabetically.
    base_url = 'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=' + nytKey
    with urlopen(base_url) as jfile1:
        jdata1 = json.load(jfile1)
    # From the initial result, capture the total number of results in the list
    num_results = jdata1['num_results']
    # The offset value must be a multiple of 20; divide the total number of results, drop the remainder, and multiply by 20, this is now the maximum value for an offset
    num_results_divisible = (num_results // 20) * 20
    # Offset parameter is between 0 and the evenly divisible approximation of the total number of results
    random_offset = random.randrange(0, num_results_divisible, 20)
    # Concatenate the base URL and the offset parameter
    query_url = base_url + "&offset=" + str(random_offset)
    # Query again, this time with the offset
    with urlopen(query_url) as jfile2:
        jdata2 = json.load(jfile2)
    # Parse JSON results into a DataFrame
    results = pd.json_normalize(jdata2, record_path = ['results'])
    # Each query returns 20 books; choose one at random
    result_num = random.randint(0, 19)
    # Extract the title from the random result. Capitalization is not consistent, so change it to title case
    random_book_result = (results['title'][result_num]).title()
    # Wordnik API query URL to get a single plural noun
    wordnik_url = "https://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&includePartOfSpeech=noun-plural&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=4&maxLength=-1&limit=1&api_key=" + wordnikKey
    # Call the API
    word_df = pd.read_json(wordnik_url)
    # Extract the word from the result
    plural_noun = word_df['word'][0]
    tweet = f'There are no {plural_noun} in "{random_book_result}".'
    print(tweet)
    return tweet

# And…tweet it!
client.create_tweet(text=RNoBot3())