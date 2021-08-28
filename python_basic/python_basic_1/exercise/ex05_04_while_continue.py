# in các số chẵn <n
n = int (input('Nhập n: '))
# Cách 1
# i=1
# while (i<n):
#     if i%2 == 0: 
#         print (i)
#     i+=1
# print ('Kết thúc')
# Cách 2: dùng continue
# i=1
# while i<n:
#     i+=1
#     if i%2 !=0:
#         i+=1
#         continue # bỏ qya các lệnh bên dưới, quay ngược lên kiểm tra điều kiện lặp
#     print(i)
#     i+=1
# print ("Kết thúc")

#Cách 3
i=2
while i<n:
    print(i)
    i+=2
print ('Kết thúc')