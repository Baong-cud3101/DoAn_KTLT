from du_lieu.quan_ly_file.DocGhiJson import DocGhiJson
from du_lieu.quan_ly_file.DuongDanFile import DuongDanFile

class LuuTruDauTu:
    def __init__(self):
        self.file_path = DuongDanFile.lay_duong_dan('dau_tu.json')

    def lay_danh_sach(self):
        return DocGhiJson.doc_file(self.file_path)

    def them_danh_muc(self, dau_tu):
        danh_sach = self.lay_danh_sach()
        danh_sach.append(dau_tu)
        DocGhiJson.ghi_file(self.file_path, danh_sach)