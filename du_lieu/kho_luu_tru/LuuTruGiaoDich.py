class LuuTruGiaoDich:
    DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/giao_dich.json'
    def loc_du_lieu(self, ma_nguoi_dung: str, bo_loc: dict) -> list: pass
    def luu(self, giao_dich: dict) -> str: pass
    def luu_hang_loat(self, danh_sach_giao_dich: list) -> int: pass
    def cap_nhat(self, ma_dinh_danh: str, truong_du_lieu: dict) -> bool: pass
    def xoa(self, ma_dinh_danh: str) -> bool: pass
    def tim_khoan_vay_theo_ma_giao_dich(self, ma_dinh_danh: str) -> dict | None: pass
    def lay_theo_danh_muc(self, ma_nguoi_dung: str, danh_muc: str, ky_han: str) -> list: pass