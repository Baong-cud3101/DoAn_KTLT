import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class ThemSuaGiaoDichUI:
    def __init__(self, root, user_id="user_001"):
        self.root = root
        self.user_id = user_id
        frame = tk.Frame(root, bg="white")
        frame.pack(fill="both", expand=True)
        tk.Label(
            frame,
            text="Thêm / Sửa giao dịch",
            font=("Arial", 20, "bold"),
            bg="white"
        ).pack(pady=20)
        form = tk.Frame(frame, bg="white")
        form.pack(pady=10)

        tk.Label(form, text="Loại giao dịch", bg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.type_var = tk.StringVar()
        ttk.Combobox(
            form,
            textvariable=self.type_var,
            values=["Thu", "Chi"],
            width=30
        ).grid(row=0, column=1, pady=5)

        tk.Label(form, text="Ngày", bg="white").grid(row=1, column=0, sticky="w", pady=5)
        self.date_entry = tk.Entry(form, width=32)
        self.date_entry.grid(row=1, column=1, pady=5)

        tk.Label(form, text="Danh mục", bg="white").grid(row=2, column=0, sticky="w", pady=5)
        self.category = ttk.Combobox(
            form,
            values=[
                "Ăn uống",
                "Di chuyển",
                "Mua sắm",
                "Giải trí",
                "Lương",
                "Khác"
            ],
            width=30
        )
        self.category.grid(row=2, column=1, pady=5)

        tk.Label(form, text="Mô tả", bg="white").grid(row=3, column=0, sticky="w", pady=5)
        self.desc = tk.Entry(form, width=32)
        self.desc.grid(row=3, column=1, pady=5)

        tk.Label(form, text="Số tiền", bg="white").grid(row=4, column=0, sticky="w", pady=5)
        self.amount = tk.Entry(form, width=32)
        self.amount.grid(row=4, column=1, pady=5)

        button_frame = tk.Frame(frame, bg="white")
        button_frame.pack(pady=20)
        tk.Button(
            button_frame,
            text="Lưu giao dịch",
            width=15,
            bg="#1cc5d8",
            fg="white",
            command=self.save_transaction
        ).pack(side="left", padx=10)
        tk.Button(
            button_frame,
            text="Huỷ",
            width=10,
            command=self.back
        ).pack(side="left", padx=10)

    def save_transaction(self):
        type_gd = self.type_var.get()
        date = self.date_entry.get()
        category = self.category.get()
        desc = self.desc.get()
        amount = self.amount.get()

        if not date or not amount or not type_gd:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return
        try:
            amount = float(amount)
        except:
            messagebox.showerror("Lỗi", "Số tiền không hợp lệ")
            return

        loai = "income" if type_gd == "Thu" else "expense"
        giao_dich = {
            "user_id": self.user_id,
            "thoi_gian": date,
            "danh_muc": category,
            "mo_ta": desc,
            "so_tien": amount,
            "loai": loai
        }

        try:
            file_name = "transactions.json"
            if os.path.exists(file_name):
                with open(file_name, "r", encoding="utf-8") as f:
                    data = json.load(f)
            else:
                data = []
            data.append(giao_dich)
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Thành công", "Đã lưu giao dịch")
            self.clear_form()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    def clear_form(self):
        self.type_var.set("")
        self.date_entry.delete(0, tk.END)
        self.category.set("")
        self.desc.delete(0, tk.END)
        self.amount.delete(0, tk.END)
    def back(self):
        from giao_dien.man_hinh.Nhom1_chung.Trangchu import TrangChuUI
        for w in self.root.winfo_children():
            w.destroy()
        TrangChuUI(self.root, "User")
