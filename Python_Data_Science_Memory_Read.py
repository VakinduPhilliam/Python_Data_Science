# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# In this script, we'll look at how to leverage tools like Pandas to explore and map out police activity
# in Montgomery County, Maryland. 
# Extracting JSON data.
# You may recall that the data is locked away in a list of lists inside the data key. We'll need to read this 
# data into memory to manipulate it.
# Fortunately, we can use the column names we just extracted to only grab the columns that are relevant.
# This will save a ton of space. If the dataset was larger, you could iteratively process batches of rows. 
# So read in the first 10000000 rows, do some processing, then the next 10000000, and so on. In this case, we 
# can define the columns we care about, and again use ijson to iteratively process the JSON file:

good_columns = [
    "date_of_stop", 
    "time_of_stop", 
    "agency", 
    "subagency",
    "description",
    "location", 
    "latitude", 
    "longitude", 
    "vehicle_type", 
    "year", 
    "make", 
    "model", 
    "color", 
    "violation_type",
    "race", 
    "gender", 
    "driver_state", 
    "driver_city", 
    "dl_state",
    "arrest_type"
]

data = []

with open(filename, 'r') as f:
    objects = ijson.items(f, 'data.item')

    for row in objects:
        selected_row = []

        for item in good_columns:
            selected_row.append(row[column_names.index(item)])

        data.append(selected_row)
