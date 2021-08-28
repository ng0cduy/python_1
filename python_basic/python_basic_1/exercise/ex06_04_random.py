import random
# phát một số (thực) ngẫu nhiên trong miền [0,1)
n1=random.random()
print(n1)
# Một số thực ngẫu nhiên trong khoảng >x và <y
x,y=10,20
n4=random.uniform(x,y)
 
# phát một số nguyên ngẫu nhiên từ 10 đến 15 với step=1
n2=random.randrange(10,16) # start,stop
print(n2)
 
n3=random.randrange(10,16,1) # start,stop,step
print(n3)
 
# phát một số nguyên ngẫu nhiên từ 10 đến 15
n4=random.randint(10,15)