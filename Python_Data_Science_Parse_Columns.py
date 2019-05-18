# Python Data Science and Analytics.
# Data Science is a field in computer science that is dedicated to analyzing patterns in raw data using
# techniques like Artificial Intelligence (AI), Machine Learning (ML), mathematical functions, and
# statistical algorithms.
# In this script, we'll look at how to leverage tools like Pandas to explore and map out police activity
# in Montgomery County, Maryland. 
# Oddly enough, time of day and the date of the stop are stored in two separate columns, time_of_stop, and
# date_of_stop. We'll parse both, and turn them into a single datetime column:

import datetime

def parse_full_date(row):

    date = datetime.datetime.strptime(row["date_of_stop"], "%Y-%m-%dT%H:%M:%S")
    time = row["time_of_stop"].split(":")

    date = date.replace(hour=int(time[0]), minute = int(time[1]), second = int(time[2]))

    return date

stops["date"] = stops.apply(parse_full_date, axis=1)
