class XuLyVayNo:
    DO_CHINH_XAC_PMT: int = 0
    TY_LE_PHAT: float = 0.005

    def xu_ly_khoan_vay(self, ma_nguoi_dung: str, du_lieu: dict) -> dict: pass
    def tao_lich_trinh(self, so_tien_goc: float, lai_suat: float, so_ky_han: int) -> list: pass
    def tinh_pmt(self, so_tien_goc: float, lai_suat_thang: float, so_ky_han: int) -> float: pass
    def ghi_nhan_thanh_toan(self, ma_khoan_vay: str, ma_ky_han: int, so_tien: float) -> dict: pass
    def kiem_tra_khoan_vay_qua_han(self): pass
    def tinh_phi_phat(self, ky_han: dict) -> float: pass
    def dong_khoan_vay(self, ma_khoan_vay: str): pass