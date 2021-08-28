baitho="""
Thánh thót tàu tiêu mấy hạt mưa,
Khen ai khéo vẽ cảnh tiêu sơ.
Xanh om cổ thụ tròn xoe tán,
Trắng xoá trường giang phẳng lặng tờ.
 
Bầu dốc giang sơn, say chấp rượu,
Túi lưng phong nguyệt, nặng vì thơ.
Cho hay cảnh cũng ưa người nhỉ,
Thấy cảnh ai mà chẳng ngẩn ngơ.
"""
noiDungtim=input('Nội Dung Tìm: ')
#TÌM KHÔNG PHÂN BIỆT HOA HAY THƯỜNG
vitri=baitho.lower().find(noiDungtim.lower())
if vitri==-1:
    print('Không tìm thấy')
else:
    print('Vị trí:',vitri)