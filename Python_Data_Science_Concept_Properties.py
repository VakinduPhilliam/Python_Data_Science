# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Concept properties.
# In the semantic network, some concepts (typically adjectives) are properties of other concepts. They describe 
# what something looks or feels like: romantic IS-PROPERTY-OF France, fast IS-PROPERTY-OF rocket, dark
# IS-PROPERTY-OF evil, evil IS-PROPERTY-OF Darth Vader, and so on. If we can find the properties (e.g., romantic, 
# fast, dark, evil) that define each concept we can construct an algorithm to compare them.
# The feature approach is our model's thinking style.

# First, we store all the left-hand concepts that occur in IS-PROPERTY-OF relations in a PROPERTIES dictionary.
# Dictionaries in Python are faster for lookup than lists:

PROPERTIES = [e.node1.id for e in g.edges if e.type == 'is-property-of'] 
PROPERTIES = dict.fromkeys(PROPERTIES, True) 

# We can then implement a properties() function that, given a concept, extracts its latent properties from the
# concept halo. 
# Note how we sort the results by betweenness centrality (Brandes, 2001) using Node.centrality (= a value between
# 0.0 and 1.0).
# This means that properties more central in the halo will appear first in the list:

cache = {} # Cache results for faster reuse.
  
def properties(node): 

    if node.id in cache: 
        return cache[node.id] 

    g = node.graph.copy(nodes=halo(node)) 

    p = (n for n in g.nodes if n.id in PROPERTIES) 
    p = reversed(sorted(p, key=lambda n: n.centrality)) 
    p = [node.graph[n.id] for n in p] 

    cache[node.id] = p 

    return p 
