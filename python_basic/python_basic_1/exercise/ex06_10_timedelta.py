from datetime import timedelta,datetime,date
 
# Tính chênh lệch theo ngày và giây
d1=datetime(1998,4,11,7,30,00)
d2=datetime(2019,12,30,8,32,20)
 
t1=d2-d1 #--> timedelta
print(t1)
soNgayChenhLech=t1.days
soGiayChenhLech=t1.seconds

# Demo timedelta
ngayMai=date.today()+timedelta(days=1) #--> date
ngayHomQua1=date.today()+timedelta(days=-1) #--> date
ngayHomQua2=date.today()-timedelta(days=1) #--> date
 
t=timedelta(days=5,hours=1,minutes=10,seconds=30)
tongSoGiay=t.total_seconds()
print ()
