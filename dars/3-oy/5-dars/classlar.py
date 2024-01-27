# class Telefon:
#     def __init__(self, company, model):
#         self.company=company
#         self.model=model
#
#     def tanishtir(self):
#         return f"model:{self.model},company:{self.company}"
#
# tel1=Telefon('mi','redmi12')
# tel1=Telefon('mi','redmi12')
# tel1=Telefon('mi','redmi12')
# tel1=Telefon('mi','redmi12')

class User:
    def __init__(self, username,password,ism,familya,tyil,emil):
        self.username=username
        self.password=password
        self.ism=ism
        self.familya=familya
        self.tyil=tyil
        self.email=emil

    def get_yosh(self ,yil):
        return yil-self.tyil
    def get_info(self):
        return f""

user1=User("zahridd1n","zahri1118","Zaxiriddin","Xatamov",2004,"hatamovz047786@gmail.com")
# print(user1.get_yosh())