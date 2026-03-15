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