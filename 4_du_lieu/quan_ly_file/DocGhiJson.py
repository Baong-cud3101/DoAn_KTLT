# du_lieu/quan_ly_file/DocGhiJson.py
import json
import os
from datetime import datetime

class DocGhiJson:
    # Lớp xử lý đọc/ghi JSON - Dùng chung cho toàn bộ hệ thống
    def __init__(self, thu_muc="src/du_lieu/file_du_lieu"):
        self.thu_muc = thu_muc
        self._tao_thu_muc()
    
    def _tao_thu_muc(self):
        #Tạo thư mục nếu chưa tồn tại
        if not os.path.exists(self.thu_muc):
            os.makedirs(self.thu_muc)
    
    def _duong_dan_file(self, ten_file):
        #Lấy đường dẫn đầy đủ của file
        return os.path.join(self.thu_muc, ten_file)
    
    def doc(self, ten_file):
        #Đọc dữ liệu từ file JSON
        duong_dan = self._duong_dan_file(ten_file)
        try:
            with open(duong_dan, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Tạo file mới nếu chưa tồn tại
            self.ghi(ten_file, [])
            return []
        except json.JSONDecodeError:
            # File lỗi -> tạo mới
            self.ghi(ten_file, [])
            return []
    
    def ghi(self, ten_file, du_lieu):
        #Ghi dữ liệu vào file JSON
        duong_dan = self._duong_dan_file(ten_file)
        with open(duong_dan, 'w', encoding='utf-8') as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=2)
    
    def them(self, ten_file, ban_ghi_moi):
        # Thêm một bản ghi mới vào file
        du_lieu = self.doc(ten_file)
        
        # Tự động tạo ID nếu chưa có
        if 'id' not in ban_ghi_moi:
            ban_ghi_moi['id'] = f"{ten_file.split('.')[0]}_{len(du_lieu)+1}"
        
        # Thêm thời gian tạo
        ban_ghi_moi['ngayTao'] = datetime.now().isoformat()
        ban_ghi_moi['ngayCapNhat'] = datetime.now().isoformat()
        
        du_lieu.append(ban_ghi_moi)
        self.ghi(ten_file, du_lieu)
        return ban_ghi_moi['id']
    
    def cap_nhat(self, ten_file, ma_so, du_lieu_moi):
        #Cập nhật bản ghi theo ID
        du_lieu = self.doc(ten_file)
        for i, item in enumerate(du_lieu):
            if item.get('id') == ma_so:
                du_lieu_moi['ngayCapNhat'] = datetime.now().isoformat()
                du_lieu[i] = {**item, **du_lieu_moi}
                self.ghi(ten_file, du_lieu)
                return True
        return False
    
    def xoa(self, ten_file, ma_so):
        #Xóa bản ghi theo ID
        du_lieu = self.doc(ten_file)
        du_lieu_moi = [item for item in du_lieu if item.get('id') != ma_so]
        if len(du_lieu_moi) < len(du_lieu):
            self.ghi(ten_file, du_lieu_moi)
            return True
        return False
    
    def tim_theo_id(self, ten_file, ma_so):
        #Tìm bản ghi theo ID
        du_lieu = self.doc(ten_file)
        for item in du_lieu:
            if item.get('id') == ma_so:
                return item
        return None
    
    def tim_theo(self, ten_file, **dieu_kien):
        #Tìm bản ghi theo điều kiện
        du_lieu = self.doc(ten_file)
        ket_qua = []
        for item in du_lieu:
            match = True
            for key, value in dieu_kien.items():
                if item.get(key) != value:
                    match = False
                    break
            if match:
                ket_qua.append(item)
        return ket_qua