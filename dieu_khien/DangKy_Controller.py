class DieuKhienDangKy:
    def dang_ky(self, du_lieu: dict) -> dict: pass
    def xac_thuc_otp(self, ma_nguoi_dung: str, ma_otp: str) -> dict: pass
import json
import os
import hashlib
import random
import string
class KiemTra:
    @staticmethod
    def hop_le_email(email: str) -> bool:
        return "@" in email and "." in email

    @staticmethod
    def hop_le_mat_khau(password: str) -> bool:
        return len(password) >= 6

    @staticmethod
    def hop_le_sdt(sdt: str) -> bool:
        return sdt.isdigit()

class LuuTruNguoiDung:
    FILE = "nguoi_dung.json"

    @staticmethod
    def doc():
        if not os.path.exists(LuuTruNguoiDung.FILE):
            return []
        with open(LuuTruNguoiDung.FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def ghi(data):
        with open(LuuTruNguoiDung.FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def tim_email(email):
        for u in LuuTruNguoiDung.doc():
            if u["Email"] == email:
                return u
        return None

    @staticmethod
    def them(user):
        data = LuuTruNguoiDung.doc()
        data.append(user)
        LuuTruNguoiDung.ghi(data)

class XuLyNguoiDung:
    def __init__(self):
        self.otp_store = {}

    def hash_mat_khau(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def tao_ma_nd(self):
        return "ND" + str(random.randint(1000, 9999))

    def tao_otp(self, ma_nd):
        otp = ''.join(random.choices(string.digits, k=6))
        self.otp_store[ma_nd] = otp
        print(f"[DEBUG OTP] {ma_nd}: {otp}")
        return otp

    def xac_thuc_otp(self, ma_nd, otp):
        return self.otp_store.get(ma_nd) == otp

class DieuKhienDangKy:

    def __init__(self):
        self.service = XuLyNguoiDung()
        
    def dang_ky(self, du_lieu: dict) -> dict:
        ho_ten = du_lieu.get("HoTen")
        email = du_lieu.get("Email")
        mat_khau = du_lieu.get("MatKhau")
        sdt = du_lieu.get("SoDT")

        if not ho_ten or not email or not mat_khau:
            return {"success": False, "message": "Thiếu thông tin"}

        if not KiemTra.hop_le_email(email):
            return {"success": False, "message": "Email không hợp lệ"}

        if not KiemTra.hop_le_mat_khau(mat_khau):
            return {"success": False, "message": "Mật khẩu yếu"}

        if sdt and not KiemTra.hop_le_sdt(sdt):
            return {"success": False, "message": "SĐT không hợp lệ"}

        if LuuTruNguoiDung.tim_email(email):
            return {"success": False, "message": "Email đã tồn tại"}

        ma_nd = self.service.tao_ma_nd()
        mat_khau_hash = self.service.hash_mat_khau(mat_khau)
        user = {
            "MaND": ma_nd,
            "Email": email,
            "MatKhauHash": mat_khau_hash,
            "HoTen": ho_ten,
            "SoDT": sdt,
            "TrangThai": "CHUA_XAC_THUC"
        }
        LuuTruNguoiDung.them(user)
        otp = self.service.tao_otp(ma_nd)
        return {
            "success": True,
            "message": "Đã gửi OTP",
            "MaND": ma_nd,
            "OTP": otp 
        }
    def xac_thuc_otp(self, ma_nguoi_dung: str, ma_otp: str) -> dict:
        if not self.service.xac_thuc_otp(ma_nguoi_dung, ma_otp):
            return {"success": False, "message": "OTP sai hoặc hết hạn"}
        data = LuuTruNguoiDung.doc()
        for user in data:
            if user["MaND"] == ma_nguoi_dung:
                user["TrangThai"] = "DA_KICH_HOAT"
                break
        LuuTruNguoiDung.ghi(data)
        return {"success": True, "message": "Đăng ký thành công"}
