import tkinter as tk


class TrangChuUI:
    def __init__(self, root, username):
        main = tk.Frame(root)
        main.pack(fill="both", expand=True)

        sidebar = tk.Frame(main, bg="#eeeeee", width=220)
        sidebar.pack(side="left", fill="y")
        tk.Label(
            sidebar,
            text="Tên APP",
            bg="#eeeeee",
            font=("Arial", 14, "bold")
        ).pack(pady=20)
        menus = [
            "Trang chủ",
            "Giao dịch",
            "Ngân sách",
            "Đầu tư",
            "Vay nợ",
            "Báo cáo",
            "Cài đặt"
        ]
        for m in menus:
            tk.Button(sidebar, text=m, width=18).pack(pady=5)

        content = tk.Frame(main, bg="white")
        content.pack(side="right", expand=True, fill="both")

        header = tk.Frame(content, bg="white")
        header.pack(fill="x", pady=10)

        tk.Label(
            header,
            text=f"Chào bạn, {username}",
            font=("Arial", 16),
            bg="white"
        ).pack(side="left", padx=20)

        tk.Button(
            header,
            text="Thêm giao dịch"
        ).pack(side="right", padx=20)
        stat = tk.Frame(content, bg="white")
        stat.pack(pady=20)
        titles = ["Tổng thu", "Tổng chi", "Số dư"]

        for t in titles:
            box = tk.Frame(stat, bg="#dddddd", width=200, height=80)
            box.pack(side="left", padx=20)
            tk.Label(
                box,
                text=t,
                bg="#dddddd"
            ).place(relx=0.5, rely=0.5, anchor="center")

        charts = tk.Frame(content, bg="white")
        charts.pack(pady=20)
        tk.Label(
            charts,
            text="Biểu đồ thu chi",
            bg="#cccccc",
            width=30,
            height=10
        ).pack(side="left", padx=20)

        tk.Label(
            charts,
            text="Biểu đồ cơ cấu chi",
            bg="#cccccc",
            width=30,
            height=10
        ).pack(side="left", padx=20)
        alert = tk.Frame(content, bg="#dddddd", height=120)
        alert.pack(fill="x", padx=40, pady=20)
        tk.Label(
            alert,
            text="Cảnh báo ngân sách",
            bg="#dddddd",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", padx=10, pady=5)

        tk.Label(
            alert,
            text="Chi tiêu 'Ăn uống' đã đạt 90%",
            bg="#dddddd"
        ).pack(anchor="w", padx=10)
