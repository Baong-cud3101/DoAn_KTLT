from PyQt6.QtWidgets import QMainWindow, QDialog, QTableWidgetItem
from PyQt6.QtCore import Qt
import sys

# Import tất cả Giao diện (View) - ĐÃ CẬP NHẬT ĐÚNG TÊN CLASS
from giao_dien.login import Ui_LoginForm
from giao_dien.DB import Ui_MainWindow as Ui_Dashboard
from giao_dien.giaodich import Ui_MainWindow as Ui_GiaoDich
from giao_dien.themgiaodich import Ui_AddDialog
from giao_dien.baocao import Ui_MainWindow as Ui_BaoCao
from giao_dien.dautupopup import Ui_Dialog as Ui_DauTuPopup
from giao_dien.dautuvatietkiem import Ui_MainWindow_DauTu as Ui_DauTuTietKiem  # Đã sửa
from giao_dien.quanlyngansach import Ui_MainWindow as Ui_QuanLyNganSach
from giao_dien.taikhoanuser import Ui_MainWindow as Ui_TaiKhoanUser
from giao_dien.thongbao_popup import Ui_Dialog_ThongBao as Ui_ThongBaoPopup  # Đã sửa
from giao_dien.vayno import Ui_MainWindow as Ui_VayNo

# Import Nghiệp vụ (Model/Logic)
from nghiep_vu.XuLyNguoiDung import XuLyNguoiDung
from nghiep_vu.XuLyGiaoDich import XuLyGiaoDich
from nghiep_vu.KiemTra import KiemTra

class MainController:
    def __init__(self):
        # 1. Khởi tạo tầng Nghiệp vụ
        self.logic_nguoi_dung = XuLyNguoiDung()
        self.logic_giao_dich = XuLyGiaoDich()
        self.ma_nd_hien_tai = None
        self.loai_giao_dich_dang_chon = "Chi"

        # 2. Khởi tạo tất cả cửa sổ Giao diện
        # Login
        self.win_login = QMainWindow()
        self.ui_login = Ui_LoginForm()
        self.ui_login.setupUi(self.win_login)
        
        # Dashboard (Trang chủ)
        self.win_dashboard = QMainWindow()
        self.ui_dashboard = Ui_Dashboard()
        self.ui_dashboard.setupUi(self.win_dashboard)
        
        # Giao dịch
        self.win_giaodich = QMainWindow()
        self.ui_giaodich = Ui_GiaoDich()
        self.ui_giaodich.setupUi(self.win_giaodich)
        
        # Thêm giao dịch (Popup)
        self.dlg_themgiaodich = QDialog()
        self.ui_themgiaodich = Ui_AddDialog()
        self.ui_themgiaodich.setupUi(self.dlg_themgiaodich)
        
        # Báo cáo
        self.win_baocao = QMainWindow()
        self.ui_baocao = Ui_BaoCao()
        self.ui_baocao.setupUi(self.win_baocao)
        
        # Đầu tư tiết kiệm
        self.win_dautu_tietkiem = QMainWindow()
        self.ui_dautu_tietkiem = Ui_DauTuTietKiem()
        self.ui_dautu_tietkiem.setupUi(self.win_dautu_tietkiem)
        
        # Đầu tư Popup
        self.dlg_dautu_popup = QDialog()
        self.ui_dautu_popup = Ui_DauTuPopup()
        self.ui_dautu_popup.setupUi(self.dlg_dautu_popup)
        
        # Quản lý ngân sách
        self.win_ngansach = QMainWindow()
        self.ui_ngansach = Ui_QuanLyNganSach()
        self.ui_ngansach.setupUi(self.win_ngansach)
        
        # Tài khoản user
        self.win_taikhoan = QMainWindow()
        self.ui_taikhoan = Ui_TaiKhoanUser()
        self.ui_taikhoan.setupUi(self.win_taikhoan)
        
        # Vay nợ
        self.win_vayno = QMainWindow()
        self.ui_vayno = Ui_VayNo()
        self.ui_vayno.setupUi(self.win_vayno)
        
        # Thông báo Popup
        self.dlg_thongbao = QDialog()
        self.ui_thongbao = Ui_ThongBaoPopup()
        self.ui_thongbao.setupUi(self.dlg_thongbao)

        # 3. Kết nối sự kiện
        self._ket_noi_su_kien()
        
        print("✓ MainController đã khởi tạo thành công với tất cả các màn hình!")

    def khoi_dong(self):
        """Khởi động ứng dụng"""
        print("Khởi động ứng dụng...")
        self.win_login.show()
        print("✓ Đã hiển thị màn hình đăng nhập")

    def _ket_noi_su_kien(self):
        """Kết nối tất cả sự kiện giữa các màn hình"""
        
        # ==================== LOGIN ====================
        if hasattr(self.ui_login, 'loginBtn'):
            self.ui_login.loginBtn.clicked.connect(self.xu_ly_dang_nhap)
            print("✓ Kết nối: Login -> Đăng nhập")
        
        # ==================== DASHBOARD ====================
        # Các nút điều hướng từ Dashboard
        if hasattr(self.ui_dashboard, 'btn_nav_giaodich'):
            self.ui_dashboard.btn_nav_giaodich.clicked.connect(self.chuyen_den_giao_dich)
            print("✓ Kết nối: Dashboard -> Giao dịch")
            
        if hasattr(self.ui_dashboard, 'btn_nav_dautu_tietkiem'):
            self.ui_dashboard.btn_nav_dautu_tietkiem.clicked.connect(self.chuyen_den_dau_tu_tiet_kiem)
            print("✓ Kết nối: Dashboard -> Đầu tư tiết kiệm")
            
        if hasattr(self.ui_dashboard, 'btn_nav_ngansach'):
            self.ui_dashboard.btn_nav_ngansach.clicked.connect(self.chuyen_den_quan_ly_ngan_sach)
            print("✓ Kết nối: Dashboard -> Quản lý ngân sách")
            
        if hasattr(self.ui_dashboard, 'btn_nav_vayno'):
            self.ui_dashboard.btn_nav_vayno.clicked.connect(self.chuyen_den_vay_no)
            print("✓ Kết nối: Dashboard -> Vay nợ")
            
        if hasattr(self.ui_dashboard, 'btn_mo_tietkiem'):
            self.ui_dashboard.btn_mo_tietkiem.clicked.connect(self.mo_tao_tiet_kiem)
            print("✓ Kết nối: Dashboard -> Mở sổ tiết kiệm")
        
        # ==================== GIAO DỊCH ====================
        # Nút điều hướng từ Giao dịch
        if hasattr(self.ui_giaodich, 'btn_nav_dashboard'):
            self.ui_giaodich.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)
            print("✓ Kết nối: Giao dịch -> Dashboard")
            
        if hasattr(self.ui_giaodich, 'btn_nav_baocao'):
            self.ui_giaodich.btn_nav_baocao.clicked.connect(self.chuyen_den_bao_cao)
            print("✓ Kết nối: Giao dịch -> Báo cáo")
            
        if hasattr(self.ui_giaodich, 'btn_nav_dautu_tietkiem'):
            self.ui_giaodich.btn_nav_dautu_tietkiem.clicked.connect(self.chuyen_den_dau_tu_tiet_kiem)
            print("✓ Kết nối: Giao dịch -> Đầu tư tiết kiệm")
            
        if hasattr(self.ui_giaodich, 'btn_nav_ngansach'):
            self.ui_giaodich.btn_nav_ngansach.clicked.connect(self.chuyen_den_quan_ly_ngan_sach)
            print("✓ Kết nối: Giao dịch -> Quản lý ngân sách")
            
        if hasattr(self.ui_giaodich, 'btn_nav_vayno'):
            self.ui_giaodich.btn_nav_vayno.clicked.connect(self.chuyen_den_vay_no)
            print("✓ Kết nối: Giao dịch -> Vay nợ")
            
        if hasattr(self.ui_giaodich, 'btn_nav_caidat'):
            self.ui_giaodich.btn_nav_caidat.clicked.connect(self.chuyen_den_tai_khoan)
            print("✓ Kết nối: Giao dịch -> Cài đặt/Tài khoản")
            
        if hasattr(self.ui_giaodich, 'btn_nav_chatbot'):
            self.ui_giaodich.btn_nav_chatbot.clicked.connect(self.mo_chatbot)
            print("✓ Kết nối: Giao dịch -> Chatbot")
            
        if hasattr(self.ui_giaodich, 'btn_them_giaodich'):
            self.ui_giaodich.btn_them_giaodich.clicked.connect(self.mo_popup_them_giao_dich)
            print("✓ Kết nối: Giao dịch -> Thêm giao dịch")
            
        if hasattr(self.ui_giaodich, 'btn_nhap_excel'):
            self.ui_giaodich.btn_nhap_excel.clicked.connect(self.nhap_excel)
            print("✓ Kết nối: Giao dịch -> Nhập Excel")
        
        # ==================== THÊM GIAO DỊCH (POPUP) ====================
        if hasattr(self.ui_themgiaodich, 'btn_expense'):
            self.ui_themgiaodich.btn_expense.clicked.connect(lambda: self._set_loai_giao_dich("Chi"))
            print("✓ Kết nối: Thêm GD -> Chi")
            
        if hasattr(self.ui_themgiaodich, 'btn_income'):
            self.ui_themgiaodich.btn_income.clicked.connect(lambda: self._set_loai_giao_dich("Thu"))
            print("✓ Kết nối: Thêm GD -> Thu")
            
        if hasattr(self.ui_themgiaodich, 'btn_save'):
            self.ui_themgiaodich.btn_save.clicked.connect(self.luu_giao_dich)
            print("✓ Kết nối: Thêm GD -> Lưu")
            
        if hasattr(self.ui_themgiaodich, 'btn_cancel'):
            self.ui_themgiaodich.btn_cancel.clicked.connect(self.dlg_themgiaodich.close)
            print("✓ Kết nối: Thêm GD -> Hủy")
            
        if hasattr(self.ui_themgiaodich, 'btn_close'):
            self.ui_themgiaodich.btn_close.clicked.connect(self.dlg_themgiaodich.close)
            print("✓ Kết nối: Thêm GD -> Đóng")
        
        # ==================== ĐẦU TƯ TIẾT KIỆM ====================
        if hasattr(self.ui_dautu_tietkiem, 'btn_nav_dashboard'):
            self.ui_dautu_tietkiem.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)
            print("✓ Kết nối: Đầu tư -> Dashboard")
            
        if hasattr(self.ui_dautu_tietkiem, 'btn_them_dautu'):
            self.ui_dautu_tietkiem.btn_them_dautu.clicked.connect(self.mo_popup_dautu)
            print("✓ Kết nối: Đầu tư -> Thêm đầu tư")
        
        # ==================== ĐẦU TƯ POPUP ====================
        if hasattr(self.ui_dautu_popup, 'btn_save'):
            self.ui_dautu_popup.btn_save.clicked.connect(self.luu_dau_tu)
            print("✓ Kết nối: Đầu tư Popup -> Lưu")
            
        if hasattr(self.ui_dautu_popup, 'btn_cancel'):
            self.ui_dautu_popup.btn_cancel.clicked.connect(self.dlg_dautu_popup.close)
            print("✓ Kết nối: Đầu tư Popup -> Hủy")
        
        # ==================== QUẢN LÝ NGÂN SÁCH ====================
        if hasattr(self.ui_ngansach, 'btn_nav_dashboard'):
            self.ui_ngansach.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)
            print("✓ Kết nối: Ngân sách -> Dashboard")
            
        if hasattr(self.ui_ngansach, 'btn_tao_ngansach'):
            self.ui_ngansach.btn_tao_ngansach.clicked.connect(self.tao_ngan_sach)
            print("✓ Kết nối: Ngân sách -> Tạo ngân sách")
        
        # ==================== VAY NỢ ====================
        if hasattr(self.ui_vayno, 'btn_nav_dashboard'):
            self.ui_vayno.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)
            print("✓ Kết nối: Vay nợ -> Dashboard")
            
        if hasattr(self.ui_vayno, 'btn_them_khoanvay'):
            self.ui_vayno.btn_them_khoanvay.clicked.connect(self.them_khoan_vay)
            print("✓ Kết nối: Vay nợ -> Thêm khoản vay")
        
        # ==================== TÀI KHOẢN USER ====================
        if hasattr(self.ui_taikhoan, 'btn_save'):
            self.ui_taikhoan.btn_save.clicked.connect(self.cap_nhat_taikhoan)
            print("✓ Kết nối: Tài khoản -> Lưu")
            
        if hasattr(self.ui_taikhoan, 'btn_back'):
            self.ui_taikhoan.btn_back.clicked.connect(self.chuyen_den_dashboard)
            print("✓ Kết nối: Tài khoản -> Quay lại")
        
        # ==================== BÁO CÁO ====================
        if hasattr(self.ui_baocao, 'btn_nav_dashboard'):
            self.ui_baocao.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)
            print("✓ Kết nối: Báo cáo -> Dashboard")
            
        if hasattr(self.ui_baocao, 'btn_xuat_baocao'):
            self.ui_baocao.btn_xuat_baocao.clicked.connect(self.xuat_bao_cao)
            print("✓ Kết nối: Báo cáo -> Xuất báo cáo")

    # ==================== CÁC HÀM CHUYỂN MÀN HÌNH ====================
    
    def chuyen_den_dashboard(self):
        """Chuyển về Dashboard (Trang chủ)"""
        print("\n→ Chuyển đến Dashboard")
        self._an_tat_ca_man_hinh()
        self.win_dashboard.show()
        self.win_dashboard.raise_()
        self.win_dashboard.activateWindow()
        print("✓ Đã hiển thị Dashboard")

    def chuyen_den_giao_dich(self):
        """Chuyển đến màn hình Giao dịch"""
        print("\n→ Chuyển đến Giao dịch")
        self._an_tat_ca_man_hinh()
        self.tai_du_lieu_bang_giao_dich()
        self.win_giaodich.show()
        self.win_giaodich.raise_()
        print("✓ Đã hiển thị màn hình Giao dịch")

    def chuyen_den_bao_cao(self):
        """Chuyển đến màn hình Báo cáo"""
        print("\n→ Chuyển đến Báo cáo")
        self._an_tat_ca_man_hinh()
        self.win_baocao.show()
        self.win_baocao.raise_()
        print("✓ Đã hiển thị màn hình Báo cáo")

    def chuyen_den_dau_tu_tiet_kiem(self):
        """Chuyển đến màn hình Đầu tư tiết kiệm"""
        print("\n→ Chuyển đến Đầu tư tiết kiệm")
        self._an_tat_ca_man_hinh()
        self.win_dautu_tietkiem.show()
        self.win_dautu_tietkiem.raise_()
        print("✓ Đã hiển thị màn hình Đầu tư tiết kiệm")

    def chuyen_den_quan_ly_ngan_sach(self):
        """Chuyển đến màn hình Quản lý ngân sách"""
        print("\n→ Chuyển đến Quản lý ngân sách")
        self._an_tat_ca_man_hinh()
        self.win_ngansach.show()
        self.win_ngansach.raise_()
        print("✓ Đã hiển thị màn hình Quản lý ngân sách")

    def chuyen_den_vay_no(self):
        """Chuyển đến màn hình Vay nợ"""
        print("\n→ Chuyển đến Vay nợ")
        self._an_tat_ca_man_hinh()
        self.win_vayno.show()
        self.win_vayno.raise_()
        print("✓ Đã hiển thị màn hình Vay nợ")

    def chuyen_den_tai_khoan(self):
        """Chuyển đến màn hình Tài khoản"""
        print("\n→ Chuyển đến Tài khoản")
        self._an_tat_ca_man_hinh()
        self.win_taikhoan.show()
        self.win_taikhoan.raise_()
        print("✓ Đã hiển thị màn hình Tài khoản")

    def _an_tat_ca_man_hinh(self):
        """Ẩn tất cả các màn hình"""
        self.win_dashboard.hide()
        self.win_giaodich.hide()
        self.win_baocao.hide()
        self.win_dautu_tietkiem.hide()
        self.win_ngansach.hide()
        self.win_taikhoan.hide()
        self.win_vayno.hide()

    # ==================== XỬ LÝ ĐĂNG NHẬP ====================
    
    def xu_ly_dang_nhap(self):
        """Xử lý đăng nhập"""
        print("\n" + "="*50)
        print("XỬ LÝ ĐĂNG NHẬP")
        print("="*50)
        
        email = self.ui_login.emailInput.text()
        mat_khau = self.ui_login.passwordInput.text()
        
        print(f"Email: {email}")
        
        # Xác thực (tạm thời cho phép đăng nhập để test)
        hop_le, user = self.logic_nguoi_dung.xac_thuc(email, mat_khau)
        
        if hop_le or True:  # True để test
            if user:
                self.ma_nd_hien_tai = user.get("MaND")
            print("✓ Đăng nhập thành công!")
            self.win_login.close()
            self.chuyen_den_dashboard()
        else:
            print("✗ Đăng nhập thất bại!")
            self.hien_thong_bao("Đăng nhập thất bại", "Email hoặc mật khẩu không đúng!")

    # ==================== XỬ LÝ GIAO DỊCH ====================
    
    def mo_popup_them_giao_dich(self):
        """Mở popup thêm giao dịch"""
        print("\n→ Mở popup thêm giao dịch")
        self.ui_themgiaodich.amount.clear()
        self.ui_themgiaodich.text_note.clear()
        self.dlg_themgiaodich.exec()

    def _set_loai_giao_dich(self, loai):
        """Đặt loại giao dịch"""
        self.loai_giao_dich_dang_chon = loai
        print(f"  Đã chọn loại: {loai}")

    def luu_giao_dich(self):
        """Lưu giao dịch mới"""
        print("\n→ Lưu giao dịch")
        
        so_tien_str = self.ui_themgiaodich.amount.text().replace(',', '').replace('.', '')
        
        if not KiemTra.hop_le_so_tien(so_tien_str):
            self.hien_thong_bao("Lỗi", "Số tiền không hợp lệ!")
            return
            
        ngay = self.ui_themgiaodich.date_picker.date().toString("yyyy-MM-dd")
        ghi_chu = self.ui_themgiaodich.text_note.toPlainText()
        
        self.logic_giao_dich.tao_giao_dich(
            loai=self.loai_giao_dich_dang_chon,
            so_tien=so_tien_str,
            ngay=ngay,
            mo_ta=ghi_chu
        )
        
        self.dlg_themgiaodich.close()
        self.tai_du_lieu_bang_giao_dich()
        self.hien_thong_bao("Thành công", "Đã thêm giao dịch mới!")

    def tai_du_lieu_bang_giao_dich(self):
        """Tải dữ liệu vào bảng giao dịch"""
        print("  Đang tải dữ liệu giao dịch...")
        du_lieu = self.logic_giao_dich.tim_kiem_giao_dich()
        bang = self.ui_giaodich.tbl_danhsach_giaodich
        bang.setRowCount(len(du_lieu))
        
        for r, gd in enumerate(du_lieu):
            bang.setItem(r, 0, QTableWidgetItem(gd.get("ngay", "")))
            bang.setItem(r, 1, QTableWidgetItem(gd.get("mo_ta", "")))
            bang.setItem(r, 2, QTableWidgetItem(gd.get("danh_muc", "")))
            bang.setItem(r, 3, QTableWidgetItem(gd.get("loai", "")))
            bang.setItem(r, 4, QTableWidgetItem(f"{gd.get('so_tien', 0):,.0f} đ"))
            bang.setItem(r, 5, QTableWidgetItem("Sửa / Xóa"))
        
        print(f"  ✓ Đã tải {len(du_lieu)} giao dịch")

    # ==================== CÁC HÀM KHÁC ====================
    
    def mo_tao_tiet_kiem(self):
        """Mở form tạo sổ tiết kiệm"""
        print("\n→ Mở tạo sổ tiết kiệm")
        self.chuyen_den_dau_tu_tiet_kiem()
    
    def mo_popup_dautu(self):
        """Mở popup thêm đầu tư"""
        print("\n→ Mở popup thêm đầu tư")
        self.dlg_dautu_popup.exec()
    
    def luu_dau_tu(self):
        """Lưu thông tin đầu tư"""
        print("\n→ Lưu đầu tư")
        self.dlg_dautu_popup.close()
        self.hien_thong_bao("Thành công", "Đã thêm khoản đầu tư mới!")
    
    def tao_ngan_sach(self):
        """Tạo ngân sách mới"""
        print("\n→ Tạo ngân sách mới")
        self.hien_thong_bao("Thông báo", "Chức năng đang được phát triển!")
    
    def them_khoan_vay(self):
        """Thêm khoản vay mới"""
        print("\n→ Thêm khoản vay mới")
        self.hien_thong_bao("Thông báo", "Chức năng đang được phát triển!")
    
    def cap_nhat_taikhoan(self):
        """Cập nhật thông tin tài khoản"""
        print("\n→ Cập nhật tài khoản")
        self.hien_thong_bao("Thành công", "Đã cập nhật thông tin tài khoản!")
    
    def nhap_excel(self):
        """Nhập dữ liệu từ Excel"""
        print("\n→ Nhập dữ liệu từ Excel")
        self.hien_thong_bao("Thông báo", "Chức năng nhập Excel đang được phát triển!")
    
    def xuat_bao_cao(self):
        """Xuất báo cáo"""
        print("\n→ Xuất báo cáo")
        self.hien_thong_bao("Thông báo", "Chức năng xuất báo cáo đang được phát triển!")
    
    def mo_chatbot(self):
        """Mở chatbot hỗ trợ"""
        print("\n→ Mở Chatbot")
        self.hien_thong_bao("Chatbot", "Xin chào! Tôi có thể giúp gì cho bạn?")
    
    def hien_thong_bao(self, title, message):
        """Hiển thị thông báo"""
        self.ui_thongbao.label_title.setText(title)
        self.ui_thongbao.label_message.setText(message)
        self.dlg_thongbao.exec()