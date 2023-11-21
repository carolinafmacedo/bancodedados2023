import sqlite3

def delete_rows(
    database_name:str,
    table_name:str,
    query:str        
) -> None:
    """ Delete rows on a table.

    Args:
        database_name(str): A database's name.
        table_name(str): A table's name.
        query(str): A logical string that will be 
            passed to a WHERE clause.
    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(f"""
        DELETE FROM {table_name}
        WHERE {query}
    """)

    conn.commit()
    conn.close()