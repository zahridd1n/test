import psycopg2
import carscalss

conn=psycopg2.connect(
                      database='cars',
                      user='postgres',
                      password='zahri1118',
                      host='127.0.0.1',
                      port='5432'
)
def validation(raqam:str):
    if len(raqam) == 8:
        natija = True
    else:
        natija=False
    return natija

def number_check(raqam):
    #40A113HA 40223AAA
    if raqam[:2].isdigit() and raqam[2].isalpha() and raqam[3:6].isdigit() and raqam[6:].isalpha():
        result='Jismoniy shaxs'
    elif raqam[:5].isdigit() and raqam[5:].isalpha():
        result='Yuridik shaxs'
    else:
        raise ValueError("xato farmatagi raqam kiritildi")

    return result

def viloyat_func(raqam):
    avto_key=int(raqam[:2])
    viloyat=None
    if avto_key>=1 and avto_key<=9:
        viloyat='Toshkent shahri'
    elif  avto_key>=10 and avto_key<=19:
        viloyat='Toshkent viloyati'
    elif  avto_key>=20 and avto_key<=24:
        viloyat='Sirdaryo viloyati'
    elif  avto_key>=25 and avto_key<=29:
        viloyat='Jizzax viloyati'
    elif  avto_key>=30 and avto_key<=39:
        viloyat='Samarqand viloyati'
    elif  avto_key>=40 and avto_key<=49:
        viloyat='Farg`ona viloyati'
    elif  avto_key>=50 and avto_key<=59:
        viloyat='Namangan viloyati'
    elif  avto_key>=60 and avto_key<=69:
        viloyat='Andijon viloyati'
    elif  avto_key>=70 and avto_key<=74:
        viloyat='Qashqadaaryo viloyati'
    elif  avto_key>=75 and avto_key<=79:
        viloyat='Surxandaryo'
    elif  avto_key>=80 and avto_key<=84:
        viloyat='Buxoro viloyati'
    elif  avto_key>=85 and avto_key<=89:
        viloyat='Navoiy viloyati'
    elif  avto_key>=90 and avto_key<=94:
        viloyat='Xorazm viloyati'
    elif  avto_key>=95 and avto_key<=99:
        viloyat='Qoraqalpog`iston Respublikasi'
    return viloyat


# cur=conn.cursor()
# for i in range(int(input('nech raqam qo\'shmoqchisiz'))):
#     raqam = input('Avtomabil raqamni kiriting:')
#     ism = input('Ism va familya:')
#     if validation(raqam):
#         number_type = number_check(raqam)
#         region = viloyat_func(raqam)
        # cur.execute(f"INSERT INTO cars_number(avto_raqam, ism_familya, viloyat, number_type) VALUES ('{raqam}','{ism}','{region}','{number_type}')")
        # conn.commit()
        #
