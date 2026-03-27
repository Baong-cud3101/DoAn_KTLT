import json
import os

class DocGhiJson:
    @staticmethod
    def doc(duong_dan):
        if not os.path.exists(duong_dan):
            return []
        try:
            with open(duong_dan, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def ghi(duong_dan, du_lieu):
        try:
            # Tự động tạo thư mục nếu chưa có
            os.makedirs(os.path.dirname(duong_dan), exist_ok=True)
            with open(duong_dan, 'w', encoding='utf-8') as f:
                json.dump(du_lieu, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Lỗi khi ghi tệp: {e}")
            return False