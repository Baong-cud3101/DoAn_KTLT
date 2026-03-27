import re

class KiemTra:
    @staticmethod
    def la_email_hop_le(email):
        pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def la_mat_khau_manh(password):
        # Ít nhất 6 ký tự
        return len(password) >= 6