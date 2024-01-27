# text=input('so\'z kiritig:')
# if text==text[::-1]:
#     print('palindrom so\'z')
# else:
#     print('palindromn emas')


# def index(text,item):
#     counter=0
#     for i in text:
#         if counter==item:
#             return i
#         elif item>len(text):
#             raise IndentationError
#         counter+=1
#
# print(index(text='Zaxiriddin',item=3))




def func(item,text):
    for i,word in enumerate(text):
        if item==word:
            return i
    raise IndentationError('xatolik')

print(func(item='a',text='qalesiz'))