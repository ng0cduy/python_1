interest = eval(input("Nhập lãi suất tiết kiệm 1 năm (%): "))
money    = eval(input("Nhập số tiền gửi: "))
months   = eval(input("Nhập số tháng gửi: "))
income = (money*months)*(interest/1200)
print ("tiền lãi là: %.2f vnd" %income)
print ("tổng số tiền là: %.2f vnd" %(income+money))