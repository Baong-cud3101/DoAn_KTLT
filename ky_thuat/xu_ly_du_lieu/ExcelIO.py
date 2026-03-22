class XuLyExcelKyThuat:
    def phan_tich_tap_tin(self, bo_nho_dem) -> list: pass
    def kiem_tra_dinh_dang(self, tieu_de: list) -> bool: pass
    def kiem_tra_dong(self, dong_du_lieu: dict) -> bool: pass
        import pandas as pd

class XuLyExcelKyThuat:
    def phan_tich_tap_tin(self, bo_nho_dem) -> list:
        """
        Đọc file Excel và trả về list dict
        """
        df = pd.read_excel(bo_nho_dem)

        if not self.kiem_tra_dinh_dang(list(df.columns)):
            raise ValueError("Sai định dạng file Excel")

        data = df.to_dict(orient="records")

        valid_data = []
        for row in data:
            if self.kiem_tra_dong(row):
                valid_data.append(row)
        return valid_data


    def kiem_tra_dinh_dang(self, tieu_de: list) -> bool:
        expected = ["date", "type", "amount"]
        return all(col in tieu_de for col in expected)

    def kiem_tra_dong(self, dong_du_lieu: dict) -> bool:
        try:
            if "amount" not in dong_du_lieu:
                return False
            if float(dong_du_lieu["amount"]) < 0:
                return False
            if dong_du_lieu.get("type") not in ["income", "expense"]:
                return False
            return True
        except:
            return False
