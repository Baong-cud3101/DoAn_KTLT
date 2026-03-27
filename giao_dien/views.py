# Trong file giao_dien/views.py
from PyQt6 import QtWidgets, uic

class GiaoDichWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("giao_dien/giaodich.ui", self)
        # Bắt sự kiện các nút trong tab Giao dịch ở đây...

class VayNoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("giao_dien/vayno.ui", self)

class DashboardView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("giao_dien/DB.ui", self) # DB.ui là khung chứa Menu trái và StackedWidget bên phải
        
        # 1. Khởi tạo các trang (tabs)
        self.page_giaodich = GiaoDichWidget()
        self.page_vayno = VayNoWidget()
        
        # 2. Thêm các trang vào StackedWidget (giả sử bạn đặt tên nó là stackedWidget trong Qt Designer)
        self.stackedWidget.addWidget(self.page_giaodich)
        self.stackedWidget.addWidget(self.page_vayno)
        
        # 3. Chuyển trang khi bấm menu
        self.btnMenuGiaoDich.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_giaodich))
        self.btnMenuVayNo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_vayno))