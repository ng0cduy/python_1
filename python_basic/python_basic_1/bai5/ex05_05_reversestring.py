str1=input('Input a string: ')
newstr=''
strlen = len(str1)
while (strlen>0):
    newstr +=str1[strlen-1]
    strlen-=1
print (newstr)