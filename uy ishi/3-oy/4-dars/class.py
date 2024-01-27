class Shaxs:
    def __init__(self,ism,fam,yosh,manzil):
        self.ism=ism
        self.fam=fam
        self.yosh=yosh
        self.manzil=manzil

    def tanishtir(self):
        return f"{self.ism} {self.fam} {self.yosh} yoshda, Yashah manzili {self.manzil}"
shaxsList=[]
n=int(input('shaxslar sonini kiriting:'))
for i in range(n):
    shaxsList.append(Shaxs(input('Ism:'), input('Familya:'), int(input('yosh:')), input('manzil:')))


# a=list(filter(lambda ,))
for shaxs in shaxsList:
    if shaxs.yosh>15:
        print(shaxs.tanishtir())