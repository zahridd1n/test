# misol1
# shcool={
#     'number':"49",
#     'pupil':350,
#     'region':'Fergana',
#     'steeps':[
#         {
#             'steep':1,
#             'calass_n':3,
#             'calsses':[
#                 {
#                     'class':'A',
#                     'pupil':30
#                 },
#                 {
#                     'class':"B",
#                     'pupil':40
#                 },
#                 {
#                     'class':'C',
#                     'pupil':30
#                 }
#             ]
#         },
#         {
#             'steep':2,
#             'class_n':1,
#             'classes':[
#                 {
#                     'class':'A',
#                     'pupil':25
#                 }
#             ]
#         },
#         {
#             'steep':3,
#             'class_n':2,
#             "classes":[
#                 {
#                     'class':"A",
#                     'pupil':35
#                 },
#                 {
#                     'class':'B',
#                     'pupil':20
#                 },
#                 {
#                     'class':'C',
#                     'pupil':20
#                 }
#             ]
#         },
#         {
#
#             'steep':4,
#             'class_n':4,
#             'claasses':[
#                 {
#                     'class':'A',
#                     'pupil':45
#                 },
#                 {
#                     'class':'B',
#                     'pupil':30
#                 },
#                 {
#                     'class':'C',
#                     'pupil':35
#                 },
#                 {
#                     'class':'D',
#                     'pupil':40
#                 }
#             ]
#         }
#     ]
# }
# for k,v in shcool.items():
#     if isinstance(v, (str, int, float, bool)):
#         print(f"{k}->{v}")
#
#     else:
#         for vsteep in v:
#             print()
#             for k2,v2 in vsteep.items():
#
#                 if isinstance(v2,(str,int,float,bool)):
#                     print(f"    {k2}->{v2}")
#                 else:
#                     for vclasses in v2:
#                         print()
#                         for k3,v3 in vclasses.items():
#                             print(f"        {k3}->{v3}")
#
#

# misol2
stopinfo=True
narx_j = {1:5000,2:4000,3:3000}
narx_y = {1:4000,2:3000,3:2000}
avto_j={}
avto_y={}
n,m=1,1
cauntj,caunty = 0,0

def j_sh(raqamin):
    success1 = False
    if len(raqaminp) == 8:
        if raqamin[:2].isdigit() and raqamin[2].isupper() and raqamin[3:6].isdigit() and raqamin.isupper():
            success1 = True
    return success1


def y_sh(raqamin):
    success1 = False
    if len(raqamin) == 8 and raqamin[:5].isdigit() and raqamin[5:].isupper():
        success1 = True
    return success1

while stopinfo:
    raqaminp=input('Avtomabil raqamini kiriting(dastur to\'xtashi uchun stop kiriting):')


    if j_sh(raqaminp):

        if avto_j.get(raqaminp, ''):
            n += 1
            avto_j[raqaminp] = n
        else:
            n = 1
            avto_j[raqaminp] = n
        cauntj+=1
    elif y_sh(raqaminp):

       if avto_y.get(raqaminp, ''):
           m += 1
           avto_y[raqaminp] = m
       else:
           m = 1
           avto_y[raqaminp] = m
       caunty += 1

    if raqaminp=='stop':
        stopinfo=False


a,b=0,0

for i in avto_j.values():
    a+=1

for j in avto_y.values():
    b+=1

print('Avtomabillar soni:',a+b)
print('tashriflar  soni:',caunty+cauntj)



