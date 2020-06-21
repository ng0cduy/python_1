import xml.dom.minidom as xml
danh_sach = [
    {"Ten": "Tiếng chim hót trong bụi mận gai",
        "Nam_san_xuat": "1982", "The_loai": "Tình cảm",
        "Dinh_dang": "DVD"},
    {"Ten": "Chiến tranh và Hòa bình",
     "Nam_san_xuat": "1981", "The_loai": "Tình cảm, Chiến tranh",
     "Dinh_dang": "DVD"},
    {"Ten": "Người đẹp và Quái vật",
     "Nam_san_xuat": "1990", "The_loai": "Tình cảm, Hoạt hình",
     "Dinh_dang": "VHS"}]

tai_lieu = xml.Document()

#tạo node root
node_root = tai_lieu.createElement('DANH_SACH')
tai_lieu.appendChild(node_root)
for film in danh_sach:
    ten_film = film["Ten"]
    nam_sx = film["Nam_san_xuat"]
    typee = film["The_loai"]
    formatt = film["Dinh_dang"]
#tạo node con
    #tạo node film
    node_film = tai_lieu.createElement("PHIM")
    node_root.appendChild(node_film)
    #gan du lieu cho node film
    node_film.setAttribute("Nam_san_xuat",nam_sx)
    node_film.setAttribute("Ten",ten_film)
    #tạo node thể loại
    node_the_loai = tai_lieu.createElement("The_loai")
    node_film.appendChild(node_the_loai)
    node_the_loai.appendChild(tai_lieu.createTextNode(typee))
    #tạo node định dạng
    node_dinh_dang = tai_lieu.createElement("Dinh_dang")
    node_film.appendChild(node_dinh_dang)
    node_dinh_dang.appendChild(tai_lieu.createTextNode(formatt))
f = open("files_xml/phim_moi.xml","w",encoding="utf-8")
tai_lieu.writexml(f,newl="\n",addindent = "\t")