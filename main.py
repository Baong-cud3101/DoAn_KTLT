import sys
from PyQt6.QtWidgets import QApplication
from dieu_khien.MainController import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    controller = MainController()
    controller.khoi_dong()

    sys.exit(app.exec())