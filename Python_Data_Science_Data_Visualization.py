# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Tweet Data Mining and Visualization.
# We can parse the nouns in the comparison from each tweet and bundle them in a graph. Calculating centrality 
# should then give us an idea of new concepts pointing to newer concepts, pointing to the newest concept.
# The visualization was realized in NodeBox for OpenGL, a Python module that generates 2D interactive animation
# using OpenGL. It comes with functionality for drawing graphs – more specifically with a Graph object that is 
# identical to pattern.graph.Graph. Output from Pattern can easily be plugged into NodeBox. Essentially, we have
# the Twitter data stored in a Datasheet on which we create an iterator function. Each time comparison() is called
# it yields a (concept1, concept2, date)-tuple (or None), where concept1 is the new concept2:

from pattern.db     import Datasheet, date
from pattern.en     import parse, Sentence
from pattern.search import search
 
rows = iter(Datasheet.load('the_new.txt'))

def comparison(exclude=['', 'i', 'me', 'it', 'side', 'he', 'mine']):   

    try:

        r = rows.next() # Fetch next row in the matrix.
        p = Sentence(parse(r[2], lemmata=True, light=True))
        m = search('NP be the new NP', p)
        a = m[0].constituents()[ 0].head.string.upper().strip('.!'"#')
        b = m[0].constituents()[-1].head.string.upper().strip('.!'"#')

        if a not in exclude and b not in exclude:

            # Additionally, we could check if a and b occur in WordNet
            # to get "clean" nouns in the output.

            return b, a, date(r[-1])

    except:
        pass

# We load a portion of the comparisons into a graph. This is the tricky part. If we load all of them, we don't have anything
# to animate. If we load too few, there may not be enough hooks to connect new concepts to. 

from nodebox.graphics import *
from nodebox.graphics.physics import Graph
 
g = Graph()

for i in range(700):
    n = comparison()

    if n is not None:
        b,a,d = n

        g.add_node(b, stroke=(1,1,1,0.1), text=(1,1,1,0.5), fontsize=7)
        g.add_node(a, stroke=(1,1,1,0.1), text=(1,1,1,0.5), fontsize=7)
        g.add_edge(b, a, stroke=(1,1,1,0.1))

g = g.split()[0]

# Next we implement a NodeBox draw() loop, which is called each frame of animation. 
# It updates and draws the graph, and incrementally adds new comparisons to it.

def draw(canvas): 
    background(0.18, 0.22, 0.28)
    translate(300, 300)

    g.betweenness_centrality()
    g.update()
    g.draw()

    for i in range(4): # Add up to 4 new nodes per frame.
        n = comparison()

        if n:
            b,a,d = n

            if a in g or b in g:

                if a in g: g[a].text.fill.alpha = 0.75
                if b in g: g[b].text.fill.alpha = 0.75

                g.add_node(a, stroke=(1,1,1,0.1), text=(1,1,1,0.5), fontsize=7)
                g.add_node(b, stroke=(1,1,1,0.1), text=(1,1,1,0.5), fontsize=7)
                g.add_edge(b, a, stroke=(1,1,1,0.1))

    for n in g.nodes:

        # Nodes with more connections grow bigger.

        n.radius = 3 + n.weight*6 + len(n.links)*0.5
 
canvas.size = 600, 600
canvas.fps = 40
canvas.run(draw)
