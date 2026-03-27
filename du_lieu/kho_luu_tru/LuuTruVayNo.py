from du_lieu.quan_ly_file.DocGhiJson import DocGhiJson
from du_lieu.quan_ly_file.DuongDanFile import DuongDanFile

class LuuTruVayNo:
    def __init__(self):
        self.file_path = DuongDanFile.lay_duong_dan('vay_no.json')

    def lay_danh_sach(self):
        return DocGhiJson.doc_file(self.file_path)

    def them_khoan_vay(self, khoan_vay):
        danh_sach = self.lay_danh_sach()
        danh_sach.append(khoan_vay)
        DocGhiJson.ghi_file(self.file_path, danh_sach)

    def cap_nhat_khoan_vay(self, khoan_vay_moi):
        danh_sach = self.lay_danh_sach()
        for i, kv in enumerate(danh_sach):
            if kv.get('id') == khoan_vay_moi.get('id'):
                danh_sach[i] = khoan_vay_moi
                break
        DocGhiJson.ghi_file(self.file_path, danh_sach)