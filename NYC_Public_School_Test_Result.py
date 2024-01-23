import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Create a pandas DataFrame called best_math_schools containing the "school_name" and "average_math" score for all schools where the results are at least 80% of the maximum possible score, sorted by "average_math" in descending order.
best_math_schools = schools[schools["average_math"] >= 640].sort_values("average_math", ascending = False)
best_math_schools = pd.DataFrame(best_math_schools[["school_name", "average_math"]])
# schools["average_math"].max()*0.8]

# Identify the top 10 performing schools based on scores across the three SAT sections, storing as a pandas DataFrame called top_10_schools containing the school name and a column named "total_SAT", with results sorted by total_SAT in descending order.
schools["total_SAT"] = schools["average_math"]+schools["average_reading"]+schools["average_writing"]
top_10_schools = schools[["school_name","total_SAT"]].sort_values("total_SAT", ascending=False)
top_10_schools = top_10_schools.head(10)

# Locate the NYC borough with the largest standard deviation for "total_SAT", storing as a DataFrame called largest_std_dev with "borough" as the index and three columns: "num_schools" for the number of schools in the borough, "average_SAT" for the mean of "total_SAT", and "std_SAT" for the standard deviation of "total_SAT". Round all numeric values to two decimal places.
import numpy as np
schools2=schools.groupby(['borough'], as_index=False).agg({'total_SAT':['count','mean','std']})
largest_std_dev = schools2[schools2.iloc[:,3]==schools2.iloc[:,3].max()]
#largest_std_dev = largest_std_dev.rename(columns={'count' :'num_schools','mean':'average_SAT','std':'std_SAT'})
#print(largest_std_dev)

largest_std_dev.columns=['borough','num_schools','average_SAT','std_SAT']
largest_std_dev = largest_std_dev.set_index("borough")
largest_std_dev.average_SAT=largest_std_dev.average_SAT.round(2)
largest_std_dev.std_SAT=largest_std_dev.std_SAT.round(2)
largest_std_dev.head()