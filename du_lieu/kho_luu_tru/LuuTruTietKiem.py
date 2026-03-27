from du_lieu.quan_ly_file.DocGhiJson import DocGhiJson
from du_lieu.quan_ly_file.DuongDanFile import DuongDanFile

class LuuTruTietKiem:
    def __init__(self):
        self.file_path = DuongDanFile.lay_duong_dan('tiet_kiem.json')

    def lay_danh_sach(self):
        return DocGhiJson.doc_file(self.file_path)

    def luu_so_tiet_kiem(self, so_tiet_kiem):
        danh_sach = self.lay_danh_sach()
        danh_sach.append(so_tiet_kiem)
        DocGhiJson.ghi_file(self.file_path, danh_sach)