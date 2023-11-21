import sqlite3

def delete_rows(
    database_name:str,
    table_name:str,
    query:str
) -> None:


conn = sqlite3.connect(database_name)
cursor = conn.cursor()

cursor.execute(f"""
    DELETE FROM {table_name}
    WHERE {query}
    """)

    conn.commit()
    conn.close()