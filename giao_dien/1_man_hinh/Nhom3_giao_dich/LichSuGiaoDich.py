import tkinter as tk
from tkinter import ttk

class LichSuGiaoDichUI:
    def __init__(self,root):
        frame = tk.Frame(root)
        frame.pack(fill="both",expand=True)
        tk.Label(
            frame,
            text="Lịch sử giao dịch",
            font=("Arial",18,"bold")
        ).pack(pady=10)
        filterbar = tk.Frame(frame)
        filterbar.pack(pady=10)
        buttons = [
            "Tìm kiếm giao dịch",
            "Tìm theo thời gian",
            "Tìm theo danh mục",
            "Xuất Excel"
        ]
        for b in buttons:
            tk.Button(filterbar,text=b).pack(side="left",padx=5)

        columns = ("Ngày","Mô tả","Danh mục","Số tiền","Thao tác")

        tree = ttk.Treeview(frame,columns=columns,show="headings")

        for c in columns:
            tree.heading(c,text=c)

        tree.pack(fill="both",expand=True,padx=40,pady=20)
