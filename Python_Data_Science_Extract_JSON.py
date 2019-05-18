# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# In this script, we'll look at how to leverage tools like Pandas to explore and map out police activity
# in Montgomery County, Maryland. 
# Extracting information on the JSON columns.
# We can accomplish this using the ijson package.
# ijson will iteratively parse the json file instead of reading it all in at once.
# This is slower than directly reading the whole file in, but it enables us to work with large files that
# can't fit in memory.
# To use ijson, we specify a file we want to extract data from, then we specify a key path to extract:

import ijson

filename = "md_traffic.json"

with open(filename, 'r') as f:

    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)