from abc import ABC,abstractmethod
class Bino(ABC):
    # @abstractmethod
    def __init__(self,name,lacation):
        self.name=name
        self.lacation=lacation


class Sinf(Bino):
    def chek_sinf(self,quantity_student):
        self.quantity=quantity_student

        if self.quantity<8:
            raise SyntaxError("talabalar soni kam")
        else:
            return "talablar yetaarli"

class Qabul(Bino):
    ...


class Tolov(Bino):
    pass


a=Sinf("nt","fergana")


print(a.chek_sinf(9))