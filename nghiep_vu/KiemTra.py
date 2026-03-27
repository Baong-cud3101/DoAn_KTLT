import re

class KiemTra:
    @staticmethod
    def hop_le_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def hop_le_so_tien(so_tien_str):
        try:
            val = float(so_tien_str)
            return val > 0
        except ValueError:
            return False