n = int(input('input a power integer n:\n'))
S1,S2,S3,S4=0,0,1,1
i=0
while (i<=n):
    if (i%2==0):
        S2+= i
    else:
        S1+=i
    i+=1
    if (i%3 ==0):
        S4 *=i
    if (i<=n):
        S3*=i

print (S1)
print (S2)  
print (S3)  
print (S4)