# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Semantic network.
# The pattern.graph module has a Graph object from which we can start.
# Perception Database.
# We don’t want to define all the relations by hand; the perception database is included in Pattern as a CSV-?le
# that we can easily import:
# In order to compare concepts, we will use a combination of graph theoretic methods: spreading activation, taxonomies, 
# subgraph partitioning, betweenness centrality and shortest path ?nding.

from pattern.graph import Graph 
from pattern.db import CSV 
  
g = Graph() 
  
data = 'pattern/graph/commonsense/commonsense.csv'
data = CSV.load(data) 

for concept1, relation, concept2, context, weight in data: 

    g.add_edge( 
        concept1, 
        concept2, 
          type = relation, 
        weight = min(int(weight) * 0.1, 1.0)) 