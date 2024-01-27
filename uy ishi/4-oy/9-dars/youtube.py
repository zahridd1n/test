import psycopg2

conn = psycopg2.connect(database='youtube',user='postgres',password='zahri1118',host='127.0.0.1',port='5432')
cursor = conn.cursor()

tables={
    1:'youtube_user',
    2:'post',
    3:'comment',
    4:'reaction'
}
print(tables)
insert_table = int(input('qaysi tablega malumot kiritimoqchisiz:'))
for i in range(int(input('nechta ma`lummot qo\'shmoqchisiz'))):
    if insert_table==1:
        email = input('email kiriting:')
        username = input('username kiriting:')
        nick_name = input('nickname kiriting:')
        bio = input('o\'zingiz haqingizda malumot kiriting (ixtiyoriy):')
        profil_image = input('profil rasm joylashuini kiriting:')

        cursor.execute(f"INSERT INTO youtube_user(email, username, nick_name, bio, profil_image) VALUES ('{email}','{username}','{nick_name}','{bio}','{profil_image}')")
        conn.commit()

    elif insert_table==2:
        post_path=input('postdagi videoning xotiradagi joylashunivi kiriting:')
        title=input('postning sarlavhasini kiriting:')
        description=input('post haqida qo`shimcha maulumot:')
        cursor.execute('SELECT id,nick_name,email FROM youtube_user')
        for author in cursor.fetchall():
            print(author)
        author_id=int(input('video mulafining id raqamini kiritng'))
        cursor.execute(f"INSERT INTO post(post_elemtn_path, title, description, author_id) VALUES ('{post_path}','{title}','{description}',{author_id})")
        conn.commit()

    elif insert_table==3:
        #post_id yani coment qaysi postag tegihliligi
        cursor.execute('SELECT id,titl  e,post_elemtn_path FROM post')
        for post in cursor.fetchall():
            print(post)
        post_id = int(input('komentarya qaysi videga tegishliligini kiritng:'))

        comment_text = input('commentarya matnini kiriting:')
        #author_id yani coment kimga tegishliligi
        cursor.execute('SELECT id,nick_name,email FROM youtube_user')
        for author in cursor.fetchall():
            print(author)
        author_id=int(input('comentarya mulafining id raqamini kiritng'))
        cursor.execute(f"INSERT INTO comment(comment_text,post_id, comment_author) VALUES ('{comment_text}',{post_id},{author_id})")
        conn.commit()

    elif insert_table==4:

        reaction_type =(int(input('like uchun 1, dislayk uchun 2 qiymatni kiritng:')))
        if reaction_type ==1 or reaction_type==2:
            cursor.execute('SELECT id,title,post_elemtn_path FROM post')
            for post in cursor.fetchall():
                print(post)
            reaction_post = int(input('qaysi videoga reaksiya qoldirmoqchisiz:'))

            cursor.execute('SELECT id,nick_name,email FROM youtube_user')
            for author in cursor.fetchall():
                print(author)
            reaction_author = int(input('like bosgan userning id raqamini kiritng:'))

            check_reaction = f'{reaction_post}and{reaction_author}'
            cursor.execute(f"INSERT INTO reaction(reaction_post,reaction_type,author,check_reaction) VALUES ({reaction_post},{reaction_type},{reaction_author},'{check_reaction}')")
            conn.commit()
        else:
            raise ValueError('1 yoki 2 qiymat qabul qilinadi!')






