n = int (input('Input n:'))
S1,S2,P,P1,S5,count=0,0,1,1,0,0

for i1 in range (1,n+1,2):
    S1+=i1
for i2 in range (2,n+1,2):
    S2+=i2
for i3 in range (1,n+1,1):
    P*=i3
for i4 in range (3,n+1,3):
    P1*=i4
for i5 in range (2,n+1,1):
    for i6 in range (1,i5,1):
        if (i5%i6 ==0):
            count+=1
    if (count==1):
        S5+=i5
    count=0
print (S1,S2,P,P1,S5)
