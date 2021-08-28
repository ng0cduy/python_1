import calendar
# kiểm tra năm nhuần
laNamNhuan1=calendar.isleap(2000) # --> True
laNamNhuan2=calendar.isleap(200) # --> False

tuple_MR=calendar.monthrange(2019,11) #--> tuple (4,30)

soNgayTrongThang=calendar.monthrange(2019,11)[1] # --> 30
soNgayTrongThang2=tuple_MR[1]

# Chỉ số thứ của ngày đầu tiên trong tháng
chiSoThu=calendar.monthrange(2019,11)[0] # --> thứ 6
chiSoThu2=tuple_MR[0]

lichThang=calendar.monthcalendar(2019,11)
print(lichThang)
print()


# https://docs.python.org/3.7/library/calendar.html
