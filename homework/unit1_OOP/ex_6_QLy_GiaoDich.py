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
            + " - " + str(self.price) + " -Total = " + str(self.paid())
class Trans_Gold(Transaction):
    def __init__(self,id,day,quantity,type,price,buy):
        self.buy = buy
        Transaction.__init__(self,id,day,quantity,type,price)
if __name__ == "__main__":
    pass