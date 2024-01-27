import func



"""item jadvali uchun"""
# items = list(func.take_data('item'))
# for item in items:
#     user = func.take_data('ads_user', 'id', item['author_id'])[0]
#     del item['author_id']
#     item['author'] = user
#     category=func.take_data('category','id', item['category_id'])[0]
#     del item['category_id']
#     item['category']=category
#     print(item, '\n')

"""item_review jadvali uchun"""
# item_review=list(func.take_data('item_review'))
# for i in item_review:
#     user=func.take_data('ads_user','id',i['user_id'])
#     del i['user_id']
#     i['user']=userp
#     item=func.take_data('item','id',i['item_id'])
#     del i['item_id']
#     i['item']=item
#
#     print(i)
while True:
    son=int(input('Sonni kiriting:'))
    s=str(son)
    if len(s)==3:

        print(s[::-1])