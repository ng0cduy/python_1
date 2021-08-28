n = int(input('input a power integer n:\n'))
i = 1
count =0
while (i<=n):
    if n % i ==0:
        count +=1
    i+=1  
if (count>2):
    print ('%d không phải là số nguyên tố!' %n)
else:
    print ('%d là số nguyên tố!' %n)
