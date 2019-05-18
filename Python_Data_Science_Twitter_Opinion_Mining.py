# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Twitter opinion Mining.

from pattern.web import Twitter, plaintext
from pattern.db  import Datasheet
from pattern.nl  import sentiment as sentiment_nl
from pattern.fr  import sentiment as sentiment_fr
    
csv = Datasheet()

for politician, party in (("bart de wever", "NV-A"), ("elio di rupo", "PS")):

    for tweet in Twitter().search(politician):

        if tweet.language in ("nl", "fr"):
            s = plaintext(tweet.description) 

            if tweet.language == "nl":
                w = sentiment_nl(s)

            if tweet.language == "fr":
                w = sentiment_fr(s)    

            csv.append([politician, party, tweet.date, s, w])