def build_table_query(
    table_name:str
):
    """ Build the query to retrieve the table
    Args:
        table_name(str): A table's name.
    """

    query = f"""
        SELECT *
        FROM {table_name}
    """
    return  query