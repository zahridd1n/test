import psycopg2

con=psycopg2.connect(
    database='school',
    user='postgres',
    password='zahri1118',
    host='127.0.0.1',
    port='5432'
)

"""staff table """
cursor=con.cursor()
cursor.execute('SELECT * FROM staff')

keys=[key.name for key in cursor.description]

staff_obj=[]

for row in cursor.fetchall():
    staff_info=dict(zip(keys,row))
    staff_obj.append(staff_info)

staff_obj=tuple(staff_obj)
print(staff_obj)

"""max va min yoshli hodimlarni topish"""
max_age=max(staff_obj,key=lambda x:x['age'])
min_age=min(staff_obj,key=lambda x:x['age'])
print('Yoshi eng katta hodim->', max_age)
print('Yoshi eng kichik hodim->',min_age)





"""students table"""
# cur=con.cursor()
# cur.execute("SELECT * FROM students")
#
# keys=[key.name for key in cur.description]
#
# students_obj=tuple(map(lambda x:dict(zip(keys,x)),cur.fetchall()))
# print(students_obj)





"""olimpiada table """
# cur=con.cursor()
# cur.execute('SELECT * FROM olimpiada')

# keys=[key.name for key in cur.description]
# olimpiada_obj=tuple(map(lambda x:dict(zip(keys,x)),cur.fetchall()))
# print(olimpiada_obj)
#

"""olimpiada ishtirokchilarini o'rniga qarab chiqarish"""
# olimpiada_obj=list(olimpiada_obj)
# sort=sorted(olimpiada_obj,key=lambda x:x['olgan_orni'])
# print(sort)
