class DieuKhienDangNhap:
    def dang_nhap(self, email: str, mat_khau: str) -> dict: pass
    def dang_xuat(self, ma_nguoi_dung: str, ma_xac_thuc: str): pass
    def tu_dong_dang_xuat(self, ma_nguoi_dung: str): pass
    def quen_mat_khau(self, email: str): pass
    def dat_lai_mat_khau(self, ma_xac_thuc: str, mat_khau: str): pass



from nghiep_vu.tai_khoan.XuLyNguoiDung import XuLyNguoiDung
from du_lieu.LuuTruNguoiDung import LuuTruNguoiDung
class DieuKhienDangNhap:
    def __init__(self):
        self.xu_ly = XuLyNguoiDung()
        self.luu_tru = LuuTruNguoiDung()
    def dang_nhap(self, email: str, mat_khau: str) -> dict:
        user = self.luu_tru.tim_theo_email(email)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}
        if not self.xu_ly.xac_thuc_chuoi_bam(mat_khau, user["MatKhauHash"]):
            return {"success": False, "message": "SAI_MAT_KHAU"}
        token = self.xu_ly.tao_jwt(user["MaND"], "user")
        self.luu_tru.luu_phien_lam_viec(user["MaND"], token, "")
        return {
            "success": True,
            "token": token,
            "ma_nd": user["MaND"]
        }
    def dang_xuat(self, ma_nguoi_dung: str, ma_xac_thuc: str):
        self.xu_ly.xoa_phien(ma_nguoi_dung, ma_xac_thuc)
        return {"success": True}
    def tu_dong_dang_xuat(self, ma_nguoi_dung: str):
        self.luu_tru.xoa_phien_lam_viec(ma_nguoi_dung)
    def quen_mat_khau(self, email: str) -> dict:
        user = self.luu_tru.tim_theo_email(email)
        if not user:
            return {"success": False, "message": "EMAIL_KHONG_TON_TAI"}
        otp, expire = self.xu_ly.tao_ma_otp()
        self.xu_ly.otp_store[email] = (otp, expire)
        print(f"[OTP DEBUG] {email}: {otp}")
        return {"success": True}
    def dat_lai_mat_khau(self, email: str, ma_otp: str, mat_khau_moi: str) -> dict:
        if email not in self.xu_ly.otp_store:
            return {"success": False, "message": "KHONG_CO_OTP"}
        otp_luu, expire = self.xu_ly.otp_store[email]
        if not self.xu_ly.kiem_tra_ma_otp(ma_otp, otp_luu, expire):
            return {"success": False, "message": "OTP_SAI"}
        user = self.luu_tru.tim_theo_email(email)
        if not user:
            return {"success": False, "message": "KHONG_TON_TAI"}
        mat_khau_hash = self.xu_ly.bam_mat_khau(mat_khau_moi)
        self.luu_tru.cap_nhat(user["MaND"], {
            "MatKhauHash": mat_khau_hash
        })
        del self.xu_ly.otp_store[email]
        return {"success": True}
