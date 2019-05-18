# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Novelty assessment.
# One approach to measure the novelty of the model's suggestions is to count the number of web pages that mention
# each suggestion.
# It follows that suggestions that are less often mentioned are more novel.

from pattern.web import Google 
 
def novelty(ideas=[]): 

    candidates = [Google().search(idea) for idea in ideas] 
    candidates = sorted(candidates, key=lambda results: results.total) 
    candidates = [(results.query, results.total) for results in candidates] 

    return candidates 
 
 print novelty(['Brussels stag', 'Brussels frog', 'Brussels toad']) 
