from functions.create_table import create_table

create_table(
    database_name = 'test.db',
    table_name = 'tabela',
    columns ='nome, idade, id'
)
from functions.insert_rows import insert_many_rows

insert_many_rows(
'test.db', 'tabela',
'nome, idade, id',
[(99, "Luiz", 53), (100, "Rafael", 20)]
 )