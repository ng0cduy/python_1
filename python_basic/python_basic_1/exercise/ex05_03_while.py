#1-in dãy số tự nhiên từ 1 đến n
# n = int (input("Nhập số n: "))
# i=1
# while (i<=n):
#     print('số là %d' %i)
#     i+=1
# print("Kết thúc")
    
#2 - Tính tổng dãy số tự nhiên từ 1 đến N
# n= int (input("Nhập n: "))
# S,i=0,0
# while (i<n):
#     i+=1
#     S+=i
#     # P*=i
# print (S)


#3- Tính tích dãy số từ 1 đến N (N!)
n= int (input("Nhập n: "))
P,i=1,0
while (i<n):
    i+=1
    P*=i
    # P*=i
print ('%d! là %d '%(n,P))


