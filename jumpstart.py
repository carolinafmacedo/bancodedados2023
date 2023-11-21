import pandas as pd
import sqlite3

# create the dataframe
data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# create database and save
# the dataframe
conn = sqlite3.connect('mydatabase.db')

# Use the to_sql method to save the DataFrame to a table in the database
data.to_sql('client', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()