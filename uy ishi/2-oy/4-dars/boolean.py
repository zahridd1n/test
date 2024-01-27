# bool1
# a=int(input("a soni kiriting:"))
# print("A soni musbat son:",a>0)

# bool2
# a=int(input("a sonni kiriting:"))
# b=a%2==1
# print("A soni toq son",b)

# bool3
# a=int(input("a sonni kiriting:"))
# print(f"A soni juft son: {a%2==0}")

# bool4
# a=int(input("A soni kiriting:"))
# b=int(input("B soni kiriting:"))
# c=a>2&b<=3
# print("A>2 va B<=3",c)

# bool5
# a=int(input("A soni kiriting:"))
# b=int(input("B soni kiriting:"))
# c=a>=0 and b<-2
# print("A>=0 va B<-2", c)

# bool6
# a=int(input("A soni kiriting:"))
# b=int(input("B soni kiriting:"))
# c=int(input("C soni kiriting:"))
#
# print("A<=B<=C:" + str(a<=b<=c) )

# bool7
# a=int(input("A soni kiriting:"))
# b=int(input("B soni kiriting:"))
# c=int(input("C soni kiriting:"))
#
# print("B soni A va C sonlari orasida yotadi:" + str(a<b<c or a>b>c) )

# bool8
# a=int(input("A soni kiriting:"))
# b=int(input("B soni kiriting:"))
# c=a%2==1 & b%2==1
# print('A va b sonlari toq son:'+str(c))

# bool9
# a=int(input("A soni kiriting:"))
# b=int(input("B soni kiriting:"))
# c=a%2==1 or b%2==1
# print('A va B sonlarining hech bolmagaganda 1tasi toq son:'+str(c))

# bool10
# a=int(input("A soni kiriting:"))
# b=int(input("B soni kiriting:"))
# c=(a%2==1 and b%2==0) or (a%2==0 and b%2==1)
# print('A va B sonlarining faqat bitasi toq son:'+str(c))

# bool11.
# a=int(input("A soni kiriting:"))
# b=int(input("B soni kiriting:"))
# c= (a%2==0 and b%2==0) or (a%2==1 and b%2==1)
# print(f"A va B sonlarining ha ikkalasin ham juft yoki toq: {c}")

# bool12
# a,b,c= int(input("A=")),int(input("B=")),int(input('C='))
# natija= a>0 and b>0 and c>0
# print("A,B,C sonlari musbat:",natija)

# bool13
# a,b,c= int(input("A=")),int(input("B=")),int(input('C='))
# natija= a>0 or b>0 or c>0
# print("A,B,C sonlari xech bo`lmaganda 1 tasi musbat:",natija)

# bool14
# a,b,c= int(input("A=")),int(input("B=")),int(input('C='))
# m1= (a>0 and b<0 and c<0)
# m2= (a<0 and b>0 and c<0)
# m3= (a<0 and b<0 and c>0)
# print("A,B,C sonlardan faqat bittasi musbat bo'lsin:",m1 or m2 or m3)


# bool15
# a,b,c= int(input("A=")),int(input("B=")),int(input('C='))
# m1= (a>0 and b>0 and c<0)
# m2= (a<0 and b>0 and c>0)
# m3= (a>0 and b<0 and c>0)
# print("A,B,C sonlardan faqat 2 tasi musbat bo'lsin:",m1 or m2 or m3)
#


# # bool16
# son=int(input('sonni kiriting:'))
# natija= 9<son<100 and son%2==0
# print(natija)