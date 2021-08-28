import requests
import time
import threading
from datetime import datetime
def download_file(url,filename):
    print ("Start download...")
    r = requests.get(url)
    with open (filename,'wb') as code:
        code.write(r.content)
    print("Finish download!")
def tinh_toan(a,b):
    tong = a+b 
    hieu = a-b
    return tong,hieu
class Download(threading.Thread):
    def __init__(self,url,filename):
        threading.Thread.__init__(self)
        self.url = url
        self.filename = filename
    def run(self):
        download_file(self.url,self.filename)

class TinhToan(threading.Thread):
    def __init__(self, a,b):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b
    def run (self):
        print("\n Tính toán")
        tong,hieu = tinh_toan(self.a,self.b)
        print("Tổng: ",tong)
        print("Hiệu: ",hieu)
        print("Kết thúc tính toán.")
if __name__ == "__main__":
    bd = time.time()
    url = "https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/annual_report_2009.pdf"
    ten_file = datetime.now().strftime("%Y%m%d_%H%M%S") + ".pdf"
    download = Download(url,ten_file)
    tinh = TinhToan(5,10)
    #start threading
    download.start()
    tinh.start()
    #join
    download.join()
    tinh.join()
    #Thông báo
    print("\nKết thúc chương trình")
    kt = time.time()
    print("\nTime elapsed",kt-bd)

    