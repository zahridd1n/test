# data={'rang':'oq','son':12}

# print(data.keys())
# print(data.values())
# print(data.items())

# for key in data.keys():
#     print(key)

# for valuee in data.values():
#     print(valuee)

narx_j = {1:5000,2:4000,3:3000}
narx_y = {1:4000,2:3000,3:2000}
avto_j = {}
avto_y = {}
n = 1
while True:
    raqaminp = input('Avtomabil raqamini kiriting(dastur to\'xtashi uchun stop kiriting):')

    def j_sh(raqaminp):
        success1 = False
        if len(raqaminp) == 8:
            if raqaminp[:2].isdigit() and raqaminp[2].isupper() and raqaminp[3:6].isdigit() and raqaminp.isupper():
                success1 = True
        return success1
    
    def y_sh(raqaminp):
        success1 = False
        if len(raqaminp) == 8 and raqaminp[:5].isdigit() and raqaminp[5:].isupper():
            success1 = True
        return success1
    
    if j_sh(raqaminp):
        if avto_j.get(raqaminp, ''):
            n += 1
            avto_j[raqaminp] = n
        else:
            n = 1 
            avto_j[raqaminp] = n
    elif y_sh(raqaminp):
       if avto_y.get(raqaminp, ''):
           n += 1
           avto_y[raqaminp] = n
       else:
           n = 1
           avto_y[raqaminp] = n

    if raqaminp == 'stop':
        break
        
print(avto_j)
