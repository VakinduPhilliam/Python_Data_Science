# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# pattern.vector
# The pattern.vector module is a toolkit for machine learning, based on a vector space model of bag-of-words
# documents with weighted features (e.g., tf-idf) and distance metrics (e.g., cosine similarity, infogain).
# Models can be used for clustering (k-means, hierarchical), classification (Naive Bayes, Perceptron, k-NN, SVM)
# and latent semantic analysis (LSA).

from pattern.web    import Twitter
from pattern.en     import tag
from pattern.vector import KNN, count

twitter, knn = Twitter(), KNN()
    
    for i in range(1, 10):
        for tweet in twitter.search('#win OR #fail', start=i, count=100):
            s = tweet.text.lower()
            p = '#win' in s and 'WIN' or 'FAIL'
            v = tag(s)
            v = [word for word, pos in v if pos == 'JJ'] # JJ = adjective
            v = count(v) 
            if v:
                knn.train(v, type=p)
    
    print knn.classify('sweet potato burger')
    print knn.classify('stupid autocorrect')
 
# Displays
# 'WIN'
# 'FAIL'
