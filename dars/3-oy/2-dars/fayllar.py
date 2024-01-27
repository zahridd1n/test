# 1 create file
# file =open('input.txt','x')
# file.close()

# 2
# file=open('input.txt','w')
# file.write('salom qalesiz !')
# file.close()

# 3
# file = open('input.txt','a')
# file.write('salom yaxshimisiz')
# file.close()

# 4
# file=open('input.txt','r')
# datas=file.read()
# print(datas)

#
# header = ['Name', 'M1 Score', 'M2 Score']
# data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
# filename = 'Student_scores.csv'
# with open(filename, 'w') as file:
#     for header in header:
#         file.write(str(header)+', ')
#     file.write('n')
#     for row in data:
#         for x in row:
#             file.write(str(x)+', ')
#         file.write('n')

# file=open('rasm.imeg','w')
# file.write('salom')

tk=input('tug\'lgan kuningizni kiriting: ')
file=open('pi_million_digits.txt')
pi=file.read()
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = pi.replace(' ','')
def tk_func(tk):
    if tk in pi:

        return True

print(tk_func(tk))
file.close()