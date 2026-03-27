#class LuuTruGiaoDich:
    #DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/giao_dich.json'
    #def loc_du_lieu(self, ma_nguoi_dung: str, bo_loc: dict) -> list: pass
    #def luu(self, giao_dich: dict) -> str: pass
    #def luu_hang_loat(self, danh_sach_giao_dich: list) -> int: pass
    #def cap_nhat(self, ma_dinh_danh: str, truong_du_lieu: dict) -> bool: pass
    #def xoa(self, ma_dinh_danh: str) -> bool: pass
    #def tim_khoan_vay_theo_ma_giao_dich(self, ma_dinh_danh: str) -> dict | None: pass
    #def lay_theo_danh_muc(self, ma_nguoi_dung: str, danh_muc: str, ky_han: str) -> list: pass


import json
import os
class LuuTruGiaoDich:
    DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/giao_dich.json'
    def __init__(self):
        os.makedirs(os.path.dirname(self.DUONG_DAN_TEP), exist_ok=True)

        if not os.path.exists(self.DUONG_DAN_TEP):
            with open(self.DUONG_DAN_TEP, "w", encoding="utf-8") as f:
                json.dump([], f)

    def doc_tat_ca(self) -> list:
        try:
            with open(self.DUONG_DAN_TEP, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def ghi_tat_ca(self, du_lieu: list):
        with open(self.DUONG_DAN_TEP, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, indent=4, ensure_ascii=False)

    def loc_du_lieu(self, ma_nguoi_dung: str, bo_loc: dict) -> list:
        danh_sach = self.doc_tat_ca()
        ket_qua = []
        for gd in danh_sach:
            if gd.get("MaND") != ma_nguoi_dung:
                continue
            if bo_loc.get("Loai") and gd.get("Loai") != bo_loc["Loai"]:
                continue
            if bo_loc.get("MaDM") and gd.get("MaDM") != bo_loc["MaDM"]:
                continue
            if bo_loc.get("MinTien") and gd.get("SoTien", 0) < bo_loc["MinTien"]:
                continue
            if bo_loc.get("MaxTien") and gd.get("SoTien", 0) > bo_loc["MaxTien"]:
                continue
            ket_qua.append(gd)
        return ket_qua

    def luu(self, giao_dich: dict) -> str:
        danh_sach = self.doc_tat_ca()
        danh_sach.append(giao_dich)
        self.ghi_tat_ca(danh_sach)
        return giao_dich.get("MaGD")

    def xoa(self, ma_dinh_danh: str, ma_nguoi_dung: str = None) -> bool:
        danh_sach = self.doc_tat_ca()
        moi = []
        da_xoa = False
        for gd in danh_sach:
            if gd.get("MaGD") == ma_dinh_danh:
                if ma_nguoi_dung and gd.get("MaND") != ma_nguoi_dung:
                    moi.append(gd)
                    continue
                da_xoa = True
                continue
            moi.append(gd)
        if not da_xoa:
            return False
        self.ghi_tat_ca(moi)
        return True

    def cap_nhat(self, ma_dinh_danh: str, truong_du_lieu: dict) -> bool:
        danh_sach = self.doc_tat_ca()
        for gd in danh_sach:
            if gd.get("MaGD") == ma_dinh_danh:
                gd.update(truong_du_lieu)
                self.ghi_tat_ca(danh_sach)
                return True
        return False

    def tim_theo_id(self, ma_dinh_danh: str):
        danh_sach = self.doc_tat_ca()
        for gd in danh_sach:
            if gd.get("MaGD") == ma_dinh_danh:
                return gd
        return None
