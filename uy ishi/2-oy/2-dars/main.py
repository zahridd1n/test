#1 capitalize()  birinchi belgini katta qilib beradi
# txt="hello,welcome word"
# print(txt.capitalize())

#2 casefold() satrni kichik harfga aylantiradi
# txt='Hello,Welcome World'
# print(txt.casefold())

#3 center() markazga ko'chiradi
# txt='banana'
# print(txt.center(50))

#4  count() berilgan qiymat satirda nechi marta ishtrok etishini  hisoblaydi
# txt='I love apples, apple my favorite fruit'
# print(txt.count("apple"))

#5 encode() satrni kodlangan versiyaga qaytaradi
# txt='My name is Zaxiriddin'
# print(txt.encode())

#6 endswith() Agar satir berilgan qiymat bilan tugasa true qiymat qaytaradi
# txt='Welcome, to my world.'
# print(txt.endswith("."))

#7 expandtabs() satrni yorliq o'lchamini o'rnatadi
# txt='H\te\tl\tl\to'
# print(txt.expandtabs(2))

#8 find() berilgan qiymat uchun satrdan qidiradi va joyini ko'rsatadi
# txt='Hello, welcome to my world'
# print(txt.find('welcome'))

#9  format() satrdagi belgilangan qiymatlarni formatlaydi
# txt='for only {price:.1f} dollars'
# print(txt.format(price=12))

# 10 index() berilgan malumotni satrdan qidirib joyini ko'rsatadi
# txt='Hello, welcome to my world.'
# print(txt.index("welcome"))

# 11 isalnum() Agar satrdagi barcha belgilar alfanumerik bo'lsa, True qiymatini qaytaradi
# txt='Company12'
# print(txt.isalnum())

#12  isalpha() satirdagi barcha elementlar alifboda bolsa true qiymat  qaytaradi
# txt='Compayny1'
# print(txt.isalpha())

#13 isascii()  Agar satrdagi barcha belgilar ascii belgilar bo'lsa, True qiymatini qaytaradi
# txt = "Company123"
# print(txt.isascii())

#14  isdecimal() Agar satrdagi barcha belgilar o'nli kasr bo'lsa, True qiymatini qaytaradi
# txt = "1234"
# print(txt.isdecimal())

#15 join() takrorolanadigann elementlarni satrga aaylantiradi
# myTuple=("John","Peter","Vicky")
# print("#".join(myTuple))

#16 ljust() berilgan miqdorda prabel tashab beradi
# txt= "banana"
# print('hello',txt.ljust(30),'is my favorite fruit.')

#17   lower() satrni kichikn harfga aylantirib beradi
# txt='Hello my FRIENDS'
# print(txt.lower())

#18 lstrip() Satrning chap trim versiyasini qaytaradi
# txt='     banana      '
# print('of all fruits '+txt.lstrip()+" is my favorite")

#19  .maketrans() Tarjimalarda foydalanish uchun tarjima jadvalini qaytaradi

# txt='Hello Sam!'
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))

#20 .partition() Satr uch qismga bo'lingan kortejni qaytaradi

# txt = "I could eat bananas all day"
# print(txt.partition("bananas"))

#21  replace() belgilangan qiymatni yangi berilgan qiymatga alishtirib berdi
# txt='I  lake  banana'
# print(txt.replace("banana","applas"))

# 22  rfind() Belgilangan qiymat uchun satrni qidiradi va u topilgan joyning oxirgi holatini qaytaradi
# txt='Mi casa, su casa'
# print(txt.rfind("casa"))

#23 rindex() Belgilangan qiymat uchun satrni qidiradi va u topilgan joyning oxirgi holatini qaytaradi
# txt='Mi casa,su casa'
# print(txt.rindex('casa'))

#24 rjust() Satrning o'ngga asoslangan versiyasini qaytaradi
# txt = "banana"
# print(txt.rjust(20), "is my favorite fruit.")

#25 .rpartition() Satr uch qismga bo'lingan kortejni qaytaradi
# txt = "I could eat bananas all day, bananas are my favorite fruit"
# print(txt.rpartition("bananas"))

# 26 rsplit() Belgilangan ajratgichda satrni ajratadi va ro'yxatni qaytaradi
# txt='apple,banana ,cherry'
# print(txt.rsplit(','))

#  27 rstr ip() Satrning o'ng trim versiyasini qaytaradi
# txt = "     banana     "
# print("of all fruits", txt.rstrip(), "is my favorite")

# 28 split() berilgan stringni so'zlarini ro'yxat qaytaradi
# txt='welcome to jungle'
# print(txt.split())

# 29 splitlines() Agar satr belgilangan qiymatdan boshlansa, true qiymatini qaytaradi
# txt='Thank you\nWelcome to the jungle'
# print(txt.splitlines())

#30  strip() Satrning kesilgan versiyasini qaytaradi
# txt = "     banana     "
# print("of all fruits", txt.strip(), "is my favorite")

# 31 title() Har bir so'zning birinchi belgisini katta harfga o'zgartiradi
# txt='Welcome to my world,'
# print(txt.title())

# 32 translate() belgini alishtiradi
# mydict = {83:  80}
# txt = "Hello Sam!"
# print(txt.translate(mydict)).

#33 upper() Satrni katta harfga aylantiradi
# txt='hello my frendsdsaad'
# print(txt.upper())

# 34 zfill() Satrni boshida belgilangan 0 qiymatlari bilan to'ldiradi
# txt = "salom"
# print(txt.zfill(10))

