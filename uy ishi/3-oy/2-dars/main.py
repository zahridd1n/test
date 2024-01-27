import csv

studentlist=[]
soni=int(input('talabalar soninin kiriting:'))
for i in range(soni):
    studentlar = {
        'tr': i + 1,
        'ism': input('talaba ismini kiriting:').capitalize(),
        'familya': input('talaba familyasini kiriting:').capitalize(),
        'otasining ismi': input('talaba otasining ismini kiriting:'),
        'jinsi': input('talaba jinsi:'),
        'tug\'lgan kuni':input('tug\'lgan kuni kiriting:'),
        'kursi': input('talaba nechani kurs:'),
        'tolov shakli': input('talaba grantmi yoki kontrakt:')
    }
    studentlist.append(studentlar)

# for j in studentlist:
#     print(j)

file=open('studentlar.csv','w')

keys=tuple(studentlar.keys())
values=[]
for d in studentlist:
    values.append(tuple(d.values()))

writer=csv.writer(file)
writer.writerow(keys)
for value in values:
    writer.writerow(value)
file.close()


