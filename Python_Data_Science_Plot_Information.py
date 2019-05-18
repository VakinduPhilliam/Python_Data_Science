# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# In this script, we'll look at how to leverage tools like Pandas to explore and map out police activity
# in Montgomery County, Maryland. 
# We can now make a plot of which days result in the most traffic stops:

import matplotlib.pyplot as plt

%matplotlib inline 

plt.hist(stops["date"].dt.weekday, bins=6)
