#if1
son=int(input("Sonni kiriting:"))
if son>0:
    print(son+1)
else:
    print(son)


# if2
# son=input("sonni kiriting:")
# son=int(son)
# if son>0:
#     print(son+1)
# else:
#     print(son-2)
#

#if3
# son=int(input("Son kiriting:"))
# if son>0:
#     print(son+1)
# elif son<0:
#     print(son-2)
# else:
#     son = 10
#     print(son)


# if4
# son1,son2,son3=int(input("1-son:")),int(input("2-son:")),int(input("3-son:"))
# musbatSon=0
# if son1>0:
#     musbatSon+=1
# if son2>0:
#     musbatSon+=1
# if son3>0:
#     musbatSon+=1
# print(musbatSon)

# if5
# son1=int(input("1-son:"))
# son2=int(input("2-son:"))
# son3=int(input('3-son:'))
# musbatSon, manfiySon  =   0,0
# if son1>0:
#     musbatSon+=1
# elif son1<0:
#     manfiySon+=1
#
# if son2>0:
#     musbatSon+=1
# elif son2<0:
#     manfiySon+=1
#
# if son3>0:
#     musbatSon+=1
# elif son3<0:
#     manfiySon+=1
# print(f"Manfiy son {manfiySon} ta, Musbat son {musbatSon} ta")

# if6
# son1,son2 =int(input("1-son:")),int(input("2-son:"))
# if son1>son2:
#     print(f"Kattasi {son1}")
# else:
#     print(f"Kattasi {son2}")

# if7
# son1,son2 =int(input("1-son:")),int(input("2-son:"))
# if son1<son2:
#     print(1)
# else:
#     print(2)

# if8
# son1,son2 =int(input("1-son:")),int(input("2-son:"))
# if son1>son2:
#     print(f"Kattasi {son1}, Kichigi {son2}")
# else:
#     print(f"Kattasi {son2}, Kichigi {son1}")

# if9
# a,b= int(input("A=")),int(input("B="))
# if b>a:
#      print('A=',a ,'B=',b )
# else:
#     print('A=', b ,"B=",a)

# if10
# a,b= int(input("A=")),int(input("B="))
# if a != b :
#     print('A=',a+b ,'B=',b+a )
# else:
#     print('A=', 0  ,' ', 'B=',0)

# if11
# a,b=int(input("A=")),int(input('B='))
# if a!=b:
#     if a>b:
#         print(f"A={a}, B={a}")
#     else:
#         print(f"A={b}, B={b}")
# else:
#     prin(f"A=0, B=0")

# if12
# son1,son2,son3=int(input("1-son:")),int(input("2-son:")),int(input("3-son:"))
# if son1>=son2>=son3 or son2>=son1>=son3:
#     print('kichigi=',son3)
# elif son1>=son3>=son2 or son3>son1>son2:
#     print('kichigi=',son2)
# else:
#     print('kichigi=',son1)

# if13
# son1,son2,son3=int(input("1-son:")),int(input("2-son:")),int(input("3-son:"))
# if son1>son2>son3 or son3>son2>son1:
#     print(f"o'rtancha son=",son2)
# elif son2>son1>son3 or son3>son1>son2:
#     print(f"o'rtancha son=",son1)
# else:
#      print(f"o'rtancha son=",son3)

# if14
# son1,son2,son3=int(input("1-son:")),int(input("2-son:")),int(input("3-son:"))
# if son1>son2>son3:
#     print('kichigi=',son3,'kottasi=',son1)
# elif son3>son2>son1:
#     print('kichigi=',son1,'kottasi=',son3)
# elif son2>son1>son3:
#     print('kichigi=',son3,'kottasi=',son2)
# elif son3>son1>son2:
#     print('kichigi=',son2,'kottasi=',son3)
# elif son1>son3>son2:
#     print('kichigi=',son2,'kottasi=',son1)
# else:
#      print('kichigi=',son1,'kottasi=',son2)

# if15
# son1,son2,son3=int(input("1-son:")),int(input("2-son:")),int(input("3-son:"))
# if son1>son2>son3 or son2>son1>son3:
#    print(son1+son2)
# elif son1>son3>son2 or son3>son1>son2:
#    print(son1+son3)
# else:
#    print(son2+son3)