# mylist=[1,2,3,4,5,6]
#
# def revers_func(mylist):
#     newlist = []
#     index=1
#     for i in range(len(mylist)):
#       if i%2==0:
#           newlist.append(mylist[i+1])
#           newlist.append(mylist[i])
#     return newlist
# print(revers_func(mylist))


#
# def fumc(text,index):
#     count=0
#     for i in text:
#
#          if index==count:
#             a=i
#          count+=1
#     return a
#
# print(fumc("salom",2))



def func(text,index):

    for counter,element in enumerate(text):

        if element==index:
            return counter
    # return result

print(func("Zaxiriddin","a"))
