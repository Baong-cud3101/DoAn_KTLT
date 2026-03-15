class XuLyNganSach:
    NGUONG_CANH_BAO: float = 0.70
    NGUONG_NGHIEM_TRONG: float = 1.00
    def kiem_tra_ngan_sach(self, ma_nguoi_dung: str, danh_muc: str, so_tien_moi: float) -> dict: pass
    def xac_thuc_ngan_sach(self, gioi_han: dict, thu_nhap: float) -> bool: pass
    def luu_ngan_sach(self, ma_nguoi_dung: str, du_lieu: dict): pass
    def de_xuat_ngan_sach(self, ma_nguoi_dung: str) -> dict: pass
    def lay_muc_do_canh_bao(self, ty_le: float) -> str: pass