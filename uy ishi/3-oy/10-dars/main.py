"""1-misol"""
# numbers=[1,2,3,4,5,6,1]
#
# def func(numbers):
#     a=""
#     for i in numbers:
#         a=a+str(i)
#     return a
# print(func(numbers))
#


"""2-misol"""

# my_list=[2,3,4,"-",3,4]
#
# def func(my_list):
#     a=''
#     b=''
#     for i in my_list:
#         if isinstance(i,str):
#             break
#         a += str(i)
#
#     a=int(a)
#     for j in my_list[::-1]:
#         if isinstance(j,str):
#             break
#         b += str(j)
#
#     b=int(b[::-1])
#     result=0
#     for ishora in my_list:
#         if ishora=="+":
#             result=a+b
#         elif ishora=="-":
#             result=a-b
#         elif ishora=="*":
#             result=a*b
#         elif ishora=="/":
#             result=a/b
#     return result
# print(func(my_list))

"""3-misol"""

# my_text="The python string metods "
# def end_items(text):
#     a=text.split()
#     return a[-1]
#
# print(end_items(my_text))


"""4-misol"""
# mylist=[121,"aka",12,20002,"salom"]
#
# def palindroms(mylist):
#     palindrom_elements=[]
#     for i in mylist:
#
#         if str(i)[0]==str(i)[-1]:
#             palindrom_elements.append(i)
#     return f"palindrom elementlar:{palindrom_elements}"
# print(palindroms(mylist))`

# import string
#
"""5-misol"""
# my_list=[1,">","Aka","=","AMMA","!"]
# def func(my_list):
#     check_list=[]
#     palindrom_numbers=[]
#
#     for i in string.punctuation:
#             if i  in my_list:
#                 my_list.remove(i)
#
#     for element in my_list:
#         element=str(element)
#         check_list.append(element.lower())
#
#     for items in check_list:
#         if items[0]==items[-1] and len(items)>1:
#             palindrom_numbers.append(items)
#
#     return palindrom_numbers
# print(func(my_list))