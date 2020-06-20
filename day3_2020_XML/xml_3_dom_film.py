from xml.dom.minidom import parse
import xml.dom.minidom


tai_lieu = parse('files_xml/phim.xml')
node_root = tai_lieu.documentElement
films = node_root.getElementsByTagName ("PHIM")

for film in films:
    nam_sx = film.getAttribute('Nam_san_xuat')
    ten = film.getAttribute('Ten')
    types = film.getElementsByTagName("The_loai")[0].childNodes[0].data
    formatt = film.getElementsByTagName("Dinh_dang")[0].childNodes[0].data
    print ("Tên Phim:", ten)
    print ("Năm sản xuất:",nam_sx)
    print ("Thể loại:",types)
    print ("Định dạng:",formatt)
    print()