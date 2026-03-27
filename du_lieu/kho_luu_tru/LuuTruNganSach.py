from du_lieu.quan_ly_file.DocGhiJson import DocGhiJson
from du_lieu.quan_ly_file.DuongDanFile import DuongDanFile

class LuuTruNganSach:
    def __init__(self):
        self.file_path = DuongDanFile.lay_duong_dan('ngan_sach.json')

    def lay_tat_ca(self):
        return DocGhiJson.doc_file(self.file_path)

    def lay_ngan_sach_theo_thang(self, thang, nam):
        tat_ca = self.lay_tat_ca()
        return [ns for ns in tat_ca if ns.get('thang') == thang and ns.get('nam') == nam]

    def luu_ngan_sach(self, ngan_sach_moi):
        danh_sach = self.lay_tat_ca()
        # Cập nhật nếu đã tồn tại, thêm mới nếu chưa
        for i, ns in enumerate(danh_sach):
            if ns.get('thang') == ngan_sach_moi.get('thang') and \
               ns.get('nam') == ngan_sach_moi.get('nam') and \
               ns.get('danh_muc') == ngan_sach_moi.get('danh_muc'):
                danh_sach[i] = ngan_sach_moi
                DocGhiJson.ghi_file(self.file_path, danh_sach)
                return
        danh_sach.append(ngan_sach_moi)
        DocGhiJson.ghi_file(self.file_path, danh_sach)