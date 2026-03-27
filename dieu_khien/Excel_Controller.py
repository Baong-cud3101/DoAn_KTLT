import pandas as pd
from nghiep_vu.giao_dich.XuLyGiaoDich import XuLyExcelNghiepVu
class DieuKhienExcel:
    def __init__(self):
        self.xu_ly = XuLyExcelNghiepVu()
    def nhap_excel(self, ma_nguoi_dung: str, tap_tin) -> dict:
        try:
            df = pd.read_excel(tap_tin)
        except Exception as e:
            return {
                "success": False,
                "message": f"Loi doc file: {str(e)}"
            }
        danh_sach = df.to_dict(orient="records")
        if not danh_sach:
            return {
                "success": False,
                "message": "File khong co du lieu"
            }
        ket_qua = self.xu_ly.nhap_hang_loat(ma_nguoi_dung, danh_sach)
        return {
            "success": True,
            "tong_dong": len(danh_sach),
            "thanh_cong": ket_qua.get("thanh_cong", 0),
            "that_bai": ket_qua.get("that_bai", 0),
            "chi_tiet_loi": ket_qua.get("chi_tiet_loi", [])
        }
