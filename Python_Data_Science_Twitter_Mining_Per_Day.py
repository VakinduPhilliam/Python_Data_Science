# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Twitter Opinion Mining, results per day. 
# To do this, we need to "bin" the tweets of a politician per day (or per week, month, year) and calculate the 
# average sentiment of that day:

from pattern.db  import Datasheet, date, avg
from collections import defaultdict
 
bins = defaultdict(lambda: defaultdict(list))

for politician, party, date, score in Datasheet.load("data.csv"):

    d = date(row[8])
    d = (d.year, d.month, d.day)

    bins[politician][d].append(float(score))

for politician in bins:

    for day in politician:
        bins[politician][day] = avg(bins[politician][day])
