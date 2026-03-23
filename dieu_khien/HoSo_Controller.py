class DieuKhienHoSo:
    def lay_ho_so(self, ma_nguoi_dung: str) -> dict: pass
    def cap_nhat_ho_so(self, ma_nguoi_dung: str, du_lieu: dict): pass
    def doi_email(self, ma_nguoi_dung: str, mat_khau: str, email_moi: str): pass
    def doi_mat_khau(self, ma_nguoi_dung: str, mat_khau_cu: str, mat_khau_moi: str): pass


from nghiep_vu.tai_khoan.XuLyNguoiDung import XuLyNguoiDung
from nghiep_vu.shared.KiemTra import KiemTraDuLieu
from du_lieu.LuuTruNguoiDung import LuuTruNguoiDung
class DieuKhienHoSo:
    def __init__(self):
        self.xu_ly = XuLyNguoiDung()
        self.kiem_tra = KiemTraDuLieu()
        self.luu_tru = LuuTruNguoiDung()
    def lay_ho_so(self, ma_nguoi_dung: str) -> dict:
        user = self.luu_tru.tim_theo_id(ma_nguoi_dung)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}
        return {
            "success": True,
            "data": {
                "MaND": user["MaND"],
                "Email": user["Email"],
                "HoTen": user.get("HoTen", ""),
                "SoDT": user.get("SoDT", "")
            }
        }
        
    def cap_nhat_ho_so(self, ma_nguoi_dung: str, du_lieu: dict):
        if not du_lieu:
            return {"success": False, "message": "THIEU_DU_LIEU"}
        user = self.luu_tru.tim_theo_id(ma_nguoi_dung)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}
        self.luu_tru.cap_nhat(ma_nguoi_dung, du_lieu)
        return {"success": True}
    def doi_email(self, ma_nguoi_dung: str, mat_khau: str, email_moi: str):

        if self.kiem_tra.kiem_tra_rong(email_moi):
            return {"success": False, "message": "THIEU_DU_LIEU"}
        user = self.luu_tru.tim_theo_id(ma_nguoi_dung)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}

        if not self.xu_ly.xac_thuc_chuoi_bam(mat_khau, user["MatKhauHash"]):
            return {"success": False, "message": "SAI_MAT_KHAU"}

        if self.luu_tru.tim_theo_email(email_moi):
            return {"success": False, "message": "EMAIL_DA_TON_TAI"}
        self.luu_tru.cap_nhat(ma_nguoi_dung, {
            "Email": email_moi
        })
        return {"success": True}

    def doi_mat_khau(self, ma_nguoi_dung: str, mat_khau_cu: str, mat_khau_moi: str):

        if self.kiem_tra.kiem_tra_rong(mat_khau_cu) or self.kiem_tra.kiem_tra_rong(mat_khau_moi):
            return {"success": False, "message": "THIEU_DU_LIEU"}

        if len(mat_khau_moi) < 6:
            return {"success": False, "message": "MAT_KHAU_YEU"}

        user = self.luu_tru.tim_theo_id(ma_nguoi_dung)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}

        if not self.xu_ly.xac_thuc_chuoi_bam(mat_khau_cu, user["MatKhauHash"]):
            return {"success": False, "message": "SAI_MAT_KHAU_CU"}
        mat_khau_hash = self.xu_ly.bam_mat_khau(mat_khau_moi)
        self.luu_tru.cap_nhat(ma_nguoi_dung, {
            "MatKhauHash": mat_khau_hash
        })
        return {"success": True}
