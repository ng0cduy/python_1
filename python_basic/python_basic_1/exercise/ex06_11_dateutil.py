from dateutil import relativedelta # pip install python-dateutil
from datetime import datetime

d1=datetime(2018,6,18,7,30,00)
d2=datetime(2019,7,20,8,32,20)

# Tính chênh lệch
chenhLech=relativedelta.relativedelta(d2,d1)
soNam=chenhLech.years # 1
soThang=chenhLech.months # 1
soNgay=chenhLech.days # 2
soGio=chenhLech.hours # 1
soPhut=chenhLech.minutes # 2
soGiay=chenhLech.seconds # 20
print()
