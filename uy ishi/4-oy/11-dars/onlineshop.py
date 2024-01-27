import psycopg2

conn=psycopg2.connect(database='online_shop',user='postgres',password='zahri1118',host='127.0.0.1',port='5432')
name_inp=input('ismingizni kiriting:').capitalize()
password_inp=input('parolingizni kiriting:')
cursor=conn.cursor()
cursor.execute(f"SELECT * FROM users WHERE name='{name_inp}' AND password='{password_inp}'")
result=cursor.fetchall()

if result:
    id = result[0][0]
    umumiynarx = 0
    sorov=input('savatcha korishni xoxlaysizmi:')
    if sorov=='ha':
        cursor.execute(f"SELECT count(is_active) FROM cart WHERE is_active=true AND user_id={id}")
        carttrue=cursor.fetchall()[0][0]
        print(f"faol savatchalar:{carttrue} ta")

        cursor.execute(f"SELECT id  FROM cart WHERE is_active=true AND user_id={id}")
        active_cart=cursor.fetchall()

        for i in active_cart:
            cursor.execute(f"SELECT product_id,qunatitiy  FROM product_cart WHERE cart_id={i[0]}")
            a=cursor.fetchall()
            cursor.execute(f"SELECT name,price FROM product WHERE id={a[0][0]} ")
            b=cursor.fetchall()
            umumiynarx+=b[0][1]
            print(f"maxsulot nomi:{b[0][0]}, narxi:{b[0][1]} soni:{a[0][1]}")
        print(f' umumiy narx:{umumiynarx}')
        print()



        umumiynarx=0
        cursor.execute(f"SELECT count(is_active) FROM cart WHERE is_active=false AND user_id={id}")
        cartfalse=cursor.fetchall()[0][0]
        print(f"no faol savatchalar:{cartfalse} ta")

        cursor.execute(f"SELECT id  FROM cart WHERE is_active=false AND user_id={id}")
        nonactive_cart = cursor.fetchall()

        for j in nonactive_cart:
            cursor.execute(f"SELECT product_id,qunatitiy  FROM product_cart WHERE cart_id={j[0]}")
            z = cursor.fetchall()
            cursor.execute(f"SELECT name,price FROM product WHERE id={z[0][0]} ")
            x = cursor.fetchall()
            umumiynarx += x[0][1]
            print(f"maxsulot nomi:{x[0][0]}, narxi:{x[0][1]} soni:{z[0][1]} ")
        print(f' umumiy narx:{umumiynarx}')
    else:
        print('dastur tugadi')
else:
    print('xatolik')