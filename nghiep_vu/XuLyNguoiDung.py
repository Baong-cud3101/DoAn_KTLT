import hashlib
import uuid
from du_lieu.kho_luu_tru.LuuTruNguoiDung import LuuTruNguoiDung
from nghiep_vu.KiemTra import KiemTra

class XuLyNguoiDung:
    def __init__(self):
        self.luu_tru = LuuTruNguoiDung()

    def _ma_hoa_mat_khau(self, password):
        """Mã hóa SHA-256 cho mật khẩu."""
        return hashlib.sha256(password.encode()).hexdigest()

    def dang_ky(self, username, password, email, full_name):
        # 1. Kiểm tra định dạng
        if not KiemTra.la_mat_khau_manh(password):
            return False, "Mật khẩu phải có ít nhất 6 ký tự."
        if not KiemTra.la_email_hop_le(email):
            return False, "Email không đúng định dạng."

        # 2. Kiểm tra trùng lặp
        if self.luu_tru.tim_theo_username(username):
            return False, "Tên đăng nhập đã tồn tại."

        # 3. Tạo người dùng mới
        nguoi_dung_moi = {
            "MaND": str(uuid.uuid4())[:8], # Tạo mã định danh ngắn
            "TenDangNhap": username,
            "MatKhau": self._ma_hoa_mat_khau(password),
            "Email": email,
            "HoTen": full_name,
            "NgayTao": "2024-03-27" # Có thể dùng datetime.now()
        }

        if self.luu_tru.luu_nguoi_dung(nguoi_dung_moi):
            return True, "Đăng ký thành công."
        return False, "Lỗi hệ thống khi lưu dữ liệu."

    def dang_nhap(self, username, password):
        user = self.luu_tru.tim_theo_username(username)
        if not user:
            return None, "Tên đăng nhập không tồn tại."
        
        # So sánh mật khẩu đã mã hóa
        if user["MatKhau"] == self._ma_hoa_mat_khau(password):
            return user, "Đăng nhập thành công."
        return None, "Mật khẩu không chính xác."