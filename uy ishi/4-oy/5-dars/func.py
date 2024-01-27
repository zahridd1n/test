import psycopg2

conn = psycopg2.connect(
    database="ads_db",
    user='postgres',
    password='zahri1118',
    host="127.0.0.1",
    port='5432'
)


def take_data(table, column=None, value=None):
    cur = conn.cursor()
    if column:
        cur.execute(f'SELECT * FROM {table} WHERE {column} = {value}')
    else:
        cur.execute(f'SELECT * FROM {table}')

    keys = tuple(key.name for key in cur.description)
    datas = tuple(map(lambda row: dict(zip(keys, row)), cur.fetchall()))

    return datas