# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Web mining.
# A simple web mining technique.

from pattern.web    import Newsfeed, plaintext
from pattern.db     import date
from pattern.vector import Model, Document, LEMMA
  
news, url = {}, 'http://news.google.com/news?output=rss'

for story in Newsfeed().search(url, cached=False):

    d = str(date(story.date, format='%Y-%m-%d'))
    s = plaintext(story.description)

    # Each key in the news dictionary is a date: news is grouped per day.
    # Each value is a dictionary of id => story items.
    # We use hash(story.description) as a unique id to avoid duplicate content.

    news.setdefault(d, {})[hash(s)] = s

# Your code will probably have some preprocessing steps to save and load the mined news updates.

m = Model()

for date, stories in news.items():
    s = stories.values()
    s = ' '.join(s).lower()

    # Each day of news is a single document.
    # By adding all documents to a model we can calculate tf-idf.

    m.append(Document(s, stemmer=LEMMA, exclude=['news', 'day'], name=date))
  
for document in m:

    print document.name
    print document.keywords(top=10)
