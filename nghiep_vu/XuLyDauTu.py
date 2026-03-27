from du_lieu.kho_luu_tru.LuuTruDauTu import LuuTruDauTu
from du_lieu.kho_luu_tru.LuuTruTietKiem import LuuTruTietKiem
import uuid

class XuLyDauTu:
    def __init__(self):
        self.repo_dau_tu = LuuTruDauTu()
        self.repo_tiet_kiem = LuuTruTietKiem()

    def mo_so_tiet_kiem(self, so_tien, ky_han, lai_suat):
        so_moi = {
            "id": str(uuid.uuid4()),
            "so_tien": float(so_tien),
            "ky_han": int(ky_han),
            "lai_suat": float(lai_suat),
            "trang_thai": "DangHoatDong"
        }
        self.repo_tiet_kiem.luu_so_tiet_kiem(so_moi)
        return so_moi

    def tinh_pnl_vang(self, gia_mua_vao, so_luong, gia_thi_truong_hien_tai):
        tong_von = float(gia_mua_vao) * float(so_luong)
        tong_gia_tri_hien_tai = float(gia_thi_truong_hien_tai) * float(so_luong)
        loi_nhuan = tong_gia_tri_hien_tai - tong_von
        return {
            "tong_von": tong_von,
            "tong_gia_tri": tong_gia_tri_hien_tai,
            "loi_nhuan": loi_nhuan,
            "phan_tram_pnl": round((loi_nhuan / tong_von) * 100, 2) if tong_von > 0 else 0
        }