a,b,c,d = eval(input("Nhập 4 giá trị a b c d: "))
print('a,b,c,d=',a,b,c,d)
gtln =a
gtnn =a
# Tìm Max
if (b>gtln):
    gtln=b
    gtnn=b
if (c>gtln):
    gtln=c
    gtnn=c
if (d>gtln):
    gtln=d
    gtnn=d
# Tìm Min
if  (b<gtnn):
    gtnn=b
if  (c<gtnn):
    gtnn=c
if  (d<gtnn):
    gtnn=d
print ("Max value: ",gtln)
print ("Min value: ",gtnn)