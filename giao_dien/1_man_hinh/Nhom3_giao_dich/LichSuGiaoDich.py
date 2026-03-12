import tkinter as tk
from tkinter import ttk


class LichSuGiaoDichUI:

    def __init__(self, root):
        frame = tk.Frame(root, bg="white")
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text="Lịch sử giao dịch",
            font=("Arial", 20, "bold"),
            bg="white"
        ).pack(pady=20)

        filterbar = tk.Frame(frame, bg="white")
        filterbar.pack(pady=10)
        tk.Entry(filterbar, width=25).pack(side="left", padx=5)
        tk.Button(
            filterbar,
            text="Tìm kiếm",
            width=12
        ).pack(side="left", padx=5)
        tk.Button(
            filterbar,
            text="Theo thời gian",
            width=14
        ).pack(side="left", padx=5)
        tk.Button(
            filterbar,
            text="Theo danh mục",
            width=14
        ).pack(side="left", padx=5)
        tk.Button(
            filterbar,
            text="Xuất Excel",
            width=12
        ).pack(side="left", padx=5)

        table_frame = tk.Frame(frame)
        table_frame.pack(fill="both", expand=True, padx=40, pady=20)
        columns = ("Ngày", "Mô tả", "Danh mục", "Số tiền")
        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )
        tree.heading("Ngày", text="Ngày")
        tree.heading("Mô tả", text="Mô tả")
        tree.heading("Danh mục", text="Danh mục")
        tree.heading("Số tiền", text="Số tiền")
        tree.column("Ngày", width=120)
        tree.column("Mô tả", width=220)
        tree.column("Danh mục", width=150)
        tree.column("Số tiền", width=120, anchor="e")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)
        data = [
            ("01/03/2026", "Ăn trưa", "Ăn uống", "-50,000"),
            ("02/03/2026", "Lương tháng", "Thu nhập", "+10,000,000"),
            ("03/03/2026", "Cafe", "Ăn uống", "-30,000"),
            ("04/03/2026", "Mua sách", "Giải trí", "-120,000"),
        ]
        for row in data:
            tree.insert("", tk.END, values=row)
