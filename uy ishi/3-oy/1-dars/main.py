from random import choice
start=input('o\'yin boshlanishi uchun start bosin:')
if 'start'==start:
    # a=[i for i in range(1,101)]
    print(choice([i for i in range(1,101)]))
else:
    print("o'yin boshlanish buyrug'i berilmadi ")