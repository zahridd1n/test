# class Product:
#     def __init__(self,name,quantity):
#         self.name=name
#         self.quantity=quantity
#
#     def __add__(self, other):
#         if isinstance(other,str):
#             result= self.name+other
#         elif isinstance(other,(int,float)):
#             result=self.quantity+other
#         else:
#             raise TypeError("xato")
#
#         return result
#
#
#     def __str__(self):
#         return f"maxsulot nomi{self.name}"
#
#     def __int__(self):
#         return self.quantity
#
#     def __len__(self):
#         return len(self.name)
#
# p=Product('pepsi',12)

# print(p+"salom")
# print(p+1)

# print(str(p))
# print(p)

# print(len(p))


