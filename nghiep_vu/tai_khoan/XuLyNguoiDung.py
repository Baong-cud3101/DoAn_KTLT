class XuLyNguoiDung:
    THOI_GIAN_HET_HAN_OTP: int = 600
    SO_LAN_THU_TOI_DA: int = 5
    THOI_GIAN_KHOA_PHUT: int = 5
    SO_VONG_BAM_MUOI: int = 12

    def kiem_tra_hop_le(self, email: str, mat_khau: str) -> bool: pass
    def bam_mat_khau(self, mat_khau: str) -> str: pass
    def xac_thuc_chuoi_bam(self, chuoi_nhap: str, chuoi_luu: str) -> bool: pass
    def tao_ma_otp(self) -> tuple[str, float]: pass
    def kiem_tra_ma_otp(self, ma_nhap: str, ma_luu: str, thoi_gian_het_han: float) -> bool: pass
    def tao_jwt(self, ma_nguoi_dung: str, vai_tro: str) -> str: pass
    def xac_thuc_jwt(self, ma_xac_thuc: str) -> dict | None: pass
    def xac_thuc_nguoi_dung(self, email: str, mat_khau: str) -> dict: pass
    def dang_ky(self, du_lieu: dict) -> dict: pass
    def cap_nhat_ho_so(self, ma_nguoi_dung: str, truong_du_lieu: dict): pass
    def doi_email(self, ma_nguoi_dung: str, email_moi: str, ma_otp: str): pass
    def dat_lai_mat_khau(self, ma_xac_thuc: str, mat_khau_moi: str): pass

import re
import time
import random
import string
import hashlib
import base64
import json
class XuLyNguoiDung:
    THOI_GIAN_HET_HAN_OTP: int = 600
    SO_LAN_THU_TOI_DA: int = 5
    THOI_GIAN_KHOA_PHUT: int = 5
    SO_VONG_BAM_MUOI: int = 12
    def __init__(self):
        self.otp_store = {}  #email:otp, expire_time
    def kiem_tra_hop_le(self, email: str, mat_khau: str) -> bool:
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email) and len(mat_khau) >= 6
    def bam_mat_khau(self, mat_khau: str) -> str:
        salt = "salt123"
        return hashlib.sha256((mat_khau + salt).encode()).hexdigest()
    def xac_thuc_chuoi_bam(self, chuoi_nhap: str, chuoi_luu: str) -> bool:
        return self.bam_mat_khau(chuoi_nhap) == chuoi_luu
    def tao_ma_otp(self) -> tuple[str, float]:
        otp = ''.join(random.choices(string.digits, k=6))
        expire = time.time() + self.THOI_GIAN_HET_HAN_OTP
        return otp, expire
    def kiem_tra_ma_otp(self, ma_nhap: str, ma_luu: str, thoi_gian_het_han: float) -> bool:
        if time.time() > thoi_gian_het_han:
            return False
        return ma_nhap == ma_luu
    def tao_jwt(self, ma_nguoi_dung: str, vai_tro: str) -> str:
        payload = {
            "ma_nd": ma_nguoi_dung,
            "role": vai_tro,
            "time": time.time()
        }
        return base64.b64encode(json.dumps(payload).encode()).decode()
    def xac_thuc_jwt(self, ma_xac_thuc: str) -> dict | None:
        try:
            data = base64.b64decode(ma_xac_thuc).decode()
            return json.loads(data)
        except:
            return None
    def xac_thuc_nguoi_dung(self, email: str, mat_khau: str) -> dict:
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except:
            return {"success": False, "message": "Chưa có dữ liệu"}

        for u in users:
            if u["Email"] == email:
                if self.xac_thuc_chuoi_bam(mat_khau, u["MatKhauHash"]):
                    token = self.tao_jwt(u["MaND"], "user")
                    return {"success": True, "token": token}
                else:
                    return {"success": False, "message": "Sai mật khẩu"}

        return {"success": False, "message": "Không tìm thấy user"}
    def dang_ky(self, du_lieu: dict) -> dict:
        email = du_lieu.get("Email")
        mat_khau = du_lieu.get("MatKhau")

        if not self.kiem_tra_hop_le(email, mat_khau):
            return {"success": False, "message": "Email hoặc mật khẩu không hợp lệ"}
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except:
            users = []

        for u in users:
            if u["Email"] == email:
                return {"success": False, "message": "Email đã tồn tại"}
        ma_nd = "ND" + str(random.randint(10000, 99999))

        user = {
            "MaND": ma_nd,
            "Email": email,
            "MatKhauHash": self.bam_mat_khau(mat_khau),
            "HoTen": du_lieu.get("HoTen"),
            "SoDT": du_lieu.get("SoDT"),
            "TrangThai": "CHUA_XAC_THUC"
        }
        otp, expire = self.tao_ma_otp()
        self.otp_store[email] = (otp, expire)

        print(f"[OTP DEBUG] {email}: {otp}")

        users.append(user)
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        return {"success": True, "MaND": ma_nd}
    def cap_nhat_ho_so(self, ma_nguoi_dung: str, truong_du_lieu: dict):
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except:
            return
        for u in users:
            if u["MaND"] == ma_nguoi_dung:
                u.update(truong_du_lieu)
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
    def doi_email(self, ma_nguoi_dung: str, email_moi: str, ma_otp: str):
        if email_moi not in self.otp_store:
            return False

        otp, expire = self.otp_store[email_moi]

        if not self.kiem_tra_ma_otp(ma_otp, otp, expire):
            return False

        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except:
            return False

        for u in users:
            if u["MaND"] == ma_nguoi_dung:
                u["Email"] = email_moi

        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        return True
    def dat_lai_mat_khau(self, ma_xac_thuc: str, mat_khau_moi: str):
        data = self.xac_thuc_jwt(ma_xac_thuc)
        if not data:
            return False
        ma_nd = data["ma_nd"]
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except:
            return False

        for u in users:
            if u["MaND"] == ma_nd:
                u["MatKhauHash"] = self.bam_mat_khau(mat_khau_moi)

        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
        return True
