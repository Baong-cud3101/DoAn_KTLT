class KiemTraDuLieu:
    def kiem_tra_kieu_so(self, gia_tri) -> bool: pass
    def kiem_tra_rong(self, gia_tri) -> bool: pass

    class KiemTraDuLieu:
    def kiem_tra_kieu_so(self, gia_tri) -> bool:
        try:
            float(gia_tri)
            return True
        except:
            return False
    def kiem_tra_rong(self, gia_tri) -> bool:
        if gia_tri is None:
            return True
        if isinstance(gia_tri, str) and gia_tri.strip() == "":
            return True
        return False
