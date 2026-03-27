import os
from du_lieu.quan_ly_file.DocGhiJson import DocGhiJson

class LuuTruNguoiDung:
    def __init__(self):
        self.file_path = os.path.join('du_lieu', 'file_du_lieu', 'nguoi_dung.json')

    def lay_danh_sach(self):
        return DocGhiJson.doc_file(self.file_path)

    def cap_nhat(self, data):
        DocGhiJson.ghi_file(self.file_path, data)