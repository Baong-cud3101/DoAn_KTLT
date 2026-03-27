class DieuKhienHeThong:
    def kiem_tra_trang_thai(self) -> bool: pass
    def dong_bo_du_lieu(self): pass


from nghiep_vu.shared.KiemTra import KiemTraDuLieu
from du_lieu.LuuTruCauHinh import LuuTruCauHinh
class DieuKhienHeThong:
    def __init__(self):
        self.kiem_tra = KiemTraDuLieu()
        self.luu_tru = LuuTruCauHinh()
    def kiem_tra_trang_thai(self) -> bool:
        try:
            data = self.luu_tru.doc_tat_ca()
            return True if data else False
        except:
            return False
    def dong_bo_du_lieu(self, du_lieu_moi: dict) -> dict:

        for key, value in du_lieu_moi.items():
            if self.kiem_tra.kiem_tra_rong(value):
                return {"success": False, "message": f"{key}_RONG"}
            if not self.kiem_tra.kiem_tra_kieu_so(value):
                return {"success": False, "message": f"{key}_KHONG_HOP_LE"}
            if float(value) < 0:
                return {"success": False, "message": f"{key}_PHAI_DUONG"}
        try:
            self.luu_tru.ghi_tat_ca(du_lieu_moi)
        except Exception as e:
            return {"success": False, "message": str(e)}
        return {"success": True}
