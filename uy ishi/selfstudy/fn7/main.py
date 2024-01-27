# class Paymet:
#     @staticmethod
#     def check_card_number(card_number):
#         if card_number.isdigit() and len(card_number)==16:
#             return True
#
#
#
# class Bank(Paymet):
#     def __init__(self,card_number,money):
#         assert Paymet.check_card_number(card_number)
#         self.card_number=card_number
#         self.money=money
#
#     def exchange(self):
#         kurs=12500
#         natija=self.money*kurs
#         return natija
#
#
# cilent=Bank("8600000112345678",200)
# print(cilent.exchange())


"""2-misol"""
class User:
    user_obj=[]
    @staticmethod
    def info_chek(info:str):
        info_list=info.split()
        if len(info_list)==4 and info_list[3]=="o'g'li" or info_list[3]=="qizi":
            return True

    @classmethod
    def tel_nummber_chek(cls,tel_number:str):
        if tel_number[:4]=="+998" and len(tel_number)==13:
            return True


    def __init__(self,info,tel_number):
        if User.info_chek(info):
            if User.tel_nummber_chek(tel_number):
                self.info=info
                self.tel_mnumber=tel_number
                self.user_obj.append(self)
            else:
                raise Exception("telefon raqam xato")
        else:
            raise Exception("malumot xato kiritilgan")

    def description(self):
        if self.tel_mnumber[4:6]=="90" or self.tel_mnumber[4:6]=="91":
            result=f"{self.info} Beeline foydalanuvchisi"
        elif self.tel_mnumber[4:6]=="93" or self.tel_mnumber[4:6]=="94" or self.tel_mnumber[4:6]=="50":
            result=f"{self.info} Usell foydalanuvchisi"
        elif self.tel_mnumber[4:6]=="95" or self.tel_mnumber[4:6]=="99":
            result=f"{self.info} Uzmobile foydalanuvchisi"
        elif self.tel_mnumber[4:6]=="97" or self.tel_mnumber[4:6]=="88":
            result=f"{self.info} Mobiuz foydalanuvchisi"
        if self.tel_mnumber[4:6]=="33" :
            result=f"{self.info} Humans foydalanuvchisi"
        return result


user_1=User("Zaxiriddin Xatamov Nosirjon o'g'li","+998907862817")
user_2=User("Jumaboy Nematov Ibrohim o'g'li","+998971862817")
user_3=User("Diyora Odilbekova Ulug'bek qizi","+998999977150")
user_4=User("Umarjonn Xatamov Nosirjon o'g'li","+998931697786")
user_5=User("kimsanov kimsan kimdur o'g'li","+998907862810")
print(user_1.description())
print(user_2.description())
print(user_3.description())
print(user_4.description())
print(user_5.description())