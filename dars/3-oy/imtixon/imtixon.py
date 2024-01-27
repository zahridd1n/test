"""5) Teacher degan class yozing. ushbu classga f_name, l_name, email, subject degan xususiyatlari bo`lsin va
emailni yagonalikga tekshiring (email degan xususiyat bu classni obyektlarida bo`lmasligi kerak). unga quyidagicha methodlar yozing.
1) get_info - obyektga tegishlik ma`lumotlarni dict typeda qaytarib bersin,
2) get_info_txt obyektga tegishlik ma`lumotlarni txt faylga yozib bersin
(10-ball)"""

# class Teacher:
#     obj_email=[]
#     @classmethod
#     def email_chek(cls,email):
#         if email not in cls.obj_email:
#             return True
#
#
#     def __init__(self, f_name, l_name,email,subject):
#         if Teacher.email_chek(email):
#             self.f_name=f_name
#             self.l_name=l_name
#             self.email=email
#             self.subject=subject
#             Teacher.obj_email.append(self.email)
#
#         else:
#             raise TypeError("bunday email mavjud")
#
#
#     def get_info(self):
#         teach_dict={
#             "ism":self.f_name,
#             "familya":self.l_name,
#             "email":self.email,
#             "subject":self.subject
#         }
#         return teach_dict
#
#     def get_info_txt(self):
#         file=open("text.txt","w")
#         a=f"ism:{self.f_name}, familya:{self.l_name},email:{self.email} \n"
#         file.write(a)
#         file.close()
#
#
# teacher_1=Teacher("Zaxiriddin","Xatamov","hatamovz047786@gmail.com","Math")
# print(teacher_1.get_info())
# teacher_1.get_info_txt()


class Product:
    obj=[]
    def __init__(self,name,quantity,is_sale:bool):
        self.name=name
        self.quantity=quantity
        self.is_sale=is_sale
        Product.obj.append(self)

    @classmethod
    def get_all_products(cls):
        mylist = []
        for i in cls.obj:


            a={"name":i.name,
             "quantity":i.quantity,
             "is_sale":i.is_sale
             }

            mylist.append(a)
        mylist=tuple(mylist)
        return mylist

    @classmethod
    def is_sale_products(cls):
        sale_list=[]
        for j in cls.obj:
            if j.is_sale==True:
                b = {"name": j.name,
                     "quantity": j.quantity,
                     "is_sale": j.is_sale
                     }
                sale_list.append(b)
        sale_list=tuple(sale_list)
        return sale_list

product_1=Product("Mishka",10,True)
product_2=Product("Manitor",2,False)

print(Product.get_all_products())
print(Product.is_sale_products())