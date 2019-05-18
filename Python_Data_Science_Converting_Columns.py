# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# In this script, we'll look at how to leverage tools like Pandas to explore and map out police activity
# in Montgomery County, Maryland. 
# Converting columns.
# We're now almost ready to do some time and location based analysis, but we need to convert the longitude,
# latitude, and date columns from strings to floats first. We can use the below code to convert latitude
# and longitude:

import numpy as np

def parse_float(x):

    try:
        x = float(x)

    except Exception:
        x = 0
    return x

stops["longitude"] = stops["longitude"].apply(parse_float)
stops["latitude"] = stops["latitude"].apply(parse_float)
