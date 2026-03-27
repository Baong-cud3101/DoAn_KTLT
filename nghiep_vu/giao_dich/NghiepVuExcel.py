#class XuLyGiaoDich:
    #def xu_ly_giao_dich(self, du_lieu: dict) -> dict: pass
    #def kiem_tra_giao_dich(self, du_lieu: dict) -> bool: pass
    #def tinh_tong_ket(self, ma_nguoi_dung: str, ky_han: str) -> dict: pass
    #def truy_van_giao_dich(self, ma_nguoi_dung: str, bo_loc: dict) -> list: pass
    #def kiem_tra_lien_ket_vay(self, ma_giao_dich: str) -> bool: pass

from du_lieu.LuuTruGiaoDich import LuuTruGiaoDich
from nghiep_vu.shared.KiemTra import KiemTraDuLieu
from nghiep_vu.giao_dich.XuLyGiaoDich import XuLyGiaoDich as XuLyCore
import uuid
from datetime import datetime
class XuLyGiaoDich:
    def __init__(self):
        self.luu_tru = LuuTruGiaoDich()
        self.kiem_tra = KiemTraDuLieu()
        self.core = XuLyCore()
    # XỬ LÝ 1 DÒNG GIAO DỊCH
    def xu_ly_giao_dich(self, du_lieu: dict) -> dict:
        if not self.kiem_tra_giao_dich(du_lieu):
            raise ValueError("DU_LIEU_KHONG_HOP_LE")
        giao_dich = {
            "MaGD": "GD_" + str(uuid.uuid4())[:8],
            "MaND": du_lieu.get("MaND"),
            "Ngay": du_lieu.get("Ngay") or datetime.now().strftime("%Y-%m-%d"),
            "SoTien": float(du_lieu.get("SoTien")),
            "Loai": du_lieu.get("Loai"),
            "MaDM": du_lieu.get("MaDM"),
            "MoTa": du_lieu.get("MoTa", "")
        }
        #phân loại tự động
        giao_dich = self.core.phan_loai_tu_dong(giao_dich)
        #kiểm tra ngân sách
        canh_bao = self.core.kiem_tra_ngan_sach(giao_dich)
        return {
            "giao_dich": giao_dich,
            "canh_bao": canh_bao
        }
    def kiem_tra_giao_dich(self, du_lieu: dict) -> bool:
        so_tien = du_lieu.get("SoTien")
        if self.kiem_tra.kiem_tra_rong(so_tien):
            return False
        if not self.kiem_tra.kiem_tra_kieu_so(so_tien):
            return False
        if float(so_tien) <= 0:
            return False
        if du_lieu.get("Loai") not in ["Thu", "Chi"]:
            return False
        return True
    def tinh_tong_ket(self, ma_nguoi_dung: str, ky_han: str) -> dict:
        danh_sach = self.luu_tru.doc_tat_ca()
        tong_thu = 0
        tong_chi = 0
        for gd in danh_sach:
            if gd.get("MaND") != ma_nguoi_dung:
                continue
            if gd.get("Loai") == "Thu":
                tong_thu += gd.get("SoTien", 0)
            elif gd.get("Loai") == "Chi":
                tong_chi += gd.get("SoTien", 0)
        return {
            "tong_thu": tong_thu,
            "tong_chi": tong_chi,
            "so_du": tong_thu - tong_chi
        }
        
    def truy_van_giao_dich(self, ma_nguoi_dung: str, bo_loc: dict) -> list:

        return self.luu_tru.loc_du_lieu(ma_nguoi_dung, bo_loc)

    def kiem_tra_lien_ket_vay(self, ma_giao_dich: str) -> bool:
        gd = self.luu_tru.tim_khoan_vay_theo_ma_giao_dich(ma_giao_dich)
        if not gd:
            return False
        return bool(gd.get("LienKetVay"))
