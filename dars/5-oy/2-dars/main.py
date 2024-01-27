# def check(data):
#     result=0
#     for i in data:
#         if i == '(':
#             result+=1
#         elif i == ')':
#             result-=1
#         elif ')' !=i and '('!=i and result<0:
#             result=-100
#             break
#     return result==0
#
#
# a=input('malumot kiriting:')
# print(check(data=a))


def matrix(data):
    a,b,c,d='','','',''
    if len(data)==3 and len(data[0])==len(data[1]) and len(data[0])==len(data[2]):
        for i in data[0]:
            a+=str(i)

        b=str(data[1][-1])

        data2=data[2]

        data2.reverse()
        for j in data2:
            c+=str(j)
        data1=data[1][:-1]

        for z in data1:
            d+=str(z)
    return f"{a}{b}{c}{d}"




a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print(matrix(a))



















