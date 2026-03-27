class DieuKhienGiaoDich:
    def them_giao_dich(self, ma_nguoi_dung: str, du_lieu: dict): pass
    def lay_lich_su(self, ma_nguoi_dung: str, trang: int): pass
    def tim_kiem(self, ma_nguoi_dung: str, bo_loc: dict): pass
    def xoa_giao_dich(self, ma_nguoi_dung: str, ma_giao_dich: str): pass


from nghiep_vu.giao_dich.XuLyGiaoDich import XuLyGiaoDich
from du_lieu.LuuTruGiaoDich import LuuTruGiaoDich
from nghiep_vu.shared.KiemTra import KiemTraDuLieu
import uuid
from datetime import datetime
class DieuKhienGiaoDich:
    def __init__(self):
        self.xu_ly = XuLyGiaoDich()
        self.luu_tru = LuuTruGiaoDich()
        self.kiem_tra = KiemTraDuLieu()
    def them_giao_dich(self, ma_nguoi_dung: str, du_lieu: dict):
        so_tien = du_lieu.get("SoTien")
        if self.kiem_tra.kiem_tra_rong(so_tien):
            return {"success": False, "message": "SO_TIEN_RONG"}
        if not self.kiem_tra.kiem_tra_kieu_so(so_tien):
            return {"success": False, "message": "SO_TIEN_KHONG_HOP_LE"}
        if float(so_tien) <= 0:
            return {"success": False, "message": "SO_TIEN_PHAI_LON_HON_0"}
        ma_gd = "GD_" + str(uuid.uuid4())[:8]

        giao_dich = {
            "MaGD": ma_gd,
            "MaND": ma_nguoi_dung,
            "Ngay": du_lieu.get("Ngay", datetime.now().strftime("%Y-%m-%d")),
            "SoTien": float(so_tien),
            "Loai": du_lieu.get("Loai"),  # Thu / Chi
            "MaDM": du_lieu.get("MaDM"),
            "MoTa": du_lieu.get("MoTa", "")
        }
        giao_dich = self.xu_ly.phan_loai_tu_dong(giao_dich)
        canh_bao = self.xu_ly.kiem_tra_ngan_sach(giao_dich)
        self.luu_tru.luu(giao_dich)
        return {
            "success": True,
            "data": giao_dich,
            "canh_bao": canh_bao
        }
    def lay_lich_su(self, ma_nguoi_dung: str, trang: int):
        danh_sach = self.luu_tru.doc_tat_ca()
        ds_user = [gd for gd in danh_sach if gd["MaND"] == ma_nguoi_dung]
        per_page = 10
        start = (trang - 1) * per_page
        end = start + per_page
        return {
            "success": True,
            "data": ds_user[start:end],
            "tong": len(ds_user)
        }
    def tim_kiem(self, ma_nguoi_dung: str, bo_loc: dict):
        danh_sach = self.luu_tru.doc_tat_ca()
        ket_qua = []
        for gd in danh_sach:
            if gd["MaND"] != ma_nguoi_dung:
                continue
            if bo_loc.get("MaDM") and gd["MaDM"] != bo_loc["MaDM"]:
                continue
            if bo_loc.get("Loai") and gd["Loai"] != bo_loc["Loai"]:
                continue
            if bo_loc.get("MinTien") and gd["SoTien"] < bo_loc["MinTien"]:
                continue
            if bo_loc.get("MaxTien") and gd["SoTien"] > bo_loc["MaxTien"]:
                continue
            ket_qua.append(gd)
        return {
            "success": True,
            "data": ket_qua
        }
    def xoa_giao_dich(self, ma_nguoi_dung: str, ma_giao_dich: str):
        danh_sach = self.luu_tru.doc_tat_ca()
        moi = [
            gd for gd in danh_sach
            if not (gd["MaGD"] == ma_giao_dich and gd["MaND"] == ma_nguoi_dung)
        ]
        self.luu_tru.ghi_tat_ca(moi)
        return {"success": True}
