#class DieuKhienGiaoDich:
    #def them_giao_dich(self, ma_nguoi_dung: str, du_lieu: dict): pass
    #def lay_lich_su(self, ma_nguoi_dung: str, trang: int): pass
    #def tim_kiem(self, ma_nguoi_dung: str, bo_loc: dict): pass
    #def xoa_giao_dich(self, ma_nguoi_dung: str, ma_giao_dich: str): pass


from nghiep_vu.giao_dich.XuLyGiaoDich import XuLyGiaoDich
from du_lieu.LuuTruGiaoDich import LuuTruGiaoDich
class DieuKhienGiaoDich:
    def __init__(self):
        self.xu_ly = XuLyGiaoDich()
        self.luu_tru = LuuTruGiaoDich()
    def them_giao_dich(self, ma_nguoi_dung: str, du_lieu: dict):
        du_lieu["MaND"] = ma_nguoi_dung
        ket_qua = self.xu_ly.xu_ly_giao_dich(du_lieu)
        giao_dich = ket_qua["giao_dich"]
        canh_bao = ket_qua["canh_bao"]
        self.luu_tru.luu(giao_dich)
        return {
            "success": True,
            "giao_dich": giao_dich,
            "canh_bao": canh_bao
        }

    def lay_lich_su(self, ma_nguoi_dung: str, trang: int = 1):
        danh_sach = self.luu_tru.doc_tat_ca()
        ket_qua = [
            gd for gd in danh_sach
            if gd.get("MaND") == ma_nguoi_dung
        ]
        return ket_qua
    def tim_kiem(self, ma_nguoi_dung: str, bo_loc: dict):
        ket_qua = self.luu_tru.loc_du_lieu(ma_nguoi_dung, bo_loc)
        return {
            "success": True,
            "data": ket_qua
        }

    def xoa_giao_dich(self, ma_nguoi_dung: str, ma_giao_dich: str):
        thanh_cong = self.luu_tru.xoa(ma_giao_dich, ma_nguoi_dung)
        if not thanh_cong:
            return {
                "success": False,
                "message": "Khong tim thay hoac khong co quyen xoa"
            }
        return {
            "success": True,
            "message": "Da xoa giao dich"
        }
