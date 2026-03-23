from abc import ABC, abstractmethod

class LuuTruCoSo(ABC):
    def __init__(self, duong_dan_tep: str):
        self._duong_dan_tep = duong_dan_tep
    @abstractmethod
    def doc_tat_ca(self) -> list: pass
    @abstractmethod
    def ghi_tat_ca(self, du_lieu: list): pass
    @abstractmethod
    def tim_theo_id(self, ma_dinh_danh: str) -> dict: pass
    @abstractmethod
    def luu(self, doi_tuong: dict) -> str: pass

class LuuTruNguoiDung(LuuTruCoSo):
    DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/nguoi_dung.json'
    def __init__(self): super().__init__(self.DUONG_DAN_TEP)
    def tim_theo_email(self, email: str) -> dict | None: pass
    def tim_theo_id(self, ma_nguoi_dung: str) -> dict | None: pass
    def luu(self, nguoi_dung: dict) -> str: pass
    def cap_nhat(self, ma_nguoi_dung: str, truong_du_lieu: dict) -> bool: pass
    def luu_phien_lam_viec(self, ma_nguoi_dung: str, ma_xac_thuc: str, han_su_dung: str): pass
    def xoa_phien_lam_viec(self, ma_nguoi_dung: str): pass
    def luu_ma_khoi_phuc(self, ma_nguoi_dung: str, ma_xac_thuc: str, han_su_dung: str): pass
    def xoa_ma_khoi_phuc(self, ma_nguoi_dung: str): pass
    def tang_so_lan_thu(self, ma_nguoi_dung: str) -> int: pass
    def khoa_tai_khoan(self, ma_nguoi_dung: str, thoi_gian_khoa: str): pass


from abc import ABC, abstractmethod
import json
import os
from datetime import datetime
class LuuTruCoSo(ABC):
    def __init__(self, duong_dan_tep: str):
        self._duong_dan_tep = duong_dan_tep
    @abstractmethod
    def doc_tat_ca(self) -> list: pass
    @abstractmethod
    def ghi_tat_ca(self, du_lieu: list): pass
    @abstractmethod
    def tim_theo_id(self, ma_dinh_danh: str) -> dict: pass
    @abstractmethod
    def luu(self, doi_tuong: dict) -> str: pass
class LuuTruNguoiDung(LuuTruCoSo):
    DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/nguoi_dung.json'
    def __init__(self):
        super().__init__(self.DUONG_DAN_TEP)
    def doc_tat_ca(self) -> list:
        if not os.path.exists(self._duong_dan_tep):
            return []

        with open(self._duong_dan_tep, "r", encoding="utf-8") as f:
            return json.load(f)
    def ghi_tat_ca(self, du_lieu: list):
        os.makedirs(os.path.dirname(self._duong_dan_tep), exist_ok=True)

        with open(self._duong_dan_tep, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, indent=4, ensure_ascii=False)
    def tim_theo_email(self, email: str) -> dict | None:
        data = self.doc_tat_ca()
        for u in data:
            if u["Email"] == email:
                return u
        return None
    def tim_theo_id(self, ma_nguoi_dung: str) -> dict | None:
        data = self.doc_tat_ca()
        for u in data:
            if u["MaND"] == ma_nguoi_dung:
                return u
        return None
    def luu(self, nguoi_dung: dict) -> str:
        data = self.doc_tat_ca()
        data.append(nguoi_dung)
        self.ghi_tat_ca(data)
        return nguoi_dung["MaND"]
    def cap_nhat(self, ma_nguoi_dung: str, truong_du_lieu: dict) -> bool:
        data = self.doc_tat_ca()
        for u in data:
            if u["MaND"] == ma_nguoi_dung:
                u.update(truong_du_lieu)
                self.ghi_tat_ca(data)
                return True
        return False
    def luu_phien_lam_viec(self, ma_nguoi_dung: str, ma_xac_thuc: str, han_su_dung: str):
        self.cap_nhat(ma_nguoi_dung, {
            "Session": {
                "Token": ma_xac_thuc,
                "Expire": han_su_dung
            }
        })
    def xoa_phien_lam_viec(self, ma_nguoi_dung: str):
        self.cap_nhat(ma_nguoi_dung, {"Session": None})

    def luu_ma_khoi_phuc(self, ma_nguoi_dung: str, ma_xac_thuc: str, han_su_dung: str):
        self.cap_nhat(ma_nguoi_dung, {
            "ResetToken": {
                "Token": ma_xac_thuc,
                "Expire": han_su_dung
            }
        })
    def xoa_ma_khoi_phuc(self, ma_nguoi_dung: str):
        self.cap_nhat(ma_nguoi_dung, {"ResetToken": None})
    def tang_so_lan_thu(self, ma_nguoi_dung: str) -> int:
        data = self.doc_tat_ca()
        for u in data:
            if u["MaND"] == ma_nguoi_dung:
                u["SoLanThu"] = u.get("SoLanThu", 0) + 1
                self.ghi_tat_ca(data)
                return u["SoLanThu"]

        return 0
    def khoa_tai_khoan(self, ma_nguoi_dung: str, thoi_gian_khoa: str):
        self.cap_nhat(ma_nguoi_dung, {
            "TrangThai": "BI_KHOA",
            "ThoiGianKhoa": thoi_gian_khoa
        })
