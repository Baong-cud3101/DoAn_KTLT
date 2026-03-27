from nghiep_vu.XuLyNguoiDung import XuLyNguoiDung
from nghiep_vu.XuLyNganSach import XuLyNganSach
from du_lieu.kho_luu_tru.LuuTruNganSach import LuuTruNganSach
from nghiep_vu.tai_khoan.XuLyNguoiDung import XuLyNguoiDung
from nghiep_vu.shared.KiemTra import KiemTraDuLieu
from du_lieu.LuuTruNguoiDung import LuuTruNguoiDung
from nghiep_vu.giao_dich.XuLyGiaoDich import XuLyGiaoDich
from du_lieu.LuuTruGiaoDich import LuuTruGiaoDich
import pandas as pd
from nghiep_vu.giao_dich.XuLyGiaoDich import XuLyExcelNghiepVu
from nghiep_vu.tai_khoan.XuLyNguoiDung import XuLyNguoiDung
from du_lieu.LuuTruNguoiDung import LuuTruNguoiDung
class MainController:
    def __init__(self):
        self.xu_ly_nd = XuLyNguoiDung()
        # Giả sử self.ui_login là giao diện nạp từ login.ui
        # self.ui_login.btn_login.clicked.connect(self.thuc_hien_dang_nhap)

    def thuc_hien_dang_nhap(self):
        u = self.ui_login.txt_username.text()
        p = self.ui_login.txt_password.text()
        
        user, message = self.xu_ly_nd.dang_nhap(u, p)
        if user:
            print(f"Chào mừng {user['HoTen']}")
            # Chuyển sang màn hình Dashbo
        else:
            print(f"Thất bại: {message}")
        

class DieuKhienNganSach:
    def __init__(self):
        self.xu_ly = XuLyNganSach()
        self.luu_tru = LuuTruNganSach()

    def thiet_lap_ngan_sach(self, ma_nguoi_dung: str, du_lieu: dict):
        du_lieu["MaND"] = ma_nguoi_dung
        hop_le, thong_bao = self.xu_ly.kiem_tra_ngan_sach(du_lieu)
        if not hop_le:
            return {
                "success": False,
                "message": thong_bao
            }
        self.luu_tru.luu(du_lieu)
        return {
            "success": True,
            "message": "Thiet lap ngan sach thanh cong"
        }
    def lay_trang_thai_ngan_sach(self, ma_nguoi_dung: str):
        danh_sach = self.luu_tru.doc_tat_ca()
        ket_qua = [
            ns for ns in danh_sach
            if ns.get("MaND") == ma_nguoi_dung
        ]
        return {
            "success": True,
            "data": ket_qua
        }

    def kiem_tra_canh_bao(self, ma_nguoi_dung: str, danh_muc: str, so_tien: float):
        canh_bao = self.xu_ly.kiem_tra_canh_bao(
            ma_nguoi_dung,
            danh_muc,
            so_tien
        )
        if not canh_bao:
            return {
                "canh_bao": None
            }
        return {
            "canh_bao": canh_bao
        }
class DieuKhienHoSo:
    def lay_ho_so(self, ma_nguoi_dung: str) -> dict: pass
    def cap_nhat_ho_so(self, ma_nguoi_dung: str, du_lieu: dict): pass
    def doi_email(self, ma_nguoi_dung: str, mat_khau: str, email_moi: str): pass
    def doi_mat_khau(self, ma_nguoi_dung: str, mat_khau_cu: str, mat_khau_moi: str): pass



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
def dang_xuat(self, ma_nguoi_dung: str, ma_xac_thuc: str) -> dict:
    try:
        self.xu_ly.xoa_phien(ma_nguoi_dung, ma_xac_thuc)
        return {"success": True}
    except Exception as e:
        return {"success": False, "message": str(e)}

class DieuKhienGiaoDich:
    def __init__(self):
        self.xu_ly = XuLyGiaoDich()
        self.luu_tru = LuuTruGiaoDich()
    def them_giao_dich(self, ma_nguoi_dung: str, du_lieu: dict):
        du_lieu["MaND"] = ma_nguoi_dung
        ket_qua = self.xu_ly.xu_ly_giao_dich(du_lieu)
        giao_dich = ket_qua["giao_dich"]
        canh_bao = ket_qua["canh_bao"]
        self.luu_tru.luu(giao_dich)
        return {
            "success": True,
            "giao_dich": giao_dich,
            "canh_bao": canh_bao
        }

    def lay_lich_su(self, ma_nguoi_dung: str, trang: int = 1):
        danh_sach = self.luu_tru.doc_tat_ca()
        ket_qua = [
            gd for gd in danh_sach
            if gd.get("MaND") == ma_nguoi_dung
        ]
        return ket_qua
    def tim_kiem(self, ma_nguoi_dung: str, bo_loc: dict):
        ket_qua = self.luu_tru.loc_du_lieu(ma_nguoi_dung, bo_loc)
        return {
            "success": True,
            "data": ket_qua
        }

    def xoa_giao_dich(self, ma_nguoi_dung: str, ma_giao_dich: str):
        thanh_cong = self.luu_tru.xoa(ma_giao_dich, ma_nguoi_dung)
        if not thanh_cong:
            return {
                "success": False,
                "message": "Khong tim thay hoac khong co quyen xoa"
            }
        return {
            "success": True,
            "message": "Da xoa giao dich"
        }

class DieuKhienExcel:
    def __init__(self):
        self.xu_ly = XuLyExcelNghiepVu()
    def nhap_excel(self, ma_nguoi_dung: str, tap_tin) -> dict:
        try:
            df = pd.read_excel(tap_tin)
        except Exception as e:
            return {
                "success": False,
                "message": f"Loi doc file: {str(e)}"
            }
        danh_sach = df.to_dict(orient="records")
        if not danh_sach:
            return {
                "success": False,
                "message": "File khong co du lieu"
            }
        ket_qua = self.xu_ly.nhap_hang_loat(ma_nguoi_dung, danh_sach)
        return {
            "success": True,
            "tong_dong": len(danh_sach),
            "thanh_cong": ket_qua.get("thanh_cong", 0),
            "that_bai": ket_qua.get("that_bai", 0),
            "chi_tiet_loi": ket_qua.get("chi_tiet_loi", [])
        }

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
