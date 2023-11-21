from queries.build_table_query import build_table_query
import pandas as pd 
import sqlite3

def get_table(
    database_name:str,
    table_name:str
) -> pd.DataFrame:
    """Retrieve table from database

    Args:
        database_name (str): created database name 
        table_name (str): table name 

    Returns:
        pd.DataFrame: A dataframe from a table in database
    """
    conn = sqlite3.connect(database_name)
    query = build_table_query(table_name)
    df = pd.read_sql_query(query,conn)
    
    return df