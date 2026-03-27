from du_lieu.kho_luu.tru.LuuTruNganSach import LuuTruNganSach
class XuLyNganSach:
    NGUONG_CANH_BAO: float = 0.70
    NGUONG_NGHIEM_TRONG: float = 1.00
    def __init__(self):
        self.luu_tru = LuuTruNganSach()
    def kiem_tra_ngan_sach(self, du_lieu: dict):
        thu_nhap = du_lieu.get("ThuNhap", 0)
        tong_ngan_sach = sum(
            muc.get("HanMuc", 0) for muc in du_lieu.get("DanhMuc", [])
        )
        if thu_nhap <= 0:
            return False, "Thu nhap khong hop le"
        if tong_ngan_sach > thu_nhap:
            return False, "Tong ngan sach vuot qua thu nhap"
        return True, "Hop le"

    def xac_thuc_ngan_sach(self, gioi_han: dict, thu_nhap: float) -> bool:
        tong = sum(v for v in gioi_han.values())
        return tong <= thu_nhap

    def luu_ngan_sach(self, ma_nguoi_dung: str, du_lieu: dict):
        du_lieu["MaND"] = ma_nguoi_dung
        self.luu_tru.luu(du_lieu)

    def de_xuat_ngan_sach(self, ma_nguoi_dung: str) -> dict:
        return {
            "an_uong": 0.5,
            "giai_tri": 0.3,
            "tiet_kiem": 0.2
        }

    def lay_muc_do_canh_bao(self, ty_le: float) -> str:
        if ty_le >= self.NGUONG_NGHIEM_TRONG:
            return "NGHIEM_TRONG"
        if ty_le >= self.NGUONG_CANH_BAO:
            return "CANH_BAO"
        return "AN_TOAN"

    def kiem_tra_canh_bao(self, ma_nguoi_dung: str, danh_muc: str, so_tien: float):
        danh_sach = self.luu_tru.doc_tat_ca()
        for ns in danh_sach:
            if ns.get("MaND") != ma_nguoi_dung:
                continue
            for muc in ns.get("DanhMuc", []):
                if muc.get("MaDM") != danh_muc:
                    continue
                han_muc = muc.get("HanMuc", 0)
                if han_muc == 0:
                    return None
                ty_le = so_tien / han_muc
                muc_do = self.lay_muc_do_canh_bao(ty_le)
                if muc_do == "AN_TOAN":
                    return None
                return {
                    "muc_do": muc_do,
                    "ty_le": round(ty_le, 2),
                    "thong_bao": f"Chi tieu {danh_muc} da dat {int(ty_le*100)}%"
                }
        return None