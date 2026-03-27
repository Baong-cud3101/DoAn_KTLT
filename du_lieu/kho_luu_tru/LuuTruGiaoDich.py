import os
from du_lieu.quan_ly_file.DocGhiJson import DocGhiJson

class LuuTruGiaoDich:
    def __init__(self):
        self.file_path = os.path.join('du_lieu', 'file_du_lieu', 'giao_dich.json')

    def lay_danh_sach(self):
        return DocGhiJson.doc_file(self.file_path)

    def them_moi(self, giao_dich):
        danh_sach = self.lay_danh_sach()
        danh_sach.append(giao_dich)
        DocGhiJson.ghi_file(self.file_path, danh_sach)