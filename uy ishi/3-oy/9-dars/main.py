import classes

user1=classes.User("zahridd1n","Zaxiriddin04","Zaxiriddin","Xatamov",19,"hatamovz047786@gmail.com")
user2=classes.User("Dilmurod12","Dili1212","Dilmurod","Mamaro'ziyev",29,"dili12@gmail.com")

# user1.password="xaker7786"
# print(user1.password)


# data = classes.User.login('zahridd1n', 'Zaxiriddin04')
# if data['success']:
#     print(f"Dasturga xush kelibsiz, sizning tokeningiz {data['token']}")
# else:
#     print('Xato ma`lumot kiritdingiz ')



classes.User.age_filter(19,">=")