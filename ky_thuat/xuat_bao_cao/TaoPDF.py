class TaoPDF:
    def tao(self, du_lieu: dict, bieu_do: dict) -> bytes: pass
    def xuat_mau(self, mau_van_ban: str, du_lieu: dict) -> str: pass
    def nhung_bieu_do(self, hinh_anh_bieu_do: bytes) -> bytes: pass
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from io import BytesIO
import matplotlib.pyplot as plt
class TaoPDF:
    def tao(self, du_lieu: dict, bieu_do: dict) -> bytes:
        """
        du_lieu: {
            "summary": {...}
        }
        bieu_do: {
            "labels": [...],
            "values": [...]
        }
        """
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        content = []

        text = self.xuat_mau("BÁO CÁO TÀI CHÍNH\n\n{data}", du_lieu)
        content.append(Paragraph(text, styles["Normal"]))
        content.append(Spacer(1, 20))
        img_bytes = self.nhung_bieu_do(bieu_do)

        if img_bytes:
            img = Image(BytesIO(img_bytes), width=4 * inch, height=3 * inch)
            content.append(img)
        doc.build(content)

        buffer.seek(0)
        return buffer.getvalue()


    def xuat_mau(self, mau_van_ban: str, du_lieu: dict) -> str:
        """
        Render nội dung text
        """
        summary = du_lieu.get("summary", {})
        text_data = ""
        for k, v in summary.items():
            text_data += f"{k}: {v}<br/>"

        return mau_van_ban.replace("{data}", text_data)


    def nhung_bieu_do(self, du_lieu_bieu_do: dict) -> bytes:
        """
        Tạo biểu đồ bằng matplotlib rồi convert sang bytes
        """
        if not du_lieu_bieu_do:
            return None

        labels = du_lieu_bieu_do.get("labels", [])
        values = du_lieu_bieu_do.get("values", [])
        plt.figure()
        plt.bar(labels, values)
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        plt.close()
        img_buffer.seek(0)
        return img_buffer.getvalue()
