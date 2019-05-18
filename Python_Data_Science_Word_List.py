# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# The pattern.en.wordlist module has a number of lists of words (ACADEMIC, PROFANITY, TIME) that can be used to
# filter noise from a document.
# For example, academic words include domain, research, technology, profanity includes words such as shit and hell. 

from pattern.en.wordlist import ACADEMIC
from pattern.vector import Document

d = Document(open("paper.txt").read(), exclude=ACADEMIC)
