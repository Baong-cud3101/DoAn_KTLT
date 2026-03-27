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
        self.otp_store = {}
    def kiem_tra_hop_le(self, email: str, mat_khau: str) -> bool:
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email) and len(mat_khau) >= 6
    def kiem_tra_do_manh_mat_khau(self, mat_khau: str) -> bool:
        if len(mat_khau) < 6:
            return False

        has_letter = any(c.isalpha() for c in mat_khau)
        has_digit = any(c.isdigit() for c in mat_khau)

        return has_letter and has_digit
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
            with open("du_lieu/file_du_lieu/nguoi_dung.json", "r", encoding="utf-8") as f:
                users = json.load(f)
        except:
            return {"success": False, "message": "KHONG_CO_DU_LIEU"}

        for u in users:
            if u["Email"] == email:
                if self.xac_thuc_chuoi_bam(mat_khau, u["MatKhauHash"]):
                    token = self.tao_jwt(u["MaND"], "user")
                    return {"success": True, "token": token}
                else:
                    return {"success": False, "message": "SAI_MAT_KHAU"}

        return {"success": False, "message": "KHONG_TON_TAI"}
    def dang_ky(self, du_lieu: dict) -> dict:
        email = du_lieu.get("Email")
        mat_khau = du_lieu.get("MatKhau")

        if not self.kiem_tra_hop_le(email, mat_khau):
            return {"success": False, "message": "DU_LIEU_KHONG_HOP_LE"}

        try:
            with open("du_lieu/file_du_lieu/nguoi_dung.json", "r", encoding="utf-8") as f:
                users = json.load(f)
        except:
            users = []

        for u in users:
            if u["Email"] == email:
                return {"success": False, "message": "EMAIL_DA_TON_TAI"}

        ma_nd = "ND" + str(random.randint(10000, 99999))

        user = {
            "MaND": ma_nd,
            "Email": email,
            "MatKhauHash": self.bam_mat_khau(mat_khau),
            "HoTen": du_lieu.get("HoTen"),
            "SoDT": du_lieu.get("SoDT"),
            "TrangThai": "CHUA_XAC_THUC",
            "SoLanThu": 0
        }

        otp, expire = self.tao_ma_otp()
        self.otp_store[email] = (otp, expire)

        print(f"[OTP DEBUG] {email}: {otp}")

        users.append(user)

        with open("du_lieu/file_du_lieu/nguoi_dung.json", "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4, ensure_ascii=False)

        return {"success": True, "MaND": ma_nd}

    def cap_nhat_ho_so(self, ma_nguoi_dung: str, truong_du_lieu: dict):
        try:
            with open("du_lieu/file_du_lieu/nguoi_dung.json", "r", encoding="utf-8") as f:
                users = json.load(f)
        except:
            return

        for u in users:
            if u["MaND"] == ma_nguoi_dung:
                u.update(truong_du_lieu)

        with open("du_lieu/file_du_lieu/nguoi_dung.json", "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4, ensure_ascii=False)
    def xoa_phien(self, ma_nguoi_dung: str, ma_xac_thuc: str):
        try:
            with open("du_lieu/file_du_lieu/nguoi_dung.json", "r", encoding="utf-8") as f:
                users = json.load(f)
        except:
            return
        for u in users:
            if u["MaND"] == ma_nguoi_dung:
                u["Session"] = None
        with open("du_lieu/file_du_lieu/nguoi_dung.json", "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4, ensure_ascii=False)
