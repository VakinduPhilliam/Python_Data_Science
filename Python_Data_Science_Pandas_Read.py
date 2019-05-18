# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# In this script, we'll look at how to leverage tools like Pandas to explore and map out police activity
# in Montgomery County, Maryland. 
# Reading the data into Pandas.
# Now that we have the data as a list of lists, and the column headers as a list, we can create a Pandas
# Dataframe to analyze the data. If you're unfamiliar with Pandas, it's a data analysis library that uses
# an efficient, tabular data structure called a Dataframe to represent your data. Pandas allows you to convert
# a list of lists into a Dataframe and specify the column names separately.

import pandas as pd

stops = pd.DataFrame(data, columns=good_columns)
