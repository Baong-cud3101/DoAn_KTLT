#class LuuTruNganSach:
    #DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/ngan_sach.json'
    #def lay_theo_danh_muc(self, ma_nguoi_dung: str, danh_muc: str) -> dict: pass
    #def luu(self, ngan_sach: dict): pass
    #def cap_nhat_da_chi(self, ma_nguoi_dung: str, danh_muc: str, so_tien_thay_doi: float): pass

import json
import os
import uuid
class LuuTruNganSach:
    DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/ngan_sach.json'
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

    def lay_theo_danh_muc(self, ma_nguoi_dung: str, danh_muc: str) -> dict | None:
        danh_sach = self.doc_tat_ca()
        for ns in danh_sach:
            if ns.get("MaND") != ma_nguoi_dung:
                continue
            for muc in ns.get("DanhMuc", []):
                if muc.get("MaDM") == danh_muc:
                    return muc
        return None

    def luu(self, ngan_sach: dict):
        danh_sach = self.doc_tat_ca()
        if "MaNS" not in ngan_sach:
            ngan_sach["MaNS"] = "NS_" + str(uuid.uuid4())[:8]
        for i, ns in enumerate(danh_sach):
            if ns.get("MaND") == ngan_sach.get("MaND"):
                danh_sach[i] = ngan_sach
                self.ghi_tat_ca(danh_sach)
                return
        danh_sach.append(ngan_sach)
        self.ghi_tat_ca(danh_sach)

    def cap_nhat_da_chi(self, ma_nguoi_dung: str, danh_muc: str, so_tien_thay_doi: float):
        danh_sach = self.doc_tat_ca()
        for ns in danh_sach:
            if ns.get("MaND") != ma_nguoi_dung:
                continue
            for muc in ns.get("DanhMuc", []):
                if muc.get("MaDM") != danh_muc:
                    continue
                if "DaChi" not in muc:
                    muc["DaChi"] = 0
                muc["DaChi"] += so_tien_thay_doi
                if muc["DaChi"] < 0:
                    muc["DaChi"] = 0
                self.ghi_tat_ca(danh_sach)
                return
