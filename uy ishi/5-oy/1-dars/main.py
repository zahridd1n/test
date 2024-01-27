"""quyidagi masalalarni yechish: 1) Berilgan strni oxirgi so`zidagi elementlar sonini topish: "salom senga" -> senga(5)
2) Berilgan strni ichidagi so`zlar sonini topish: "salom senga: -> 2
3) berilgan listdagi har juft elementi teskari qilish
4) strni ichidagi bo`sh joylarni olib tashlab palindromlikga tekshirish
5) str ichidagi shart belgialrni olib tashlab palindromlikga tekshirish"""
import string

'''1-misol'''

text="O‘zbekiston Avstraliya bilan durang o‘ynadi"
data = text.split()
print(data[-1],'->',len(data[-1]))


'''2-misol'''
'''1-usul'''
# text =  "O‘zbekiston Avstraliya bilan durang o‘ynab Osiyo kubogi pley-offiga chiqdi"
#
# a=text.count(' ')+1
# print('matn uzunligi->',a)
'''2-usul'''
# mylist=text.split()
# print(f'matn uzunligi-> {len(mylist)}')


'''3-misol'''
# my_list=[1,2,3,4,5,6,7,8,'a','b']
# new_list=[]
# for i in range(len(my_list)):
#     # print(i)
#     if i%2==0:
#         new_list.append(my_list[i+1])
#     else:
#         new_list.append(my_list[i-1])
# print(new_list)


'''4-misol'''
# text='all a '
# data=''
# for i in text:
#     if ' ' not in i:
#         data+=i
# if data==data[::-1]:
#     print(f"{data}-> palindrom so'z")
# else:
#     print(f"{data}-> palindrom emas")
#



'''5-misol'''
# text="najot_ta'lim!"
# data=''
# for i in text:
#     if i  not in string.punctuation:
#         data+=i
# if data==data[::-1]:
#     print(f"{data}-> palindrom so'z")
# else:
#     print(f"{data}-> palindrom emas")
