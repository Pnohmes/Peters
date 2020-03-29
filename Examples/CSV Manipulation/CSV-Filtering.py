import pandas as pd
import numpy as np
import pprint
# Reads csv from any url
df = pd.read_csv('http://winterolympicsmedals.com/medals.csv')

# Filters based on number and string comparison, exports to filter2.csv
df[
    (df['Year'] < 2006) &
    (df['City'].str.contains('Salt'))
    ].to_csv(
        './filter.csv',
        mode='w',header=True
        )
