file=open("text.txt","w")
file.write("HTML veb sahifalarni yaratish uchun ishlatiladigan markaziy tildir. Bu til, matn,"
           " rasmlar, videolar, linklar va boshqa tarkibiy elementlarni \n saqlash va tuzatish uchun mo'ljallangan. "
           "Veb brauzerlar bu HTML kodi orqali sahifani tuzilgan holda ko'rsatishadi.")
file.close()


"""1-misol"""
# file=open("text.txt","r")
# text_read=file.read()
# text_len=len(text_read.split())
# print(text_len)
# file.close()


"""2-misol"""
# file=open("text.txt","r")
# text_read=file.read()
# text_list=text_read.split()
# file.close()
#
# max_unli=0
# dict_item={}
# for item in text_list:
#     a = 0
#     for i in item:
#         if i=="o":
#             a+=1
#         if i=="a":
#             a+=1
#         if i=="i":
#             a+=1
#         if i=="u":
#             a+=1
#         if i=="e":
#             a+=1
#
#         dict_item[item]=a
#
# max_value=max(dict_item.values())
# for key, value in dict_item.items():
#     if value==max_value:
#         result=key
#
#
#
# print(f"Eng ko;'p unli harfli so'z: {result}, unlilar soni:{max_value}")


"""3-misol"""
#
# file=open("text.txt","r")
# text_read=file.read()
# text_list=text_read.split()
# file.close()
# print(text_list[-1])


"""4-misol"""
# import string
# file=open("text.txt")
# text_read=file.read()
# filter_text=''
# for i in text_read:
#     for j in i:
#         if j not in string.punctuation:
#             filter_text+=j
#
# my_list=filter_text.split()
# max_word=''
# for word in my_list:
#     if len(word)>len(max_word):
#         max_word=word
# print(max_word)
#


"""5-misol"""

file=open("text.txt","r")

last_line=file.readline()[-1]
file.close()
print(last_line)