import datetime
class Transaction (object):
    def __init__(self,tran_id,day,quantity,type,price):
        self.tran_id =tran_id
        self.day = day
        self.quantity = quantity
        self.price = price
        self.type =type
    def paid (self):
        return self.quantity* self.price
    def print_tran(self):
        return self.tran_id + " - " + self.day + " - " + self.type + " - " + str(self.quantity) \
            + " - " + "{:,.0f}".format(self.price) + " -Total = " + "{:,.0f}".format(self.paid())
class Trans_Money(Transaction):
    def __init__(self,id,day,quantity,type,price,buy):
        self.buy = buy
        Transaction.__init__(self,id,day,quantity,type,price)
    def total_paid(self):
        if self.buy:
            return Transaction.paid(self)
        else: 
            return Transaction.paid(self) *1.05
    def print_paid_money(self):
        if self.buy:
            print ("Buying Transaction: ", "{:,.0f}".format(self.total_paid()))
        else: 
            print ("Selling Transaction: ","{:,.0f}".format(self.total_paid()))
if __name__ == "__main__":
    id = input("Input ID: ")
    day = input("Input day in dd/mm/yyyy")
    sl = int (input("Input quantity"))
    type = int (input("Choose the type: 1.Gold     2.Money"))
    

    # d1= datetime.datetime.strptime(day,"%d/%m/%y")
    