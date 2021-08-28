count = int(input('Input an integer number:'))
i = 0
s0 = 0
s1 = 1
print (s0)
print (s1)
while (i<count-2):
    s2=s1+s0
    s0=s1
    s1=s2
    i+=1
    print (s2)
    
