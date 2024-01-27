# avtomabil={
#     'nom':'jentra',
#     'rang':'qora',
#     'yili':2021,
#     'lyuk':True,
#     'disk':15,
#     'abs':True,
#     'egalar':['men']
# }
# print(avtomabil['lyuk'])

# student={
#     'FIO':'Xatamov Zaxiriddin Nosirjonovich',
#     'oliygoh':'TATU',
#     'yosh':19,
#     'fakultet':'Kompyter injineringi:',
#     'yo`nalish':'Kompyter injineringi:',
#     'kurs':2,
#     'fanlar soni':6,
#     'is_grand':True,
#     'baxo':5,
#     'bitirish yili':2026
# }


# persons=[]
# quality=int(input('necha kishisilar:'))
# for _ in range(quality):
#     data={
#         'ism':input('ismingiz nima:'),
#         'famil':input('familyangiz nima:'),
#         'yosh':int(input('yoshingiz nechida:'))
#         }
#     persons.append(data)
# for person in persons:
#     if(
#         person['ism'].endswith('jon') or
#         person['ism'].endswith('xon') or
#         person['ism'].endswith('bek')
#         ):
#         print(person)

# person=list(filter(lambda a:a['ism'].endswith('jon'),persons))
# print(person)


# masala


son=int(input('soni kiriting:'))
if 99<son<1000:
    birlar=son%10
    onlar=(son%100)//10
    yuzlar=son//100

    dic_birlar={
        1:'bir',
        2:'ikki',
        3:'uch',
        4:'tort',
        5:'besh',
        6:'olti',
        7:'yetti',
        8:'sakkiz',
        9:'to\'qqiz'
    }

    dic_onlar={
        1:'o`n',
        2: 'yigirma',
        3: 'o\'tiz',
        4: 'qirq',
        5: 'ellik',
        6: 'oltimish',
        7: 'yettimish',
        8: 'sakksan',
        9: 'to\'qqsan'
    }



    print(dic_birlar.get(yuzlar,''),'yuz',dic_onlar.get(onlar,''),dic_birlar.get(birlar,''))

else:
    print("3 xonali son kiritish lozim")