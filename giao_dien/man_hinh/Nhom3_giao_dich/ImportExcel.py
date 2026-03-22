import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json
import os

class ImportExcelUI:
    def __init__(self, root, user_id="user_001"):
        self.root = root
        self.user_id = user_id
        self.data = None
        frame = tk.Frame(root, padx=40, pady=30)
        frame.pack(fill="both", expand=True)
        tk.Label(
            frame,
            text="Import giao dịch từ Excel",
            font=("Arial", 18, "bold")
        ).pack(pady=20)
        tk.Button(
            frame,
            text="Chọn file Excel",
            width=25,
            command=self.open_file
        ).pack(pady=10)
        self.text = tk.Text(frame, height=15)
        self.text.pack(fill="both", expand=True)
        tk.Button(
            frame,
            text="Lưu dữ liệu",
            width=25,
            command=self.save_data
        ).pack(pady=10)
        tk.Button(
            frame,
            text="Quay lại",
            width=25,
            command=self.back
        ).pack(pady=5)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx")]
        )

        if not file_path:
            return
        try:
            df = pd.read_excel(file_path)

            required_columns = ["so_tien", "loai", "danh_muc"]
            for col in required_columns:
                if col not in df.columns:
                    messagebox.showerror(
                        "Lỗi",
                        f"Thiếu cột: {col}"
                    )
                    return
            df = df.fillna("")
            records = df.to_dict(orient="records")

            for r in records:
                r["user_id"] = self.user_id
            self.data = records
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, df.head().to_string())
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def save_data(self):
        if not self.data:
            messagebox.showerror("Lỗi", "Chưa có dữ liệu")
            return
        try:
            file_name = "transactions.json"
            if os.path.exists(file_name):
                with open(file_name, "r", encoding="utf-8") as f:
                    old = json.load(f)
            else:
                old = []
            old.extend(self.data)
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(old, f, indent=4, ensure_ascii=False)

            messagebox.showinfo("Thành công", "Đã import dữ liệu")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    def back(self):
        from giao_dien.man_hinh.Nhom1_chung.Trangchu import TrangChuUI
        for w in self.root.winfo_children():
            w.destroy()
        TrangChuUI(self.root, "User")
