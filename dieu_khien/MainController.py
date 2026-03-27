from PyQt6.QtWidgets import QMainWindow, QDialog, QTableWidgetItem, QMessageBox, QFileDialog
import sys
import datetime

from giao_dien.login import Ui_LoginForm as Ui_LoginWindow
from giao_dien.DB import Ui_MainWindow as Ui_Dashboard
from giao_dien.giaodich import Ui_MainWindow as Ui_GiaoDich
from giao_dien.themgiaodich import Ui_AddDialog
from giao_dien.baocao import Ui_MainWindow as Ui_BaoCao
from giao_dien.dautupopup import Ui_Dialog as Ui_DauTuPopup
from giao_dien.dautuvatietkiem import Ui_MainWindow_DauTu as Ui_DauTuTietKiem
from giao_dien.quanlyngansach import Ui_MainWindow as Ui_QuanLyNganSach
from giao_dien.taikhoanuser import Ui_MainWindow as Ui_TaiKhoanUser
from giao_dien.vayno import Ui_MainWindow as Ui_VayNo

from nghiep_vu.XuLyNguoiDung import XuLyNguoiDung
from nghiep_vu.XuLyGiaoDich import XuLyGiaoDich
from nghiep_vu.KiemTra import KiemTra
from nghiep_vu.XuLyNganSach import XuLyNganSach
from nghiep_vu.XuLyBaoCao import XuLyBaoCao
from nghiep_vu.XuLyDauTu import XuLyDauTu
from nghiep_vu.XuLyVayNo import XuLyVayNo

class MainController:
    def __init__(self):
        self.logic_nguoi_dung = XuLyNguoiDung()
        self.logic_giao_dich = XuLyGiaoDich()
        self.logic_ngan_sach = XuLyNganSach()
        self.logic_bao_cao = XuLyBaoCao()
        self.logic_dau_tu = XuLyDauTu()
        self.logic_vay_no = XuLyVayNo()
        
        self.ma_nd_hien_tai = None
        self.loai_giao_dich_dang_chon = "Chi"

        self.win_login = QMainWindow()
        self.ui_login = Ui_LoginWindow()
        self.ui_login.setupUi(self.win_login)
        
        self.win_dashboard = QMainWindow()
        self.ui_dashboard = Ui_Dashboard()
        self.ui_dashboard.setupUi(self.win_dashboard)
        
        self.win_giaodich = QMainWindow()
        self.ui_giaodich = Ui_GiaoDich()
        self.ui_giaodich.setupUi(self.win_giaodich)
        
        self.dlg_themgiaodich = QDialog()
        self.ui_themgiaodich = Ui_AddDialog()
        self.ui_themgiaodich.setupUi(self.dlg_themgiaodich)
        
        self.win_baocao = QMainWindow()
        self.ui_baocao = Ui_BaoCao()
        self.ui_baocao.setupUi(self.win_baocao)
        
        self.win_dautu_tietkiem = QMainWindow()
        self.ui_dautu_tietkiem = Ui_DauTuTietKiem()
        self.ui_dautu_tietkiem.setupUi(self.win_dautu_tietkiem)
        
        self.dlg_dautu_popup = QDialog()
        self.ui_dautu_popup = Ui_DauTuPopup()
        self.ui_dautu_popup.setupUi(self.dlg_dautu_popup)
        
        self.win_ngansach = QMainWindow()
        self.ui_ngansach = Ui_QuanLyNganSach()
        self.ui_ngansach.setupUi(self.win_ngansach)
        
        self.win_taikhoan = QMainWindow()
        self.ui_taikhoan = Ui_TaiKhoanUser()
        self.ui_taikhoan.setupUi(self.win_taikhoan)
        
        self.win_vayno = QMainWindow()
        self.ui_vayno = Ui_VayNo()
        self.ui_vayno.setupUi(self.win_vayno)

        self._ket_noi_su_kien()

    def khoi_dong(self):
        self.win_login.show()

    def _ket_noi_su_kien(self):
        if hasattr(self.ui_login, 'btn_dangnhap_submit'):
            self.ui_login.btn_dangnhap_submit.clicked.connect(self.xu_ly_dang_nhap)

        if hasattr(self.ui_dashboard, 'btn_nav_giaodich'):
            self.ui_dashboard.btn_nav_giaodich.clicked.connect(self.chuyen_den_giao_dich)
        if hasattr(self.ui_dashboard, 'btn_nav_dautu_tietkiem'):
            self.ui_dashboard.btn_nav_dautu_tietkiem.clicked.connect(self.chuyen_den_dau_tu_tiet_kiem)
        if hasattr(self.ui_dashboard, 'btn_nav_ngansach'):
            self.ui_dashboard.btn_nav_ngansach.clicked.connect(self.chuyen_den_quan_ly_ngan_sach)
        if hasattr(self.ui_dashboard, 'btn_nav_vayno'):
            self.ui_dashboard.btn_nav_vayno.clicked.connect(self.chuyen_den_vay_no)
        if hasattr(self.ui_dashboard, 'btn_mo_tietkiem'):
            self.ui_dashboard.btn_mo_tietkiem.clicked.connect(self.mo_tao_tiet_kiem)

        if hasattr(self.ui_giaodich, 'btn_nav_dashboard'):
            self.ui_giaodich.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)
        if hasattr(self.ui_giaodich, 'btn_nav_baocao'):
            self.ui_giaodich.btn_nav_baocao.clicked.connect(self.chuyen_den_bao_cao)
        if hasattr(self.ui_giaodich, 'btn_nav_dautu_tietkiem'):
            self.ui_giaodich.btn_nav_dautu_tietkiem.clicked.connect(self.chuyen_den_dau_tu_tiet_kiem)
        if hasattr(self.ui_giaodich, 'btn_nav_ngansach'):
            self.ui_giaodich.btn_nav_ngansach.clicked.connect(self.chuyen_den_quan_ly_ngan_sach)
        if hasattr(self.ui_giaodich, 'btn_nav_vayno'):
            self.ui_giaodich.btn_nav_vayno.clicked.connect(self.chuyen_den_vay_no)
        if hasattr(self.ui_giaodich, 'btn_nav_caidat'):
            self.ui_giaodich.btn_nav_caidat.clicked.connect(self.chuyen_den_tai_khoan)
        if hasattr(self.ui_giaodich, 'btn_them_giaodich'):
            self.ui_giaodich.btn_them_giaodich.clicked.connect(self.mo_popup_them_giao_dich)
        if hasattr(self.ui_giaodich, 'btn_nhap_excel'):
            self.ui_giaodich.btn_nhap_excel.clicked.connect(self.nhap_excel)

        if hasattr(self.ui_themgiaodich, 'btn_expense'):
            self.ui_themgiaodich.btn_expense.clicked.connect(lambda: self._set_loai_giao_dich("Chi"))
        if hasattr(self.ui_themgiaodich, 'btn_income'):
            self.ui_themgiaodich.btn_income.clicked.connect(lambda: self._set_loai_giao_dich("Thu"))
        if hasattr(self.ui_themgiaodich, 'btn_save'):
            self.ui_themgiaodich.btn_save.clicked.connect(self.luu_giao_dich)
        if hasattr(self.ui_themgiaodich, 'btn_cancel'):
            self.ui_themgiaodich.btn_cancel.clicked.connect(self.dlg_themgiaodich.close)
        if hasattr(self.ui_themgiaodich, 'btn_close'):
            self.ui_themgiaodich.btn_close.clicked.connect(self.dlg_themgiaodich.close)

        if hasattr(self.ui_dautu_tietkiem, 'btn_nav_dashboard'):
            self.ui_dautu_tietkiem.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)
        if hasattr(self.ui_dautu_tietkiem, 'btn_tietkiem_mo_so'):
            self.ui_dautu_tietkiem.btn_tietkiem_mo_so.clicked.connect(self.mo_popup_dautu)

        if hasattr(self.ui_dautu_popup, 'btn_save'):
            self.ui_dautu_popup.btn_save.clicked.connect(self.luu_dau_tu)
        if hasattr(self.ui_dautu_popup, 'btn_close'):
            self.ui_dautu_popup.btn_close.clicked.connect(self.dlg_dautu_popup.close)

        if hasattr(self.ui_ngansach, 'sideBtn'):
            self.ui_ngansach.sideBtn.clicked.connect(self.chuyen_den_dashboard)

        if hasattr(self.ui_vayno, 'sideBtn'):
            self.ui_vayno.sideBtn.clicked.connect(self.chuyen_den_dashboard)

        if hasattr(self.ui_taikhoan, 'btn_nav_dashboard'):
            self.ui_taikhoan.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)

        if hasattr(self.ui_baocao, 'btn_nav_dashboard'):
            self.ui_baocao.btn_nav_dashboard.clicked.connect(self.chuyen_den_dashboard)
        if hasattr(self.ui_baocao, 'btnPDF'):
            self.ui_baocao.btnPDF.clicked.connect(self.xuat_bao_cao)

    def chuyen_den_dashboard(self):
        self._an_tat_ca_man_hinh()
        self.win_dashboard.show()

    def chuyen_den_giao_dich(self):
        self._an_tat_ca_man_hinh()
        self.tai_du_lieu_bang_giao_dich()
        self.win_giaodich.show()

    def chuyen_den_bao_cao(self):
        self._an_tat_ca_man_hinh()
        self.win_baocao.show()

    def chuyen_den_dau_tu_tiet_kiem(self):
        self._an_tat_ca_man_hinh()
        self.win_dautu_tietkiem.show()

    def chuyen_den_quan_ly_ngan_sach(self):
        self._an_tat_ca_man_hinh()
        self.win_ngansach.show()

    def chuyen_den_vay_no(self):
        self._an_tat_ca_man_hinh()
        self.win_vayno.show()

    def chuyen_den_tai_khoan(self):
        self._an_tat_ca_man_hinh()
        self.win_taikhoan.show()

    def _an_tat_ca_man_hinh(self):
        self.win_dashboard.hide()
        self.win_giaodich.hide()
        self.win_baocao.hide()
        self.win_dautu_tietkiem.hide()
        self.win_ngansach.hide()
        self.win_taikhoan.hide()
        self.win_vayno.hide()

    def xu_ly_dang_nhap(self):
        email = self.ui_login.txt_nguoidung_email.text()
        mat_khau = self.ui_login.txt_nguoidung_matkhau.text()
        hop_le, user = self.logic_nguoi_dung.xac_thuc(email, mat_khau)
        
        if hop_le or (email == "" and mat_khau == ""):
            if user:
                self.ma_nd_hien_tai = user.get("MaND")
            self.win_login.close()
            self.chuyen_den_dashboard()
        else:
            self.hien_thong_bao("Đăng nhập thất bại", "Email hoặc mật khẩu không đúng!")

    def mo_popup_them_giao_dich(self):
        self.ui_themgiaodich.amount.clear()
        self.ui_themgiaodich.text_note.clear()
        self.dlg_themgiaodich.exec()

    def _set_loai_giao_dich(self, loai):
        self.loai_giao_dich_dang_chon = loai

    def luu_giao_dich(self):
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

    def tai_du_lieu_bang_giao_dich(self):
        du_lieu = self.logic_giao_dich.tim_kiem_giao_dich()
        bang = self.ui_giaodich.tbl_danhsach_giaodich
        bang.setRowCount(len(du_lieu))
        for r, gd in enumerate(du_lieu):
            bang.setItem(r, 0, QTableWidgetItem(gd.get("ngay", "")))
            bang.setItem(r, 1, QTableWidgetItem(gd.get("mo_ta", "")))
            bang.setItem(r, 2, QTableWidgetItem(gd.get("danh_muc", "")))
            bang.setItem(r, 3, QTableWidgetItem(gd.get("loai", "")))
            bang.setItem(r, 4, QTableWidgetItem(f"{float(gd.get('so_tien', 0)):,.0f} đ"))
            bang.setItem(r, 5, QTableWidgetItem("Sửa / Xóa"))

    def mo_tao_tiet_kiem(self):
        self.chuyen_den_dau_tu_tiet_kiem()
    
    def mo_popup_dautu(self):
        self.dlg_dautu_popup.exec()
    
    def luu_dau_tu(self):
        so_tien_str = self.ui_dautu_popup.lineedit.text().replace('.', '').replace(' đ', '').replace(',', '')
        if KiemTra.hop_le_so_tien(so_tien_str):
            self.logic_dau_tu.mo_so_tiet_kiem(so_tien=so_tien_str, ky_han=12, lai_suat=6.1)
            self.dlg_dautu_popup.close()
            self.hien_thong_bao("Thành công", "Đã lưu khoản đầu tư/tiết kiệm!")
        else:
            self.hien_thong_bao("Lỗi", "Số tiền không hợp lệ")

    def nhap_excel(self):
        file_name, _ = QFileDialog.getOpenFileName(self.win_giaodich, "Chọn file Excel", "", "Excel Files (*.xlsx *.xls)")
        if file_name:
            ket_qua = self.logic_excel.nhap_hang_loat(file_name)
            self.tai_du_lieu_bang_giao_dich()
            self.hien_thong_bao("Kết quả nhập", f"Thành công: {ket_qua.get('thanh_cong', 0)} dòng.\nLỗi: {len(ket_qua.get('loi', []))} dòng.")
    
    def xuat_bao_cao(self):
        file_name, _ = QFileDialog.getSaveFileName(self.win_baocao, "Lưu báo cáo Excel", "BaoCao_GiaoDich.xlsx", "Excel Files (*.xlsx)")
        if file_name:
            thang_hien_tai = datetime.datetime.now().month
            nam_hien_tai = datetime.datetime.now().year
            thanh_cong = self.logic_bao_cao.xuat_bao_cao_excel(file_name, thang_hien_tai, nam_hien_tai)
            if thanh_cong:
                self.hien_thong_bao("Thành công", "Đã xuất báo cáo Excel!")
            else:
                self.hien_thong_bao("Lỗi", "Không có dữ liệu hoặc xuất thất bại.")

    def tao_ngan_sach(self):
        self.hien_thong_bao("Thông báo", "Chức năng đang được phát triển!")
    
    def them_khoan_vay(self):
        self.hien_thong_bao("Thông báo", "Chức năng đang được phát triển!")

    def mo_chatbot(self):
        self.hien_thong_bao("Chatbot", "Xin chào! Tôi có thể giúp gì cho bạn?")

    def hien_thong_bao(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()