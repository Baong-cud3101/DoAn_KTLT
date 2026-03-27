from du_lieu.kho_luu_tru.LuuTruNguoiDung import LuuTruNguoiDung

class XuLyNguoiDung:
    def __init__(self):
        self.repo = LuuTruNguoiDung()

    def xac_thuc(self, email, mat_khau):
        danh_sach = self.repo.lay_danh_sach()
        for tk in danh_sach:
            if tk.get("email") == email and tk.get("mat_khau") == mat_khau:
                return True, tk
        return False, None