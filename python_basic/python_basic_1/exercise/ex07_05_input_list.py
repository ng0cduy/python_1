lstN=[]
i=0
n=int(input("Input N:\t"))
if n<0:
    print ('Error!')
else:
    while (i<n):
        m=int(input('Input value %d:\t'%(i+1)))
        lstN.append(m)
        i+=1
    print ('List input: ',lstN)
print("END!")