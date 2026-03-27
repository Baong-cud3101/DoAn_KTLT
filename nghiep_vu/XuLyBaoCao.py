from du_lieu.kho_luu_tru.LuuTruGiaoDich import LuuTruGiaoDich
import pandas as pd
import os
class XuLyBaoCao:
    def __init__(self):
        self.repo_giao_dich = LuuTruGiaoDich()

    def thong_ke_tong_quan(self, thang, nam):
        du_lieu = self.repo_giao_dich.lay_danh_sach()
        tong_thu = 0
        tong_chi = 0
        for gd in du_lieu:
            ngay_gd = gd.get('ngay', '')
            if ngay_gd.startswith(f"{nam}-{thang:02d}"):
                if gd.get('loai') == 'Thu':
                    tong_thu += gd.get('so_tien', 0)
                elif gd.get('loai') == 'Chi':
                    tong_chi += gd.get('so_tien', 0)
        
        return {
            "tong_thu": tong_thu,
            "tong_chi": tong_chi,
            "so_du_kha_dung": tong_thu - tong_chi
        }

    def chi_tiet_co_cau_chi_tieu(self, thang, nam):
        du_lieu = self.repo_giao_dich.lay_danh_sach()
        co_cau = {}
        tong_chi = 0
        for gd in du_lieu:
            ngay_gd = gd.get('ngay', '')
            if ngay_gd.startswith(f"{nam}-{thang:02d}") and gd.get('loai') == 'Chi':
                danh_muc = gd.get('danh_muc', 'Khác')
                so_tien = gd.get('so_tien', 0)
                co_cau[danh_muc] = co_cau.get(danh_muc, 0) + so_tien
                tong_chi += so_tien
        
        phan_tram = {}
        if tong_chi > 0:
            for dm, tien in co_cau.items():
                phan_tram[dm] = round((tien / tong_chi) * 100, 2)
        return phan_tram


    # Bổ sung vào class XuLyBaoCao
    def xuat_bao_cao_excel(self, duong_dan_luu, thang, nam):
        du_lieu = self.repo_giao_dich.lay_danh_sach()
        du_lieu_loc = [gd for gd in du_lieu if gd.get('ngay', '').startswith(f"{nam}-{thang:02d}")]
        
        if not du_lieu_loc:
            return False
            
        df = pd.DataFrame(du_lieu_loc)
        df.rename(columns={
            "ngay": "Ngày giao dịch",
            "danh_muc": "Danh mục",
            "mo_ta": "Mô tả",
            "loai": "Loại",
            "so_tien": "Số tiền"
        }, inplace=True)
        
        df.to_excel(duong_dan_luu, index=False, columns=["Ngày giao dịch", "Danh mục", "Mô tả", "Loại", "Số tiền"])
        return os.path.exists(duong_dan_luu)