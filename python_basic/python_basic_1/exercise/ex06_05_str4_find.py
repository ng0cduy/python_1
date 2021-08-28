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
giatritim='cảnh'
# Tìm
vitribatdau=0
i = baitho.find(giatritim)
# Tìm tiếp
vitribatdau=i+len(giatritim)
j = baitho.find(giatritim,vitribatdau)
print()