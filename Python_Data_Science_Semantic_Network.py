# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Semantic network.
# The pattern.graph module has a Graph object from which we can start:

from pattern.graph import Graph
 
g = Graph() 
g.add_edge('doll', 'toy', type='is-a') # doll is-a toy 
g.add_edge('silent', 'doll', type='is-property-of') 
g.add_edge('doll', 'girl', type='is-related-to') 
 
node = g['doll'] 

print node.id
print node.links 