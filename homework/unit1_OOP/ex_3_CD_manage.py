class CD_manage (object):
    def __init__(self,CD_name,singer_name,song_num,price):
        self.CD_name = CD_name
        self.singer_name = singer_name
        self.song_num = song_num
        self.price = price
    def print_CD_info (self):
        print ("#", self.CD_name,"-",self.singer_name,"-",self.song_num,"-",self.price)

if __name__ == "__main__":
    while True:
        CD_name = input("Input CD name: ")
        singer_name = input("input Singer name: ")
        song_num = int(input("Input number of songs: "))
        price = float(input("Input the price of the CD: "))
        CD = CD_manage(CD_name,singer_name,song_num,price)
        CD.print_CD_info()
        c = input("Do you want to continue: Y/N ")
        if c.lower() != "y":
            break
            
    