import os

class DuongDanFile:
    # Thư mục gốc của dữ liệu
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_FOLDER = os.path.join(BASE_DIR, "file_du_lieu")

    # Đường dẫn cụ thể tới từng tệp JSON
    NGUOI_DUNG = os.path.join(DATA_FOLDER, "nguoi_dung.json")
    GIAO_DICH = os.path.join(DATA_FOLDER, "giao_dich.json")
    NGAN_SACH = os.path.join(DATA_FOLDER, "ngan_sach.json")
    VAY_NO = os.path.join(DATA_FOLDER, "vay_no.json")
    TIET_KIEM = os.path.join(DATA_FOLDER, "tiet_kiem.json")
    DAU_TU = os.path.join(DATA_FOLDER, "dau_tu.json")
    CAU_HINH = os.path.join(DATA_FOLDER, "cau_hinh.json")