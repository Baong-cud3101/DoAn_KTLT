class XuLyExcelNghiepVu:
    def nhap_hang_loat(self, ma_nguoi_dung: str, danh_sach_dong: list) -> dict: pass



from du_lieu.LuuTruGiaoDich import LuuTruGiaoDich
from du_lieu.LuuTruCauHinh import LuuTruCauHinh
class XuLyGiaoDich:
    def __init__(self):
        self.luu_tru = LuuTruGiaoDich()
        self.cau_hinh = LuuTruCauHinh()
    def phan_loai_tu_dong(self, giao_dich: dict) -> dict:
        mo_ta = (giao_dich.get("MoTa") or "").lower()
        tu_khoa = self.cau_hinh.lay_tu_khoa()
        for ma_dm, ds_tu in tu_khoa.items():
            for tu in ds_tu:
                if tu.lower() in mo_ta:
                    giao_dich["MaDM"] = ma_dm
                    return giao_dich
        return giao_dich
    def kiem_tra_ngan_sach(self, giao_dich: dict):
        if giao_dich.get("Loai") != "Chi":
            return None
        ma_dm = giao_dich.get("MaDM")
        so_tien = giao_dich.get("SoTien")
        ngan_sach = {
            "an_uong": 5000000,
            "di_chuyen": 2000000,
            "giai_tri": 3000000
        }
        han_muc = ngan_sach.get(ma_dm)
        if not han_muc:
            return None
        if so_tien >= han_muc:
            return f"⚠️ Vượt ngân sách {ma_dm}"
        if so_tien >= 0.8 * han_muc:
            return f"⚠️ Gần đạt ngân sách {ma_dm}"
        return None
class XuLyExcelNghiepVu:
    def __init__(self):
        self.luu_tru = LuuTruGiaoDich()
    def nhap_hang_loat(self, ma_nguoi_dung: str, danh_sach_dong: list) -> dict:
        ket_qua = []
        loi = []
        for i, dong in enumerate(danh_sach_dong):
            try:
                giao_dich = {
                    "MaGD": f"GD_EXCEL_{i}",
                    "MaND": ma_nguoi_dung,
                    "Ngay": dong.get("Ngay"),
                    "SoTien": float(dong.get("SoTien", 0)),
                    "Loai": dong.get("Loai"),
                    "MaDM": dong.get("MaDM"),
                    "MoTa": dong.get("MoTa", "")
                }
                self.luu_tru.luu(giao_dich)
                ket_qua.append(giao_dich)
            except Exception as e:
                loi.append({
                    "dong": i,
                    "loi": str(e)
                })
        return {
            "thanh_cong": len(ket_qua),
            "that_bai": len(loi),
            "chi_tiet_loi": loi
        }
