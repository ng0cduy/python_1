lstN=[8,15,20,5]
# P=1
# for item in lstN:
#     P*=item
# print (P)

#chuyen thanh chuoi strN voi gia tri cua moi phan tu cach nhau 1 dau phay
# strN=''
# for item in lstN:
#     strN+=str(item)+','
# print (strN.rstrip(','))
# in theo mẫu : index --> giá trị
#cách 1:
# i=0
# for item in lstN:
#     s=f'{i} --> {item}'
#     print (s)
#     i+=1
#print ('_'*50)

#cách 2:
# tongSPT= len(lstN)
# for i in range(0,tongSPT,1):
#     s = f'{i} -->{lstN[i]}'
#     print (s)
# print ('_'*50)
# cách 3:
# i=0
# while (i<len(lstN)):
#     item=lstN[i]
#     s=f'{i+1} --> {item}'
#     print(s)
#     i+=1
