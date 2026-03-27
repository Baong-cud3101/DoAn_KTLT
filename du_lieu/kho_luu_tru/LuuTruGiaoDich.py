from du_lieu.quan_ly_file.DocGhiJson import DocGhiJson
from du_lieu.quan_ly_file.DuongDanFile import DuongDanFile

class LuuTruGiaoDich:
    def __init__(self):
        self.duong_dan = DuongDanFile.GIAO_DICH

    def doc_tat_ca(self) -> list:
        return DocGhiJson.doc(self.duong_dan)

    def ghi_tat_ca(self, du_lieu: list) -> bool:
        return DocGhiJson.ghi(self.duong_dan, du_lieu)

    def loc_du_lieu(self, ma_nguoi_dung: str, bo_loc: dict) -> list:
        danh_sach = self.doc_tat_ca()
        ket_qua = []
        for gd in danh_sach:
            if gd.get("MaND") != ma_nguoi_dung:
                continue
            # Kiểm tra các điều kiện lọc nếu có trong bo_loc
            if bo_loc.get("Loai") and gd.get("Loai") != bo_loc["Loai"]:
                continue
            if bo_loc.get("MaDM") and gd.get("MaDM") != bo_loc["MaDM"]:
                continue
            if "MinTien" in bo_loc and gd.get("SoTien", 0) < bo_loc["MinTien"]:
                continue
            if "MaxTien" in bo_loc and gd.get("SoTien", 0) > bo_loc["MaxTien"]:
                continue
            if bo_loc.get("TuNgay") and gd.get("Ngay") < bo_loc["TuNgay"]:
                continue
            if bo_loc.get("DenNgay") and gd.get("Ngay") > bo_loc["DenNgay"]:
                continue
            ket_qua.append(gd)
        return ket_qua

    def luu(self, giao_dich: dict) -> str:
        danh_sach = self.doc_tat_ca()
        danh_sach.append(giao_dich)
        if self.ghi_tat_ca(danh_sach):
            return giao_dich.get("MaGD")
        return ""

    def luu_hang_loat(self, danh_sach_moi: list) -> int:
        danh_sach_hien_tai = self.doc_tat_ca()
        danh_sach_hien_tai.extend(danh_sach_moi)
        if self.ghi_tat_ca(danh_sach_hien_tai):
            return len(danh_sach_moi)
        return 0

    def cap_nhat(self, ma_dinh_danh: str, truong_du_lieu: dict) -> bool:
        danh_sach = self.doc_tat_ca()
        da_thay_doi = False
        for gd in danh_sach:
            if gd.get("MaGD") == ma_dinh_danh:
                gd.update(truong_du_lieu)
                da_thay_doi = True
                break
        if da_thay_doi:
            return self.ghi_tat_ca(danh_sach)
        return False

    def xoa(self, ma_dinh_danh: str) -> bool:
        danh_sach = self.doc_tat_ca()
        moi = [gd for gd in danh_sach if gd.get("MaGD") != ma_dinh_danh]
        if len(moi) < len(danh_sach):
            return self.ghi_tat_ca(moi)
        return False

    def tim_theo_id(self, ma_dinh_danh: str) -> dict or None:
        danh_sach = self.doc_tat_ca()
        for gd in danh_sach:
            if gd.get("MaGD") == ma_dinh_danh:
                return gd
        return None

    def lay_theo_danh_muc(self, ma_nguoi_dung: str, ma_danh_muc: str) -> list:
        danh_sach = self.doc_tat_ca()
        return [gd for gd in danh_sach if gd.get("MaND") == ma_nguoi_dung and gd.get("MaDM") == ma_danh_muc]