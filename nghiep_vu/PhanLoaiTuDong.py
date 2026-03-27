class PhanLoaiTuDong:
    TUDIEN_PHANLOAI = {
        "Ăn uống": ["highland", "kfc", "phở", "cơm", "coffee", "cafe", "starbucks", "nhà hàng", "trà sữa"],
        "Di chuyển": ["grab", "be", "gojek", "xăng", "vé xe", "taxi", "bảo dưỡng xe"],
        "Nhà cửa": ["tiền nhà", "điện", "nước", "internet", "vinhomes", "phí quản lý"],
        "Giải trí": ["cgv", "netflix", "spotify", "du lịch", "xem phim"],
        "Lương": ["lương", "thưởng", "cấp", "hoa hồng"],
        "Đầu tư": ["mua cổ phiếu", "trái phiếu", "gửi tiết kiệm"]
    }

    @staticmethod
    def phan_loai(mo_ta):
        if not mo_ta:
            return "Khác"
        mo_ta_lower = str(mo_ta).lower()
        for danh_muc, tu_khoas in PhanLoaiTuDong.TUDIEN_PHANLOAI.items():
            for tk in tu_khoas:
                if tk in mo_ta_lower:
                    return danh_muc
        return "Khác"