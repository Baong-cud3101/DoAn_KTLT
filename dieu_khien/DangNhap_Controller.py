class DieuKhienDangNhap:
    def dang_nhap(self, email: str, mat_khau: str) -> dict: pass
    def dang_xuat(self, ma_nguoi_dung: str, ma_xac_thuc: str): pass
    def tu_dong_dang_xuat(self, ma_nguoi_dung: str): pass
    def quen_mat_khau(self, email: str): pass
    def dat_lai_mat_khau(self, ma_xac_thuc: str, mat_khau: str): pass



from nghiep_vu.tai_khoan.XuLyNguoiDung import XuLyNguoiDung
from nghiep_vu.shared.KiemTra import KiemTraDuLieu
from du_lieu.LuuTruNguoiDung import LuuTruNguoiDung
import time
class DieuKhienDangNhap:
    def __init__(self):
        self.xu_ly = XuLyNguoiDung()
        self.kiem_tra = KiemTraDuLieu()
        self.luu_tru = LuuTruNguoiDung()
    def dang_nhap(self, email: str, mat_khau: str) -> dict:
        if self.kiem_tra.kiem_tra_rong(email) or self.kiem_tra.kiem_tra_rong(mat_khau):
            return {"success": False, "message": "Thiếu dữ liệu"}
        user = self.luu_tru.tim_theo_email(email)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}
        if user.get("TrangThai") == "BI_KHOA":
            return {"success": False, "message": "TAI_KHOAN_BI_KHOA"}
        if not self.xu_ly.xac_thuc_chuoi_bam(mat_khau, user["MatKhauHash"]):
            so_lan = self.luu_tru.tang_so_lan_thu(user["MaND"])
            if so_lan >= self.xu_ly.SO_LAN_THU_TOI_DA:
                self.luu_tru.khoa_tai_khoan(
                    user["MaND"],
                    time.ctime()
                )
                return {"success": False, "message": "TAI_KHOAN_BI_KHOA"}
            return {"success": False, "message": "SAI_MAT_KHAU"}
        self.luu_tru.cap_nhat(user["MaND"], {"SoLanThu": 0})
        token = self.xu_ly.tao_jwt(user["MaND"], "user")
        self.luu_tru.luu_phien_lam_viec(
            user["MaND"],
            token,
            str(time.time() + 3600)
        )
        return {
            "success": True,
            "token": token,
            "MaND": user["MaND"]
        }

    def dang_xuat(self, ma_nguoi_dung: str, ma_xac_thuc: str):
        self.luu_tru.xoa_phien_lam_viec(ma_nguoi_dung)

    def tu_dong_dang_xuat(self, ma_nguoi_dung: str):
        self.luu_tru.xoa_phien_lam_viec(ma_nguoi_dung)

    def quen_mat_khau(self, email: str):
        user = self.luu_tru.tim_theo_email(email)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}
        token = self.xu_ly.tao_jwt(user["MaND"], "reset")
        self.luu_tru.luu_ma_khoi_phuc(
            user["MaND"],
            token,
            str(time.time() + 600)
        )
        print(f"[RESET TOKEN] {token}")

        return {"success": True}

    def dat_lai_mat_khau(self, ma_xac_thuc: str, mat_khau: str):
        data = self.xu_ly.xac_thuc_jwt(ma_xac_thuc)
        if not data:
            return {"success": False, "message": "TOKEN_INVALID"}
        ma_nd = data["ma_nd"]
        user = self.luu_tru.tim_theo_id(ma_nd)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}
        mat_khau_hash = self.xu_ly.bam_mat_khau(mat_khau)
        self.luu_tru.cap_nhat(ma_nd, {
            "MatKhauHash": mat_khau_hash
        })
        self.luu_tru.xoa_ma_khoi_phuc(ma_nd)
        return {"success": True}
