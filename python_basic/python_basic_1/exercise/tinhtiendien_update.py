try:
    usertype = input('Nhập kiểu sử dụng: trả trước (1) hoặc trả sau (2): ')
    assert(usertype=='1' or usertype=='2'),'Vui lòng chỉ nhập 1 hoặc 2'
    usageamount=float(input('Nhập số lượng điện tiêu thụ nhà bạn: '))
    assert(usageamount>=0),'>>> Vui lòng nhập số dương'
except ValueError:
    print("Vui lòng nhập số")
    exit(0)
except AssertionError as thongbao:
    print (thongbao)
else:
    if (usertype ==1):
        tongtiendien = 2461*usageamount
    else:
        if (usageamount<=50):
            tongtiendien = usageamount*1678
        elif(usageamount<=100):
            tongtiendien = 50*1678+(usageamount-50)*1734
        elif(usageamount<=200):
            tongtiendien = 50*1678+50*1734+(usageamount-100)*2014
        elif(usageamount<=300):
            tongtiendien = 50*1678+50*1734+100*2014+(usageamount-200)*2536
        elif(usageamount<=400):
            tongtiendien = 50*1678+50*1734+100*2014+100*2536+(usageamount-300)*2834
        else:
            tongtiendien = 50*1678+50*1734+100*2014+100*2536+100*2834+(usageamount-400)*2927   
    print("Tổng số tiền điện bạn phải trả là %.0f đồng: ",tongtiendien)