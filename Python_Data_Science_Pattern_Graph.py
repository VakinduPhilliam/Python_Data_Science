# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# pattern.graph
# The pattern.graph module provides a graph data structure that represents relations between nodes (e.g., terms, concepts).
# Graphs can be exported as HTML <canvas> animations (demo). In the example below, more central nodes
#  (= more incoming traffic) are colored in blue.

from pattern.web    import Bing, plaintext
from pattern.en     import parsetree
from pattern.search import search
from pattern.graph  import Graph

g = Graph()

    for i in range(10):

        for result in Bing().search('"more important than"', start=i+1, count=50):

            s = r.text.lower() 
            s = plaintext(s)
            s = parsetree(s)
            p = '{NP} (VP) more important than {NP}'

            for m in search(p, s):
                x = m.group(1).string # NP left
                y = m.group(2).string # NP right

                if x not in g:
                    g.add_node(x)

                if y not in g:
                    g.add_node(y)

                g.add_edge(g[x], g[y], stroke=(0,0,0,0.75)) # R,G,B,A
     
    g = g.split()[0] # Largest subgraph.
     
    for n in g.sorted()[:40]: # Sort by Node.weight.
        n.fill = (0, 0.5, 1, 0.75 * n.weight)

    g.export('test', directed=True, weighted=0.6)
