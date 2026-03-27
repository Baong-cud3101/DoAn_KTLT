class ChuanHoa:
    @staticmethod
    def dinh_dang_tien_te(so_tien):
        try:
            return f"{float(so_tien):,.0f} đ".replace(',', '.')
        except (ValueError, TypeError):
            return "0 đ"

    @staticmethod
    def lam_sach_chuoi(chuoi):
        if not chuoi:
            return ""
        return " ".join(chuoi.strip().split())