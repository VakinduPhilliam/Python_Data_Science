# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# Sematic Networks and Perceptions.
# As a thought experiment, suppose we want to create an advertising campaign to promote Brussels, the capital
# of the European Union. How can the model pick, for example, a striking image or photograph? We want something
# a little bit more thought-provoking than retrieving brussels.jpg from the Web. In the words of Veale, Feyaerts
# & Forceville: we want something that compresses multiple meanings into a single form.
# Using the nearest_neighbors() function, we can shift the context of one concept to another concept as an exercise
# in combinatorial creativity.
# Unfortunately, perception has no Brussels concept.
# But we can annotate the semantic network by mining the Web with the tools in Pattern:

from pattern.web import Google, plaintext 
from pattern.search import search 
 
def learn(concept): 

    q = 'I think %s is *' % concept 
    p = [] 
    g = Google(language='en') 

    for i in range(10): 

        for result in g.search(q, start=i, cached=True): 

            m = plaintext(result.description) 
            m = search(q, m) # use * as wildcard 

            if m: 
                p.append(m[0][-1].string) 

    return [w for w in p if w in PROPERTIES] 

# The learn() function returns a list of known properties for a given concept, mined from Google’s search engine with
# an "I think * is *" query. This is adapted from a technique for ?nding similes (as * as *) described by Veale & Hao
# (2007). In this particular instance, the results are: expensive, great (2x), green and proud. 
# We update the semantic network on the fly:

for p in learn('Brussels'): 
    g.add_edge(p, 'Brussels', type='is-property-of') 

# Now we can do:

print nearest_neighbors(g['Brussels'], field(g['animal'])) 