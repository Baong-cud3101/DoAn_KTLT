import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json


class ImportExcelUI:
    def __init__(self, root):
        self.root = root
        frame = tk.Frame(root, padx=40, pady=30)
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text="Import giao dịch từ Excel",
            font=("Arial",18,"bold")
        ).pack(pady=20)

        tk.Button(
            frame,
            text="Chọn file Excel",
            width=20,
            command=self.open_file
        ).pack(pady=10)

        self.text = tk.Text(frame, height=20)
        self.text.pack(fill="both", expand=True)

        tk.Button(
            frame,
            text="Lưu dữ liệu",
            width=20,
            command=self.save_data
        ).pack(pady=10)

        self.data = None


    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel files","*.xlsx")]
        )
        if not file_path:
            return
        try:
            df = pd.read_excel(file_path)
            self.data = df.to_dict(orient="records")
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, df.head().to_string())

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def save_data(self):
        if not self.data:
            messagebox.showerror("Lỗi","Chưa có dữ liệu")
            return
        try:
            try:
                with open("transactions.json","r") as f:
                    old = json.load(f)
            except:
                old = []
            old.extend(self.data)
            with open("transactions.json","w") as f:
                json.dump(old,f,indent=4)
            messagebox.showinfo("Thành công","Đã import dữ liệu")
        except Exception as e:
            messagebox.showerror("Lỗi",str(e))
