class LuuTruCauHinh:
    DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/cau_hinh.json'
    def lay_tat_ca_lai_suat_ngan_hang(self) -> list: pass
    def lay_tu_khoa(self) -> dict: pass
    def cap_nhat(self, truong_du_lieu: dict): pass



import json
import os
class LuuTruCauHinh:
    DUONG_DAN_TEP: str = 'du_lieu/file_du_lieu/cau_hinh.json'

    def __init__(self):
        os.makedirs(os.path.dirname(self.DUONG_DAN_TEP), exist_ok=True)
        if not os.path.exists(self.DUONG_DAN_TEP):
            with open(self.DUONG_DAN_TEP, "w", encoding="utf-8") as f:
                json.dump({}, f)
    def doc_tat_ca(self) -> dict:
        try:
            with open(self.DUONG_DAN_TEP, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    def lay_tat_ca_lai_suat_ngan_hang(self) -> list:
        data = self.doc_tat_ca()
        return data.get("lai_suat_ngan_hang", [])
    def lay_tu_khoa(self) -> dict:
        data = self.doc_tat_ca()
        return data.get("tu_khoa", {})
    def cap_nhat(self, truong_du_lieu: dict):
        data = self.doc_tat_ca()
        data.update(truong_du_lieu)
        with open(self.DUONG_DAN_TEP, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
