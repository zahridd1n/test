file=open("products.txt","w")

class Product:

    def __init__(self,product):
        self.product=product
        self.a=[]
        self.a.append(self.product)

class Category:

    def __init__(self,name,brand,quantity,price):
        self.name=name
        self.brand=brand
        self.quantity=quantity
        self.price=price
        self.price_list=[]
        self.quantity_list=[]
        self.quantity_list.append(self.quantity)
        self.price_list.append(self.price)


    def tanishtir(self):
        return f"Maxsulot nomi:{self.name}, Brand:{self.brand}, narxi:{self.price}, Soni;{self.quantity}"

    def kam_somli_maxsulot(self):
        return f"eng kam sonli maxsulot {min(self.quantity_list)}"

    def eng_qimat_maxsulot(self):
        return f"eng qimat maxsulot:{max(self.price_list)} "
    def eng_arzon_maxsulot(self):
        return f"eng arzon maxsulot: {min(self.price_list)}"


products=[]

for i in range(int(input("nechta maxsulot kiritimoqchisiz:"))):
    p_name=input("Maxsulot nomini kiriting:")
    p_brand=input("Maxsulot Brend nomini kiriting:")
    p_quantity=int(input("maxsulo soni:"))
    p_price=float(input("1 ta maxsulot narxi:"))
    obj=Category(p_name,p_brand,p_quantity,p_price)
    products.append(obj)


for product in products:
    file.write(str(product))
    p1=Product(product)
while True:
    print("1:maxsulotni tanishtirish")
    print("2:eng arzon maxsulot")
    print("3:eng qimat maxsulot")
    print("4:eng kam sonli maxsulot")
    categoryinp=input("qaysi categoryani tanlaysiz (to'xtash uchun stop deb yozing)")

    if categoryinp=='1':
        for product in products:
            print(Category.tanishtir(product))

    elif categoryinp=="2":
        print(Category.eng_arzon_maxsulot(obj))

    elif categoryinp=="3":
        print(Category.eng_qimat_maxsulot(obj))

    elif categoryinp=="4":
        print(Category.kam_somli_maxsulot(obj))

    elif categoryinp=="stop":
        break


