import os

class DuongDanFile:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_FOLDER = os.path.join(BASE_DIR, 'file_du_lieu')

    @staticmethod
    def lay_duong_dan(ten_file):
        return os.path.join(DuongDanFile.DATA_FOLDER, ten_file)