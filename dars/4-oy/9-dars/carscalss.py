import psycopg2
import cars
conn=psycopg2.connect(
                      database='cars',
                      user='postgres',
                      password='zahri1118',
                      host='127.0.0.1',
                      port='5432'
)
cursor=conn.cursor()

class Avto():
    @classmethod
    def __init__(cls,raqam,ism,number_type,region):
        # raqam=raqam
        # self.ism=ism
        # self.number_type=number_type
        # self.region=region
        cursor.execute(f"INSERT INTO cars_number(avto_raqam, ism_familya, viloyat, number_type) VALUES ('{raqam}','{ism}','{region}','{number_type}')")
        conn.commit()


    # def get_item(self):

for i in range(int(input('nech raqam qo\'shmoqchisiz'))):
    raqam = input('Avtomabil raqamni kiriting:')
    ism = input('Ism va familya:')
    if cars.validation(raqam):
        number_type = cars.number_check(raqam)
        region = cars.viloyat_func(raqam)
        Avto(raqam,ism,number_type,region)







