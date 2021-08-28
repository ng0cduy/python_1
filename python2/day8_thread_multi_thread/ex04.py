import requests
import time
bd = time.time()
print("Download File")
url = "https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/annual_report_2009.pdf"
print ("Start download...")
r = requests.get(url)
with open ('test_download.pdf','wb') as code:
    code.write(r.content)
print("Finish download!")
print("\n=== Tính toán")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("Tổng: ",a+b)
print("Hiệu: ",a-b)

kt = time.time()
print("Time elapsed: ",kt-bd)