import sqlite3

def create_table(
    database_name:str,
    table_name:str,
    columns:str
) -> None: 
    """ Create a table on a specific database

    Args:
        database_name(str): A database's name.
        table_name(str): A table's name.
        columns(str): A query specifying the columns.
    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} ({columns})
    """)
    
    conn.close()
    