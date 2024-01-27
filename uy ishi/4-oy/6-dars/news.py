import psycopg2

conn=psycopg2.connect(
    database='news',
    user='postgres',
    password='zahri1118',
    host="127.0.0.1",
    port='5432'
)



def take_data(table,column=None,value=None):
    cur = conn.cursor()
    if column:
        cur.execute(f'SELECT * FROM {table} WHERE {column}={value}')
     
    else:
        cur.execute(f"SELECT * FROM {table} ")

    
    
    keys=list(key.name for key in cur.description)
    datas=list(map(lambda x:dict(zip(keys,x)),cur.fetchall()))

    return datas

 
news=take_data('news')
for new in news:
    user=take_data('news_user','id',new['user_id'])[0]
    del new['user_id']
    new['author']=user
    
    category=take_data('category','id',new['category_id'])[0]
    del new['category_id']
    new['category']=category
    
    region=take_data('region','id',new['region_id'])[0]
    del new['region_id']
    new['region']=region
   
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(id) FROM view WHERE news_id={new['id']} ")
    view=cur.fetchall()
    new['view']=[t[0] for t in view if isinstance(t[0],int)][0]

    cur.execute(f'SELECT marks FROM review WHERE news_id={new["id"]}')
    review=cur.fetchall()
    result=[i[0] for i in review if isinstance(i[0],int)]
    new['review']=sum(result)/len(result)
    
    print(new,'\n')
