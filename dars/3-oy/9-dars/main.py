class Transport:
    @staticmethod
    def km_hisobla(hour,speed):
        return hour*speed

class Avto(Transport):
    pass


class Moto(Transport):
    pass

moto1 = Moto()
print(moto1.km_hisobla(10,10))
