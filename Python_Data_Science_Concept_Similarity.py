# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Concept similarity.
# Similarity between two concepts is measured as the distance between their properties.
# The similarity() function retrieves the k most central properties in each concept’s halo. It then measures
# the length of the shortest path (Dijkstra, 1959) connecting each two properties, preferring to traverse
# IS-PROPERTY-OF relations over other relations. This yields a higher value for more similar concepts
# (lower value for distinct concepts):

def similarity(node1, node2, k=3): 

    g = node1.graph 
    h = lambda id1, id2: 1 - int(g.edge(id1, id2).type == 'is-property-of') 
    w = 0.0

    for p1 in properties(node1)[:k]: 

        for p2 in properties(node2)[:k]: 
            p = g.shortest_path(p1, p2, heuristic=h) 
            w += 1.0 / (p is None and 1e10 or len(p)) 

    return w / k 

# We can then use similarity() to implement a one-versus-all search:

def nearest_neighbors(node, candidates=[], k=3): 

    w = lambda n: similarity(node, n, k) 

    return sorted(candidates, key=w, reverse=True) 

# "What are creepy-looking animals?" For a given concept (e.g., creepy) and a list of candidates (e.g., animals),
# nearest_neighbors() yields the candidates with the highest similarity (the creepiest animals).
# In this particular example, it will suggest animals such as octopus, bat, owl, tick, spider, crow, ...
# No fluffy bunnies or frolicking ponies there!

print nearest_neighbors(g['creepy'], field(g['animal'])) 
