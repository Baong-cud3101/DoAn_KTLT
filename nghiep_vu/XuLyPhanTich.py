from du_lieu.kho_luu_tru.LuuTruGiaoDich import LuuTruGiaoDich

class XuLyPhanTich:
    def __init__(self):
        self.repo_giao_dich = LuuTruGiaoDich()

    def phan_tich_rui_ro_tin_dung(self, tong_thu_nhap, tong_nghia_vu_no):
        if tong_thu_nhap <= 0:
            return 100.0, "RỦI RO CAO"
        
        dti = (tong_nghia_vu_no / tong_thu_nhap) * 100
        
        if dti <= 35:
            trang_thai = "AN TOÀN"
        elif dti <= 45:
            trang_thai = "TRUNG BÌNH"
        else:
            trang_thai = "RỦI RO CAO"
            
        return round(dti, 2), trang_thai

    def du_bao_dong_tien_ngan_han(self, so_thang_gan_nhat=3):
        # Tính trung bình thu chi để dự báo tháng tiếp theo
        # Mã logic giả lập đơn giản phục vụ hiển thị (Linear moving average)
        du_lieu = self.repo_giao_dich.lay_danh_sach()
        tong_thu = sum(gd.get('so_tien', 0) for gd in du_lieu if gd.get('loai') == 'Thu')
        tong_chi = sum(gd.get('so_tien', 0) for gd in du_lieu if gd.get('loai') == 'Chi')
        
        # Giả định dữ liệu phân bổ đều
        trung_binh_thu = tong_thu / so_thang_gan_nhat if so_thang_gan_nhat > 0 else 0
        trung_binh_chi = tong_chi / so_thang_gan_nhat if so_thang_gan_nhat > 0 else 0
        
        return {
            "du_bao_thu_thang_toi": round(trung_binh_thu, 2),
            "du_bao_chi_thang_toi": round(trung_binh_chi, 2),
            "du_bao_tich_luy": round(trung_binh_thu - trung_binh_chi, 2)
        }