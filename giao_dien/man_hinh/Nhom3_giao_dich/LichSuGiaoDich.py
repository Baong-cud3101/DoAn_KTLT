import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class LichSuGiaoDichUI:
    def __init__(self, root, user_id="user_001"):
        self.root = root
        self.user_id = user_id
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
        self.search_entry = tk.Entry(filterbar, width=25)
        self.search_entry.pack(side="left", padx=5)
        tk.Button(
            filterbar,
            text="Tìm kiếm",
            width=12,
            command=self.tim_kiem
        ).pack(side="left", padx=5)
        tk.Button(
            filterbar,
            text="Xuất Excel",
            width=12,
            command=self.xuat_excel
        ).pack(side="left", padx=5)
        tk.Button(
            filterbar,
            text="Quay lại",
            width=12,
            command=self.back
        ).pack(side="left", padx=5)
        table_frame = tk.Frame(frame)
        table_frame.pack(fill="both", expand=True, padx=40, pady=20)
        columns = ("Ngày", "Mô tả", "Danh mục", "Số tiền")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.column("Ngày", width=120)
        self.tree.column("Mô tả", width=220)
        self.tree.column("Danh mục", width=150)
        self.tree.column("Số tiền", width=120, anchor="e")
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)
        self.load_data()

    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        try:
            with open("transactions.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []
        self.full_data = [d for d in data if d.get("user_id") == self.user_id]
        self.hien_thi(self.full_data)
        
    def hien_thi(self, data):
        self.tree.delete(*self.tree.get_children())
        for d in data:
            self.tree.insert("", tk.END, values=(
                d.get("thoi_gian", ""),
                d.get("mo_ta", ""),
                d.get("danh_muc", ""),
                d.get("so_tien", "")
            ))

    def tim_kiem(self):
        keyword = self.search_entry.get().lower()
        filtered = [
            d for d in self.full_data
            if keyword in d.get("mo_ta", "").lower()
        ]
        self.hien_thi(filtered)

    def xuat_excel(self):
        try:
            from xuat_bao_cao.TaoExcel import TaoExcel
            exporter = TaoExcel()
            data = {
                "transactions": self.full_data,
                "summary": {}
            }
            chart = {}
            file_bytes = exporter.tao(data, chart)
            with open("report.xlsx", "wb") as f:
                f.write(file_bytes)
            messagebox.showinfo("Thành công", "Đã xuất Excel")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def back(self):
        from giao_dien.man_hinh.Nhom1_chung.Trangchu import TrangChuUI
        for w in self.root.winfo_children():
            w.destroy()
        TrangChuUI(self.root, "User")
