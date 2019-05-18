# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# Pattern is a web mining module for the Python programming language.
# It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser), natural
# language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet), machine learning
# (vector space model, clustering, SVM), network analysis and <canvas> visualization.
# pattern.en
# The pattern.en module is a natural language processing (NLP) toolkit for English. Because language is ambiguous
# (e.g., I can <-> a can) it uses statistical approaches + regular expressions. This means that it is fast, quite
# accurate and occasionally incorrect. It has a part-of-speech tagger that identifies word types (e.g., noun, verb,
# adjective), word inflection (conjugation, singularization) and a WordNet API.
# Parsers for Spanish, French, Italian, German and Dutch are also available: 

from pattern.en import parsetree
     
    s = 'The mobile web is more important than mobile apps.'
    s = parsetree(s) 

    for sentence in s: 

     for chunk in sentence.chunks:

            for word in chunk.words:

                print word,

            print
 
# Displays
# Word(u'The/DT') Word(u'mobile/JJ') Word(u'web/NN')
# Word(u'is/VBZ')
# Word(u'more/RBR') Word(u'important/JJ')
# Word(u'than/IN')
# Word(u'mobile/JJ') Word(u'apps/NNS')
