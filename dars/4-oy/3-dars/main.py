import psycopg2

conn=psycopg2.connect(
    database="school",
    user='postgres',
    password='zahri1118',
    host='127.0.0.1',
    port='5432'
)


cur=conn.cursor()
cur.execute('SELECT * FROM  staff')

keys=[key.name for key in cur.description]

datas =[]

for row in cur.fetchall():
    data_dict=dict(zip(keys,row))
    datas.append(data_dict)

# a=0
# for i in datas:
#     if i["age"]>a:
#         max_dic=i
#         a=i["age"]


max_obj=max(datas, key=lambda x:x['age'])


# print(max_dic)
print(max_obj)


# datas=tuple(map(lambda row: dict(zip(keys,row)) ,cur.fetchall()))

# print(datas)