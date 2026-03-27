#class DieuKhienNganSach:
    #def thiet_lap_ngan_sach(self, ma_nguoi_dung: str, du_lieu: dict): pass
    #def lay_trang_thai_ngan_sach(self, ma_nguoi_dung: str): pass
    #def kiem_tra_canh_bao(self, ma_nguoi_dung: str, danh_muc: str, so_tien: float): pass

from nghiep_vu.ngan_sach.XuLyNganSach import XuLyNganSach
from du_lieu.LuuTruNganSach import LuuTruNganSach
class DieuKhienNganSach:
    def __init__(self):
        self.xu_ly = XuLyNganSach()
        self.luu_tru = LuuTruNganSach()

    def thiet_lap_ngan_sach(self, ma_nguoi_dung: str, du_lieu: dict):
        du_lieu["MaND"] = ma_nguoi_dung
        hop_le, thong_bao = self.xu_ly.kiem_tra_ngan_sach(du_lieu)
        if not hop_le:
            return {
                "success": False,
                "message": thong_bao
            }
        self.luu_tru.luu(du_lieu)
        return {
            "success": True,
            "message": "Thiet lap ngan sach thanh cong"
        }
    def lay_trang_thai_ngan_sach(self, ma_nguoi_dung: str):
        danh_sach = self.luu_tru.doc_tat_ca()
        ket_qua = [
            ns for ns in danh_sach
            if ns.get("MaND") == ma_nguoi_dung
        ]
        return {
            "success": True,
            "data": ket_qua
        }

    def kiem_tra_canh_bao(self, ma_nguoi_dung: str, danh_muc: str, so_tien: float):
        canh_bao = self.xu_ly.kiem_tra_canh_bao(
            ma_nguoi_dung,
            danh_muc,
            so_tien
        )
        if not canh_bao:
            return {
                "canh_bao": None
            }
        return {
            "canh_bao": canh_bao
        }
