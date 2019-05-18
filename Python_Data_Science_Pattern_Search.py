# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# pattern.search
# The pattern.search module contains a search algorithm to retrieve sequences of words (called n-grams)
# from tagged text.
# The search pattern NP be RB?+ important than NP means any noun phrase (NP) followed by the verb to be, followed
# by zero or more adverbs (RB, e.g., much, more), followed by the words important than, followed by any noun phrase.
# It will also match "The mobile web will be much less important than mobile apps" and other grammatical variations.

from pattern.en import parsetree
from pattern.search import search
  
s = 'The mobile web is more important than mobile apps.'
s = parsetree(s, relations=True, lemmata=True)

for match in search('NP be RB?+ important than NP', s):
         print match.constituents()[-1], '=>', \
               match.constituents()[0]

# Displays 
# Chunk('mobile apps/NP') => Chunk('The mobile web/NP-SBJ-1')
