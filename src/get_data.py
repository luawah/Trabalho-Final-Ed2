import pandas as pd
from models.Country import Country as Country

# Variables for read_csv
original_table = '../databases/Summer-Olympic-medals-1976-to-2008.csv'
original_cols = ['Year','Discipline', 'Country', 'Medal']
encoding='latin-1'

# Reading the csv data
original_csv_df = pd.read_csv(original_table, usecols=original_cols, encoding=encoding )

# Filtering data to only contain rows from Beijing 2008 Olympics
#beijing_data = original_csv_df[original_csv_df['Year'] == 2008]

# Grouping the rows so we can get a count of medals for each country by each discipline
original_csv_df = original_csv_df.groupby(by=['Year','Discipline','Country'])["Medal"].count().reset_index()

# Transforming the last Series into a List of Dictionaries
datarows = original_csv_df.to_dict('records');
