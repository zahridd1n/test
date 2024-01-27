import psycopg2

conn=psycopg2.connect(database='shop',user='postgres',password='zahri1118',    host="127.0.0.1", port='5432')



cur=conn.cursor()
# cur.execute('SELECT MAX(price) FROM product')
#
# print(cur.fetchall())

# cur.execute("SELECT category_id FROM product ORDER BY price DESC LIMIT 1 ")
# max_category=cur.fetchall()[0][0]
# # max_categor=[t[0] for t in max_category if isinstance(t[0],int)]
# cur.execute(f'SELECT name FROM category WHERE id={max_category}')
# print(cur.fetchall())

# for i in range(int(input('NEcha dona maxsulot kiritasiz'))):
#
#     nom = input('nom')
#     price = float(input('narxi:'))
#     quantity= int(input('soni:'))
#
#     cur.execute('SELECT name FROM category;')
#     for element in cur.fetchall():
#         print(element[0])
#     wish=input('kategorya nomini kiriting: ')
#     cur.execute(f"SELECT id  FROM CATEGORY WHERE name'{wish}'")
#     category_id = cur.fetchall()[0][0]
#     cur.execute(f"INSERT INTO product(name,price,quantity,category_id) VALUES '({nom})',({price}),({quantity}),({category_id})")
#     conn.commit()


query=input('nima qidirmoqchisiz:')
cur.execute(f"SELECT * FROM product WHERE name LIKE '%{query}%' ")
print(cur.fetchall())