# matni=input("matn kiriting:")
# def func(matn):
#     n=0
#     for i in matn:
#       if   i.isdigit():
#         n+=1
#     return n
# print(func(matn=matni))


# ismlar=['Ali','sarvar','muhammad']
# def upperis(ismlar):
#     for i in ismlar:
#         i.upper()
#

# pasword=input('password kiriting:')
# def func(passw):
#     if len(passw)>7:
#         return passw.isdigit and passw.isalpha()
#
#
#
# print(func(passw=pasword))


# ismlar=['Ali','sarvar','muhammad','aslbek','zaxiriddin']
# ismlar_natija=[]
# n = len(ismlar)//2
#
# if len(ismlar) % 2 == 0:
#     for i in ismlar[n//2]:
#         ismlar_natija.append(i)
# else:
#     for i in ismlar[n//2-1]:
#         ismlar_natija.append(i)
# print(ismlar_natija)
#

users=[]
id = 0
a=True
while a:
    id+=1
    username=input('username kiriting :')
    if username=='stop':
        break
    password=input('password kiriting :')
    users.append({
        'id':id,
        'username':username,
        'password':password
    })

usernameI=input()
passwordI=input()

for user in users:a
    if user['username']==usernameI and user['password']==passwordI:
        print(user['id'])
        break
    else:
        print('xato')

