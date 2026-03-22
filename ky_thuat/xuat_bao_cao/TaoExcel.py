class TaoExcel:
    def tao(self, du_lieu: dict, bieu_do: dict) -> bytes: pass
    def ghi_trang_tinh(self, trang_tinh, du_lieu: dict): pass
    def them_bieu_do(self, tap_tin_excel, du_lieu_bieu_do: dict): pass
        import pandas as pd
from io import BytesIO
class TaoExcel:
    def tao(self, du_lieu: dict, bieu_do: dict) -> bytes:
        """
        du_lieu: {
            "transactions": [...],
            "summary": {...}
        }

        bieu_do: {
            "labels": [...],
            "values": [...]
        }
        """
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            workbook = writer.book
            df = pd.DataFrame(du_lieu.get("transactions", []))
            df.to_excel(writer, sheet_name="GiaoDich", index=False)
            worksheet = writer.sheets["GiaoDich"]
            self.ghi_trang_tinh(worksheet, du_lieu.get("summary", {}))
            self.them_bieu_do(workbook, worksheet, bieu_do)
        output.seek(0)
        return output.getvalue()


    def ghi_trang_tinh(self, trang_tinh, du_lieu: dict):
        """
        Ghi tổng kết vào Excel
        """
        row = 2 
        for key, value in du_lieu.items():
            trang_tinh.write(row, 5, key)
            trang_tinh.write(row, 6, value)
            row += 1


    def them_bieu_do(self, tap_tin_excel, trang_tinh, du_lieu_bieu_do: dict):
        """
        Thêm biểu đồ cột
        """
        if not du_lieu_bieu_do:
            return
        labels = du_lieu_bieu_do.get("labels", [])
        values = du_lieu_bieu_do.get("values", [])

        start_row = 2
        for i, (label, value) in enumerate(zip(labels, values)):
            trang_tinh.write(start_row + i, 0, label)
            trang_tinh.write(start_row + i, 1, value)

        chart = tap_tin_excel.add_chart({'type': 'column'})

        chart.add_series({
            'name': 'Biểu đồ thu chi',
            'categories': ['GiaoDich', start_row, 0, start_row + len(labels) - 1, 0],
            'values':     ['GiaoDich', start_row, 1, start_row + len(values) - 1, 1],
        })

        chart.set_title({'name': 'Thống kê tài chính'})
        chart.set_x_axis({'name': 'Danh mục'})
        chart.set_y_axis({'name': 'Giá trị'})
        trang_tinh.insert_chart('H2', chart)
