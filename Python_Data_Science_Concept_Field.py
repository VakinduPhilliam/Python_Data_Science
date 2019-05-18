# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Concept field.
# Such a collection is also known as a semantic field (Brinton, 2000), a set of words that share a common semantic
# property, related to hyponymy but more loosely de?ned. So we need a field() function that returns a list with when
# given 'animal' and sort it by creepiness.
# Retrieving such a list is not hard to accomplish using a combination of Graph and Node methods.
# The Node.flatten() method returns a list containing the given node (depth=0), any nodes connected to it (depth=1),
# and so on. We can supply a filter function to restrict which edges are traversed. In our case, we only follow is-a
# relations. The Graph.fringe() method returns a list of nodes with a single edge (depth=0), any nodes connected to
# these nodes (depth=1), and so on. A combination of the two methods yields the 'outer rim' of a node's taxonomy, which
# is a good approximation of our semantic field:

def field(node, depth=3, fringe=2): 

    def traversable(node, edge): 
        return edge.node2 == node and edge.type == 'is-a'

    g = node.graph.copy(nodes=node.flatten(depth, traversable)) 
    g = g.fringe(depth=fringe) 
    g = [node.graph[n.id] for n in g if n != node] 

    return g
