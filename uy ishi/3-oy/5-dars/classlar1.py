# """1) teacher, student, guruh degan classlar yozing. u eng kamida 5ta xususiyati bo`lsin va eng kamida 3ta methodi bo`lsin."""
# """misol:1 (Teacher)"""
#
# # class Teacher:
# #     def __init__(self, ism,familya,yosh,fan,toifa):
# #         self.ism=ism
# #         self.familya=familya
# #         self.yosh=yosh
# #         self.fan=fan
# #         self.toifa=toifa
# #
# #     def tanishtir(self):
# #         return f"O'qtuvchining ismi-familyasi:{self.ism} {self.familya}, yoshi:{self.yosh} "
# #
# #     def teacher_reytingt(self):
# #         return f"o'qituvchining toifasi-> {self.toifa}"
# #
# #     def teacher_fan(self):
# #         return f"o'qituvchining dars beradigan fani->{self.fan}"
# #
# # a=Teacher(input("O'qituvchi ismi:"),
# #               input("Familyasi:"),
# #               int(input("Yoshi:")),
# #               input("Dars beradigan fani:"),
# #               input("O'qituvchi toifasi:"))
# #
# # print(a.teacher_fan())
#
#
#
# """misol:2 (Student)"""
# # class Student:
# #     def __init__(self, ism,fam,univertet,kurs,yonalish):
# #         self.ism=ism
# #         self.fam=fam
# #         self.univertet=univertet
# #         self.kurs=kurs
# #         self.yonalish=yonalish
# #
# #     def tanishtir(self):
# #         return f"Studentning ismi:{self.ism},familyasi:{self.fam},"
# #
# #     def student_univer(self):
# #         return  f"Student o'qiydigan oliygoh->{self.univertet}"
# #
# #     def student_info(self):
# #         return f'Talaba {self.yonalish} yo\'nalishida, {self.kurs}-kursda o\'qoydi'
# #
# # talaba1=Student("Zaxiriddin",'Xatamov',"TATU",2,'Kampyuter injineringi')
# #
# # print(talaba1.tanishtir())
# # print(talaba1.student_info())
#
#
# # """misol:3 (Gurruh)"""
# #
# # class Guruh:
# #     def __init__(self, nom,yonalish,son,ustoz):
# #         self.nom=nom
# #         self.yonalish=yonalish
# #         self.son=son
# #         self.ustoz=ustoz
# #
# #     def guruhinfo(self):
# #         return f"guruh nomi{self.nom},yo'nalishi:{self.yonalish}"
# #     def ustozinfo(self):
# #         return f"Ustozi ismi:{self.ustoz}"
# #     def oquvchi_soni(self):
# #         return f"o'quvchilar soni"
# #
# # guruh=Guruh("FN-9",'backend',10,"Boburjon")
#
#
# class Person:
#     __id = 0
#     yosh_list = []
#     name_list = []
#     objects_list = []
#
#     def __init__(self, ism, familya, yosh, jins):
#         Person.__id += 1
#         self.__id = Person.__id
#         self.ism = ism
#         self.familya = familya
#         self.yosh = yosh
#         self.jins = jins
#         object_list = [self.__id, self.ism, self.familya, self.yosh, self.jins]
#         Person.objects_list.append(object_list)
#         Person.yosh_list.append(self.yosh)
#         Person.name_list.append(self.ism)
#
#     @staticmethod
#     def get_id():
#         return Person.__id
#
#     def yosh_avg(self):
#         a = sum(Person.yosh_list)
#         natija = a // len(Person.yosh_list)
#         return f"O'rtacha yosh: {natija}"
#
#     def max_name(self):
#         max_leng = 0
#         max_name = ""
#         for i in Person.name_list:
#             if len(i) > max_leng:
#                 max_leng = len(i)
#                 max_name = i
#         return f"Eng uzun ism: {max_name}"
#
#     def min_name(self):
#         min_leng = float('inf')
#         min_name = ""
#         for i in Person.name_list:
#             if len(i) < min_leng:
#                 min_leng = len(i)
#                 min_name = i
#         return f"Eng qisqa ism: {min_name}"
#
#
#      def age_filter(self, inpyosh, belgi):
#         filter_obj = []
#         for i in Person.objects_list:
#             if len(i) >= 4:
#                 if belgi == ">" and i[3] > inpyosh:
#                     filter_obj.append(i)
#                 elif belgi == "<" and i[3] < inpyosh:
#                     filter_obj.append(i)
#                 elif belgi == ">=" and i[3] >= inpyosh:
#                     filter_obj.append(i)
#                 elif belgi == "<=" and i[3] <= inpyosh:
#                     filter_obj.append(i)
#                 elif belgi == "==" and i[3] == inpyosh:
#                     filter_obj.append(i)
#                 elif belgi == "!=" and i[3] != inpyosh:
#                     filter_obj.append(i)
#         return filter_obj
#
#
# person3 = Person("Ali", "Anvarov", 30, "erkak")
# person1 = Person("Zaxiriddin", "Xatamov", 20, "erkak")
# person2 = Person("Javohir", "odilov", 22, "erkak")
# person4 = Person("Aziz", "komilov", 10, "erkak")
#
# print(Person.yosh_avg(Person.yosh_list))
# print(Person.max_name(Person.name_list))
# print(Person.min_name(Person.name_list))
# print(Person.age_filter(Person.objects_list,20,">"))
