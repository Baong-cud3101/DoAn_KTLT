from du_lieu.kho_luu_tru.LuuTruGiaoDich import LuuTruGiaoDich
from nghiep_vu.PhanLoaiTuDong import PhanLoaiTuDong
import uuid
from datetime import datetime

class XuLyGiaoDich:
    def __init__(self):
        self.repo = LuuTruGiaoDich()

    def tao_giao_dich(self, loai, so_tien, ngay, mo_ta):
        # UC-06: Tự động phân loại nếu không chọn danh mục thủ công
        danh_muc = PhanLoaiTuDong.phan_loai(mo_ta)
        
        giao_dich_moi = {
            "id": str(uuid.uuid4()),
            "loai": loai,
            "so_tien": float(so_tien),
            "danh_muc": danh_muc,
            "ngay": ngay,
            "mo_ta": mo_ta,
            "ngay_tao": datetime.now().isoformat()
        }
        self.repo.them_moi(giao_dich_moi)
        return giao_dich_moi

    def tim_kiem_giao_dich(self, tu_khoa="", loai="", tu_ngay=None, den_ngay=None):
        du_lieu = self.repo.lay_danh_sach()
        ket_qua = []
        for gd in du_lieu:
            match = True
            if tu_khoa and tu_khoa.lower() not in gd.get("mo_ta", "").lower():
                match = False
            if loai and gd.get("loai") != loai:
                match = False
            if tu_ngay and gd.get("ngay") < tu_ngay:
                match = False
            if den_ngay and gd.get("ngay") > den_ngay:
                match = False
            
            if match:
                ket_qua.append(gd)
        return sorted(ket_qua, key=lambda x: x['ngay'], reverse=True)
        
    def xoa_giao_dich(self, id_giao_dich):
        danh_sach = self.repo.lay_danh_sach()
        danh_sach_moi = [gd for gd in danh_sach if gd.get("id") != id_giao_dich]
        self.repo.cap_nhat_du_lieu(danh_sach_moi)