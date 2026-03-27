from du_lieu.quan_ly_file.DocGhiJson import DocGhiJson
from du_lieu.quan_ly_file.DuongDanFile import DuongDanFile

class LuuTruCauHinh:
    def __init__(self):
        self.file_path = DuongDanFile.lay_duong_dan('cau_hinh.json')

    def lay_cau_hinh(self):
        du_lieu = DocGhiJson.doc_file(self.file_path)
        return du_lieu if du_lieu else {}

    def cap_nhat_cau_hinh(self, cau_hinh):
        DocGhiJson.ghi_file(self.file_path, cau_hinh)