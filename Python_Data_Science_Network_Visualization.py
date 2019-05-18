# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Network visualization.
# The functions in the pattern.graph module are identical to those in the graph module in NodeBox for OpenGL.
# We can combine the two implementations to visualize the network, using a force-directed algorithm to place
# the nodes on a 2D canvas. 

from nodebox.graphics import * 
from nodebox.graphics.physics import Graph as NodeBoxGraph 
 
g1 = g.copy(nodes=halo(g['rocket'])) 
g2 = NodeBoxGraph() 

for e in g1.edges: 
    g2.add_edge(e.node1.id, e.node2.id) 
 
def draw(canvas): 
    canvas.clear() 
    translate(canvas.width / 2, canvas.height / 2) 

    g2.update() 
    g2.draw() 
 
canvas.draw = draw 
canvas.run()
