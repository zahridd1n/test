import csv
# avtosoni=int(input('avto yoki user sonini kiritinng:'))
# carsList=[]
# usersList=[]
# for i in range(avtosoni):
#     cars={
#         'id':i+1,
#         'Modeli':input('Avtomabil modelini:').capitalize(),
#         'Rangi':input('Avtomabil rangi:'),
#         'Yili':input('Avtomabilning yili:'),
#         'Xolati':input('Avtomabil xolati:'),
#         'Mator Xajmi':input('Avto mantor hajmi:'),
#         'Uzatmalar qutisi':input('Mexanika yoki Avtomat?:')
#     }
#     carsList.append(cars)
#
#     users={
#         'id':i+1,
#         'Ism':input("Foydalanuvchi ismi? ").capitalize(),
#         'Familyasi':input('Foydalanuvchi familyasi? ').capitalize(),
#         'Millati':input('foydalanuvchi millati:'),
#         'Yoshi':input('foydalanuvchi yoshi:'),
#         'kaspi':input('foydalanuvchi kaspi:'),
#         'Avtomabili':cars['id']
#     }
#     usersList.append(users)
#
# # print(usersList)
# avtoKeys=tuple(cars.keys())
# avtoValues=[]
# for i in carsList:
#     avtoValues.append(tuple(i.values()))
#
# userKeys=tuple(users.keys())
# userValues=[]
# for j in usersList:
#     userValues.append(tuple(j.values()))
#
# avtoFile=open('Avto.csv','w')
# writer=csv.writer(avtoFile)
# writer.writerow(avtoKeys)
# for avalue in avtoValues:
#     writer.writerow(avalue)
# avtoFile.close()
#
# userFile=open('User.csv','w')
# writer2=csv.writer(userFile)
# writer2.writerow(userKeys)
# for uvalue in userValues:
#     writer2.writerow(uvalue)
# userFile.close()
#
#
from abc import ABC, abstractmethod

class OS(ABC):
    def init(self, os_name, version, year_issue):
        self.os_name = os_name
        self.version = version
        self.year_issue = year_issue

    @abstractmethod
    def os_name(self):
        pass

    @abstractmethod
    def version(self):
        pass

    @abstractmethod
    def year_issue(self):
        pass

class Linux(OS):
    def init(self, os_name, version, year_issue):
        super().init(os_name, version, year_issue)

    def os_name(self):
        return f'linux_name: {self.os_name}'

    def version(self):
        return f'version: {self.version}'

    def year_issue(self):
        return f'year_issue: {self.year_issue}'
class Mac(OS):
    def init(self, os_name, version, year_issue):
        super().init(os_name, version, year_issue)

    def os_name(self):
        return f'mac_name: {self.os_name}'

    def version(self):
        return f'version: {self.version}'

    def year_issue(self):
        return f'year_issue: {self.year_issue}'

class Win(OS):
    def init(self, os_name, version, year_issue):
        super().init(os_name, version, year_issue)

    def os_name(self):
        return f'win_name: {self.os_name}'
    def version(self):
        return f'version: {self.version}'

    def year_issue(self):
        return f'year_issue: {self.year_issue}'

a = str(input('Hozirda bizda bor kompyuterlar(linux/mac/win): '))
key =  ['os_name', 'version', 'year_issue']
values=[]
if a == 'linux':
    os_name = str(input('OS kiriting: '))
    version = str(input('Version kiriting: '))
    year_issue = str(input('Year_issue kiriting: '))
    print('Faylga yozildi')
    value=[os_name, version, year_issue]
    values.append(value)
elif a == 'mac':
    os_name = str(input('OS kiriting: '))
    version = str(input('Version kiriting: '))
    year_issue = str(input('Year_issue kiriting: '))
    print('Faylga yozildi')
    value=[os_name, version, year_issue]
    values.append(value)

elif a == 'win':
    os_name = str(input('OS kiriting: '))
    version = str(input('Version kiriting: '))
    year_issue = str(input('Year_issue kiriting: '))
    value=[os_name, version, year_issue]
    values.append(value)
    print('Faylga yozildi')
else:
    print('Bizda siz qidirgan kompyuter yoq')
file=open('comp.csv','w')
writer=csv.writer(file)
writer.writerow(key)




file=open('comp.csv','a')
writer=csv.writer(file)

for j in values:
    writer.writerow(j)
file.close()
