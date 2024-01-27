"""meroslanish"""
import time


class Person:
    def __init__(self, ism, fam):
        self.ism=ism
        self.fam=fam
    def tanistir(self):
        return f"ism:{self.ism}"




class Teacher(Person):
    def __init__(self,ism,fam,tajriba):
        Person.__init__(self,ism,fam)
        self.tajriba=tajriba
        self.students=[]

    def teacher_tanishtir(self):
        return f"O'qituvchinig  ismi-familyasi: {self.ism.title()} {self.fam.capitalize()},tajriba {self.tajriba} yil"

    # def dars(self):
    #     print('dars boshlandi ')
    #     time.sleep(2)
    #     print('dars bo\'lyapti')
    #     time.sleep(2)
    #     print('dars tugadi')


class Student(Person):
    def __init__(self,ism,fam,universitet,yosh,jinsi):
        Person.__init__(self,ism,fam)
        self.universitet=universitet
        self.yosh=yosh
        self.jinsi=jinsi

    def student_tanishtir(self):
        return f"O'quvchinig  ismi-familyasi: {self.ism.title()} {self.fam.capitalize()},universtiteti:{self.universitet}, yoshi:{self.yosh},jinsi:{self.jinsi}"

