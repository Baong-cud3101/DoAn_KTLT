from du_lieu.kho_luu_tru.LuuTruVayNo import LuuTruVayNo
import uuid
from datetime import datetime
class XuLyVayNo:
    def __init__(self):
        self.repo = LuuTruVayNo()

    def tao_khoan_vay(self, ten_khoan_vay, so_tien, lai_suat_nam, so_thang_vay):
        lich_tra_no = self.sinh_lich_tra_no(so_tien, lai_suat_nam, so_thang_vay)
        khoan_vay = {
            "id": str(uuid.uuid4()),
            "ten": ten_khoan_vay,
            "so_tien_goc": float(so_tien),
            "lai_suat": float(lai_suat_nam),
            "ky_han": int(so_thang_vay),
            "du_no_hien_tai": float(so_tien),
            "lich_tra_no": lich_tra_no
        }
        self.repo.them_khoan_vay(khoan_vay)
        return khoan_vay

    def sinh_lich_tra_no(self, so_tien, lai_suat_nam, so_thang_vay):
        # Dư nợ giảm dần
        lai_suat_thang = (lai_suat_nam / 100) / 12
        goc_hang_thang = so_tien / so_thang_vay
        du_no = so_tien
        
        lich = []
        for ky in range(1, so_thang_vay + 1):
            lai_phai_tra = du_no * lai_suat_thang
            tong_tra = goc_hang_thang + lai_phai_tra
            lich.append({
                "ky": ky,
                "du_no_dau_ky": round(du_no, 2),
                "goc_phai_tra": round(goc_hang_thang, 2),
                "lai_phai_tra": round(lai_phai_tra, 2),
                "tong_tra": round(tong_tra, 2)
            })
            du_no -= goc_hang_thang
        return lich
    from datetime import datetime

    # Bổ sung vào class XuLyVayNo
    def cap_nhat_thanh_toan(self, id_khoan_vay, ky_thu, so_tien_tra):
        danh_sach = self.repo.lay_danh_sach()
        for kv in danh_sach:
            if kv.get("id") == id_khoan_vay:
                lich = kv.get("lich_tra_no", [])
                for ky in lich:
                    if ky.get("ky") == ky_thu and ky.get("trang_thai") != "DA_TRA":
                        if float(so_tien_tra) >= float(ky.get("tong_tra", 0)):
                            ky["trang_thai"] = "DA_TRA"
                            kv["du_no_hien_tai"] -= ky.get("goc_phai_tra", 0)
                            self.repo.cap_nhat_khoan_vay(kv)
                            return True
        return False

    def kiem_tra_qua_han(self, phi_phat_phan_tram=0.5):
        danh_sach = self.repo.lay_danh_sach()
        ngay_hien_tai = datetime.now().date()
        danh_sach_qua_han = []

        for kv in danh_sach:
            lich = kv.get("lich_tra_no", [])
            for ky in lich:
                if ky.get("trang_thai") not in ["DA_TRA", "QUA_HAN"]:
                    try:
                        ngay_den_han = datetime.strptime(ky.get("ngay_den_han", ""), "%Y-%m-%d").date()
                        if ngay_hien_tai > ngay_den_han:
                            ky["trang_thai"] = "QUA_HAN"
                            tien_phat = ky.get("lai_phai_tra", 0) * (phi_phat_phan_tram / 100)
                            ky["tong_tra"] = round(ky.get("tong_tra", 0) + tien_phat, 2)
                            if kv["id"] not in danh_sach_qua_han:
                                danh_sach_qua_han.append(kv["id"])
                    except ValueError:
                        continue
            self.repo.cap_nhat_khoan_vay(kv)
        return danh_sach_qua_han