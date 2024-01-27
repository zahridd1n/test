'''1-misol'''
# def func(numbers):








   #     result={}
#     a=numbers[0]
#     for index,item in enumerate(numbers):
#         s=abs(item-a)
#         result.update({s:index})
#         a=item
#     max_value=max(result.keys())
#     max_index=result.get(max_value)
#     n=(numbers[max_index-1],numbers[max_index])
#
#     return  f"{numbers}-> listdagi eng katta interval {n} sonlar orasida"
# print(func([1,3,6,8,15,20]))
#

'''2-misol'''
# def func(numbers):
#     a=float('inf')
#     b=None
#     for i in range(len(numbers)-1):
#         interval=numbers[i+1]-numbers[i]
#         if interval<a:
#             a=interval
#             b=(numbers[i],numbers[i+1])
#     return f"{numbers}-> listdagi eng kichik interval {b} sonlar orasida"
# print(func([1, 3, 8, 12, 13]))


'''3-misol'''
# def math(data):
#     operators=None
#     operators_index=None
#     result=None
#     for index,item in enumerate(data):
#         if item in ['+','-','*','/']:
#             operators_index = index
#             operators=item
#     firts=''.join(data[0:operators_index])
#     last=''.join(data[operators_index+1:])
#     if operators=='+':
#         n=int(firts)+int(last)
#     elif operators=='-':
#         n=int(firts)-int(last)
#     elif operators=='*':
#         n=int(firts)*int(last)
#     elif operators=='/':
#         n=int(firts)/int(last)
#     else:
#         raise ValueError('xatolik bor')
#     return f"{data} = {firts}{operators}{last}={n}"
#
# print(math(data=['1','2','0','-','5','5']))


'''4-misol'''

# def reverse_str(data):
#     my_list=data.split()
#     my_list.reverse()
#     result=' '.join(my_list)
#     return f"{data}  ->  {result}"
# print(reverse_str('Python mashhur dasturlash tili'))



'''5-misol'''
# def email_check(email):
#     data=[]
#     a,b,c,d,e=0,0,0,0,0
#     for i in email:
#         if '@' in i:
#             if i.endswith('@gmail.com') and a==0:
#                 data.append(i)
#                 a=1
#             if i.endswith('@mail.ru') and b==0:
#                 data.append(i)
#                 b=1
#             if i.endswith('@vkontakte.ru') and c==0:
#                 data.append(i)
#                 c=1
#             if i.endswith('@icloud.com') and d==0:
#                 data.append(i)
#                 d=1
#             if i.endswith('@yandec.ru') and e==0:
#                 data.append(i)
#                 e=1
#     return data
#
# email=['zahriddin','hatamovz047786@gmail.com','ali@mail.ru','hello','hsilwood5@vkontakte.ru','zx12112@icloud.com','husanboy@gmail.com']
# print(email_check(email))


'''6-misol'''
# data=[]
# for _ in range(int(input('nechta malumot qo\'shmoqchisiz? '))):
#     info={
#         'ism':input('ism kiriting:'),
#         'yil':int(input('tug\'lgan yil kiriting:')),
#         'oy':int(input('qaysi oyda tug\'lganligi:')),
#         'kun':int(input('qaysi kunda tug\'lganligi:')),
#     }
#     data.append(info)
# min_yil=0
# min_oy=0
# min_kun=0
# ism1=''
#
# max_yil=float('inf')
# max_oy=12
# max_kun=31
# ism2=''
#
# for i in data:
#
#     if i['yil']>min_yil:
#         min_yil=i['yil']
#         min_oy=i['oy']
#         min_kun=i['kun']
#         ism1=i['ism']
#     elif i['yil']==min_yil:
#         if i['oy']>min_oy:
#             min_yil = i['yil']
#             min_oy = i['oy']
#             min_kun = i['kun']
#             ism1 = i['ism']
#
#         elif i['oy']==min_oy:
#             if i['kun']>min_kun:
#                 min_yil = i['yil']
#                 min_oy = i['oy']
#                 min_kun = i['kun']
#                 ism1 = i['ism']
#
#
#     if i['yil']<max_yil:
#         max_yil=i['yil']
#         max_oy = i['oy']
#         max_kun = i['kun']
#         ism2 = i['ism']
#     elif i['yil']==max_yil:
#         if i['oy']<max_oy:
#             max_yil = i['yil']
#             max_oy = i['oy']
#             max_kun = i['kun']
#             ism2 = i['ism']
#         elif i['oy']==max_oy:
#             if i['kun']<min_kun:
#                 max_yil = i['yil']
#                 max_oy = i['oy']
#                 max_kun = i['kun']
#                 ism2 = i['ism']
#
#
# print('yoshi kichik',ism1)
# print('yoshi katta',ism2)
