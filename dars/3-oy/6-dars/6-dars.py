class Persson:
    __id=0
    yoshlist=[]
    def __init__(self,ism,fam,yosh):
        Persson.__id= Persson.__id + 1
        self.__id=Persson.__id
        self.ism=ism
        self.fam=fam
        self.yosh=yosh
        Persson.yoshlist.append(self.yosh)
    def id_get(self):
        return self.id_get()

    def avg(self):
       return sum(Persson.yoshlist)/len(Persson.yoshlist)



person1=Persson("Zaxiriddin","Xatamov",20)
person2=Persson("Javohir","odilov",22)

print(Persson.avg())