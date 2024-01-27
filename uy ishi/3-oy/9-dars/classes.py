import string
import random

class User:
    usernames=[]
    objects=[]
    def __init__(self,username,password,firs_name,last_name,age,email:str=None):
        assert self.username_validation(username)
        assert self.password_validation(password)
        self.__username=username
        self.__password=password
        self.firs_name=firs_name
        self.last_name=last_name
        self.__email=email
        self.age=age
        User.usernames.append(self.__username)
        User.objects.append((self))

    @classmethod
    def username_validation(clc,username):
        if len(username)>=8 and " " not in username and username not in clc.usernames:
            for i in username:
                if i in string.punctuation:
                    return False
            return True
        return False

    @staticmethod
    def password_validation(password):
        if len(password)>=8 and " " not in password:
            for i in password:
                if i in string.punctuation:
                    return False
            return True
        return False

    @staticmethod
    def create_token(num):
        return "".join(random.sample(string.ascii_letters+string.digits,num))

    @classmethod
    def get_all_object(cls):
        return cls.objects

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def email(self):
        return self.__email

    @username.setter
    def username(self,new_value):
        assert self.username_validation(new_value)
        self.__username=new_value

    @password.setter
    def password(self,new_value):
        assert self.password_validation(new_value)
        a=input("eski parolni kiriting:")
        if a==self.__password:
            self.__password=new_value

    @classmethod
    def login(cls, username, password):
        for user in cls.objects:
            if  password == user.__password and username == user.__username:
                return {"success":True, "token":cls.create_token(8)}

        return {"success":False}


    @classmethod
    def age_filter(cls,age,oper):
        filter_obj=[]
        for obj in cls.objects:
            if oper==">" and obj.age>age:
                 filter_obj.append(obj)

            elif oper==">=" and obj.age>=age:
                 filter_obj.append(obj)

            elif oper=="<" and obj.age<age:
                 filter_obj.append(obj)

            elif oper==">=" and obj.age>=age:
                 filter_obj.append(obj)

            elif oper=="==" and obj.age==age:
                 filter_obj.append(obj)

            elif oper=="!=" and obj.age!=age:
                 filter_obj.append(obj)

        for objage in filter_obj:
            print(objage.age)

