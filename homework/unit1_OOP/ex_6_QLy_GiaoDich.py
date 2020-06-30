import datetime
class Transaction (object):
    def __init__(self,tran_id,day,quantity,type_,price):
        self.tran_id =tran_id
        self.day = day
        self.quantity = quantity
        self.price = price
        self.type =type_
    def paid (self):
        return self.quantity* self.price
    def print_tran(self):
        return "Transaction ID: " + self.tran_id + " - " +"Transaction date: " + \
                self.day + " - " + self.type + " - " + "Quantity: "+ \
                str(self.quantity)+ " - " + "Price: "+"{:,.0f}".format(self.price) + \
                " -Total = " + "{:,.0f}".format(self.paid())
class Trans_Money(Transaction):
    def __init__(self,id,day,quantity,type,price,buy):
        self.buy = buy
        Transaction.__init__(self,id,day,quantity,type,price)
    def total_paid(self):
        if self.buy:
            return Transaction.paid(self)
        else: 
            return Transaction.paid(self) *1.05
    # def print_paid_money(self):
    #     if self.buy ==1 :
    #         print ("Buying Transaction: ", "{:,.0f}".format(self.total_paid()))
    #     elif self.buy ==0: 
    #         print ("Selling Transaction: ","{:,.0f}".format(self.total_paid()))
    def print_tran_money(self):
        return "Transaction ID: " + self.tran_id + " - " +"Transaction date: " + \
                self.day + " - " + self.type + " - " + "Quantity: "+ \
                str(self.quantity)+ " - " + "Price: "+"{:,.0f}".format(self.price) + \
                " -Total = " + "{:,.0f}".format(self.total_paid())
if __name__ == "__main__":
    id_ = input("Input Transaction ID: ")
    day_ = input("Input Transaction day in dd/mm/yyyy: ")
    quantity_ = float (input("Input Transaction quantity: "))
    type_Transaction = int (input("Choose the type: 1.Gold     2.Money: "))
    if (type_Transaction==1):
        gold_type = input("Choose the type of gold: 18k /   24k /   9999: ")
        if gold_type == "18k" or gold_type == "24k" or gold_type == "9999":
            if gold_type == "18k":
                price_1 = 35854000
            elif gold_type =="24k":
                price_1 = 47600000
            elif gold_type == "9999":
                price_1 = 47950000
            data = Transaction(id_,day_,quantity_,gold_type,price_1)
            print(data.print_tran())
        else:
            print ("Valid input, please input again!!")
    elif type_Transaction == 2 :
        money_type = input("Choose the type of money: USD /   EUR /   AUD ").upper()
        if money_type== "USD" or money_type == "EUR" or money_type == "AUD":
            if money_type == "USD":
                price_1 = 233000
            elif money_type.lower =="EUR":
                price_1 = 26650
            elif money_type == "AUD":
                price_1 = 16000
            buying_type = int(input("Do you want to buy or sell: 1/Buy  0/Sell: "))
            if buying_type ==1 or buying_type ==0:
                data=Trans_Money(id_,day_,quantity_,money_type,price_1,buying_type)
                print(data.print_tran_money())
            else:
                print ("Invalid buying type, input again!")
        else:
            print ("Valid input, please input again!!")
    else:
        print ("Error")
        

        



    
 
    