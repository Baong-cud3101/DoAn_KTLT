from du_lieu.kho_luu_tru.LuuTruNganSach import LuuTruNganSach
from nghiep_vu.XuLyGiaoDich import XuLyGiaoDich
from datetime import datetime

class XuLyNganSach:
    def __init__(self):
        self.repo = LuuTruNganSach()
        self.logic_giao_dich = XuLyGiaoDich()

    def thiet_lap_ngan_sach(self, thang, nam, danh_muc, han_muc):
        ngan_sach = {
            "thang": thang,
            "nam": nam,
            "danh_muc": danh_muc,
            "han_muc": float(han_muc)
        }
        self.repo.luu_ngan_sach(ngan_sach)

    def kiem_tra_canh_bao_chi_tieu(self, thang, nam):
        danh_sach_ngan_sach = self.repo.lay_ngan_sach_theo_thang(thang, nam)
        giao_dich_trong_thang = self.logic_giao_dich.tim_kiem_giao_dich(
            loai="Chi", 
            tu_ngay=f"{nam}-{thang:02d}-01", 
            den_ngay=f"{nam}-{thang:02d}-31"
        )
        
        chi_tieu_thuc_te = {}
        for gd in giao_dich_trong_thang:
            dm = gd.get("danh_muc")
            chi_tieu_thuc_te[dm] = chi_tieu_thuc_te.get(dm, 0) + gd.get("so_tien", 0)

        canh_bao = []
        for ns in danh_sach_ngan_sach:
            dm = ns.get("danh_muc")
            han_muc = ns.get("han_muc", 0)
            da_chi = chi_tieu_thuc_te.get(dm, 0)
            
            if da_chi > han_muc:
                canh_bao.append({
                    "danh_muc": dm,
                    "trang_thai": "Vượt ngân sách",
                    "vuot_muc": da_chi - han_muc
                })
            elif da_chi >= han_muc * 0.8:
                canh_bao.append({
                    "danh_muc": dm,
                    "trang_thai": "Sắp vượt ngân sách",
                    "vuot_muc": 0
                })
        return canh_bao