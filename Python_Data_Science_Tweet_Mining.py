# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Tweet Mining.
# Assuming we have a collection of hate-tweets organised as a list of (tweet, date)-tuples, it is not difficult
# to group the tweets by day and look at the difference between weekdays and weekends. In general, this difference
# is small, likely because Twitter messages are retweeted across days.
# Here are the top keywords of hate-tweets grouped by day:

daily = {}
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

for tweet, date in hate_tweets:

    # Collect tweets in a dictionary indexed by weekday.

    daily.setdefault(days[date.weekday()],[]).append(tweet)
 
m = Model()

for k, v in daily.items:
    m.append(Document(' '.join(v).lower(), name=k, stemmer=LEMMA))

for document in m:

    print document.name
    print document.keywords(10)
