# misol1
# sinflist=[]
# son=int(input("o'quvchilar soni:"))
# for i in range(son):
#     sinf={
#         'ism':input('ismingiz nima:'),
#         'familya':input('familya nima:'),
#         'yosh':int(input('yoshingizni kiriting:'))
#     }
#     sinflist.append(sinf)
# print(list(filter(lambda i:i['yosh']>=16,sinflist)))

# misol2
# tel= input('telefon raqamni kiriting:') # +998907862817
# if len(tel)==13 and tel.start
# swith('+998'):
#     if tel[4:6]=='90' or tel[4:6]=='91':
#         print('sizning raqamingiz validatsiyadan o`tdi va Beeline SIM karta ekan')
#     elif tel[4:6]=='93' or tel[4:6]=='94' or tel[4:6]=='50':
#         print('sizning raqamingiz validatsiyadan o`tdi va Ucell SIM karta ekan')
#     elif tel[4:6]=='99' or tel[4:6]=='95':
#         print('sizning raqamingiz validatsiyadan o`tdi va Uzmobile SIM karta ekan')
#     elif tel[4:6]=='97' or tel[4:6]=='88':
#         print('sizning raqamingiz validatsiyadan o`tdi va Mobiuz SIM karta ekan')
#     elif tel[4:6]=='33':
#         print('sizning raqamingiz validatsiyadan o`tdi va Humans SIM karta ekan')
#
#     else:
#         print('Validatsiyadan o\'tmadi bunday operator yo\'q')
# else:
#     print('Validatsiyadan o\'tmadi raqam xato kiritlgan')

# misol3
# avtoraqam=input('Jismoniy Shaxs avto raqaminin  kirintng:') #40O113HA
# avtoraqam=avtoraqam.upper()
def j_r(raqam):
    if len(raqam)==8:
        if raqam[0:2].isdigit() and raqam[3:6].isdigit():
            if raqam[2:3].isalpha() and raqam[6:8].isalpha():
                return (raqam,"Jismoniy shaxs avtomabil raqami tekshiruvdan o'tdi")
            else:
                return ('raqam xato kiritilgan')
        else:
            return ('raqam xato kiritilgan')
    else:
        return ('raqam 8 da belgidan iborat bo\'lishi kerak')

# print(j_r(raqam=avtoraqam))

# misol4
# avtoraqam=input('yurisik shaxs avto raqamini kiriting:') #40588AAA
# avtoraqam=avtoraqam.upper()
def y_r(raqam):
    if len(raqam)==8 and raqam[0:5].isdigit() and raqam[5:-1].isalpha():
        return (raqam,'Yuridik shaxs avto raqami tekshiruvdan o\'tdi')
    else:
        return "kiritilgan malumot xato"
#
# print(y_r(raqam=avtoraqam))



# misol5
avtoraqam=input('avto raqam kiriting:')
def malumot_tekshir(raqam):
    result_j = j_r(raqam)
    result_y = y_r(raqam)

    if result_j[1] == "Jismoniy shaxs avtomabil raqami tekshiruvdan o'tdi" and result_y[1] != "Yuridik shaxs avto raqami tekshiruvdan o'tdi":
        return result_j
    elif result_y[1] == "Yuridik shaxs avto raqami tekshiruvdan o'tdi" and result_j[1] != "Jismoniy shaxs avtomabil raqami tekshiruvdan o'tdi":
        return result_y
    else:
        return "kiritilgan malumot xato"

print(malumot_tekshir(raqam=avtoraqam))