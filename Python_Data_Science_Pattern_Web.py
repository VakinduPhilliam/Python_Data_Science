# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# pattern.web
# The pattern.web module is a web toolkit that contains API's (Google, Gmail, Bing, Twitter, Facebook, Wikipedia,
# Wiktionary, DBPedia, Flickr, ...), a robust HTML DOM parser and a web crawler.

from pattern.web import Twitter, plaintext

twitter = Twitter(language='en') 
    for tweet in twitter.search('"more important than"', cached=False):
       print plaintext(tweet.text)

# Displays
# 'The mobile web is more important than mobile apps.'
# 'Start slowly, direction is more important than speed.'
# 'Imagination is more important than knowledge. - Albert Einstein'
# ...
