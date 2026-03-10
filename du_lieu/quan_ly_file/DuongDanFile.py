# du_lieu/quan_ly_file/DuongDanFile.py
from pathlib import Path

# PROJECT_KTLT/du_lieu/quan_ly_file/DuongDanFile.py
# parents[2] = PROJECT_KTLT/
ROOT = Path(__file__).resolve().parents[2]

# Thư mục chứa file JSON
DU_LIEU = ROOT / "du_lieu" / "file_du_lieu"

# 7 file JSON
NGUOI_DUNG = DU_LIEU / "nguoi_dung.json"
GIAO_DICH = DU_LIEU / "giao_dich.json"
NGAN_SACH = DU_LIEU / "ngan_sach.json"
TIET_KIEM = DU_LIEU / "tiet_kiem.json"
DAU_TU = DU_LIEU / "dau_tu.json"
VAY_NO = DU_LIEU / "vay_no.json"
CAU_HINH = DU_LIEU / "cau_hinh.json"