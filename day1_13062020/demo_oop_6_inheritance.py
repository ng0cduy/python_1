# class Human:
#     def __init__(self,name,bd,gendre):
#         self.name =name
#         self.bd = bd
#         self.gendre = gendre
#     def print_info(self):
#         print ("Name: ",self.name)
#         print ("Day of brith: ",self.bd)
#         print ("Gendre: ", self.gendre)
# class employee(Human):
#     def __init__ (self,name,bd,gendre,num,income):
#         self.num = num
#         self.income = income
#         Human.__init__(self,name,bd,gendre)
#     def print_info(self):
#         Human.print_info()
#         print ("num: ",self.num )
#         print ("income: ", self.income)