class XuLyLaiSuat:
    @staticmethod
    def tinh_gia_tri_tuong_lai(so_tien_goc, lai_suat_nam_phan_tram, so_thang):
        # Công thức TVM lãi kép hàng tháng: FV = P * (1 + r/12)^n
        lai_suat_thang = (lai_suat_nam_phan_tram / 100) / 12
        fv = so_tien_goc * ((1 + lai_suat_thang) ** so_thang)
        tien_lai = fv - so_tien_goc
        return round(fv, 2), round(tien_lai, 2)

    @staticmethod
    def de_xuat_goi_tiet_kiem_toi_uu(danh_sach_lai_suat, so_tien, so_thang):
        # danh_sach_lai_suat format: [{"ngan_hang": "VCB", "lai_suat": 6.1, "ky_han": 12}, ...]
        goi_phu_hop = [goi for goi in danh_sach_lai_suat if goi["ky_han"] == so_thang]
        goi_phu_hop.sort(key=lambda x: x["lai_suat"], reverse=True)
        return goi_phu_hop[:3] if goi_phu_hop else []