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