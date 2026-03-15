class XuLyPhanTich:
    SO_THANG_LICH_SU_TOI_THIEU: int = 24
    MUC_DTI_CAO: float = 0.50
    MUC_DTI_TRUNG_BINH: float = 0.35

    def du_bao(self, ma_nguoi_dung: str, so_nam: int) -> dict: pass
    def hoi_quy_tuyen_tinh(self, truc_x: list, truc_y: list) -> tuple: pass
    def phong_chieu_tuong_lai(self, he_so_a: float, he_so_b: float, so_thang: int) -> list: pass
    def tinh_tong_luy_ke(self, danh_sach_gia_tri: list) -> list: pass
    def tinh_diem_rui_ro(self, ma_nguoi_dung: str, khoan_vay: dict) -> dict: pass
    def tinh_chi_so_dti(self, thu_nhap: float, danh_sach_no: list) -> float: pass
    def lay_nam_tham_hut(self, du_lieu_du_bao: list) -> list: pass