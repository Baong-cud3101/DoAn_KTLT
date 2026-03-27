#  Ứng dụng Quản lý Tài chính Cá nhân

## Yêu cầu hệ thống
- Python 3.9+
- Thư viện: `pip install -r requirement.txt`

## Cấu trúc thư mục
- `dieu_khien`: Lớp Controller điều phối luồng giữa View và Model.
- `du_lieu`: Lớp DAO và quản lý I/O tệp JSON.
- `giao_dien`: Lớp View (mã nguồn giao diện PyQt6 sinh từ tệp `.ui`).
- `nghiep_vu`: Lớp xử lý logic, tính toán và phân tích.

## Hướng dẫn chạy
Thực thi lệnh: `python main.py`