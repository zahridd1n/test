"""2) darsda yozgan user classiga login uchun method yozing, u method o`zida qabul qilayotgan username va password bilan classdan
 obyekt olingan bo`lsa session_id aks xolda bunday foydalanuvchi yo`q degan xatolik qaytarsin
"""
import string
import random

class User:
    usernames = []
    usersdict = {}
    def username_validatsiya(self, username:str):
        if username not in User.usernames and " " not in username and username.isascii():
            return True
        else:
            return False
    def password_validaatsiya(self,password:str):
        if len(password)>=8 and " " not in password and  password.isascii():
            return True
        else:
            return False

    def __init__(self, usernameinp,passwordinp,name,telnumber):
        if self.username_validatsiya(usernameinp):
            if self.password_validaatsiya(passwordinp):
                self.username=usernameinp
                self.password=passwordinp
                self.name=name
                self.telnumber=telnumber
                User.usersdict[self.username]=self.password
            else:
                raise ValueError("Parol xato farmatda kiritildi:")
        else:
            raise ValueError("Username xato farmatda kiritildi")


    def session(self):
        datas=string.ascii_letters+string.digits
        random_session=random.sample(datas,8)
        return  "".join(random_session)

    def login(self, username1, password1):
        self.username1 = username1
        self.password1 = password1
        if self.username1 in User.usersdict and User.usersdict[self.username1] == self.password1:
            return self.session()
        else:
            return "foydalanuvchi topilmadi"



a=User("zahriddin","Zaxiriddin","Zaxiriddin",907862817)
print(a.login("zahriddin","Zaxiriddin"))


# a=User.(
#     input("Username kiriting:"),
#     input("Password kiriting:"),
#     input("Ismingizni kiriting:"),
#     input("Telefon raqam kiriting:")
# )

