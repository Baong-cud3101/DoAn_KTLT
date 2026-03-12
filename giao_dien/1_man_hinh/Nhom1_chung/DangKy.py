import tkinter as tk
from tkinter import messagebox
import json


class DangKyUI:
    def __init__(self, root):
        self.root = root
        main = tk.Frame(root)
        main.pack(fill="both", expand=True)

        left = tk.Frame(main, bg="#1cc5d8", width=400)
        left.pack(side="left", fill="y")
        tk.Label(
            left,
            text="LOGO",
            font=("Arial", 30, "bold"),
            bg="#1cc5d8",
            fg="white"
        ).place(relx=0.5, rely=0.5, anchor="center")

        right = tk.Frame(main, bg="white", padx=40, pady=40)
        right.pack(side="right", expand=True)

        tk.Label(
            right,
            text="Tạo tài khoản",
            font=("Arial", 22, "bold"),
            bg="white"
        ).pack(pady=15)

        tk.Label(right, text="Tên", bg="white").pack(anchor="w")
        self.entry_name = tk.Entry(right, width=35)
        self.entry_name.pack(pady=5)

        tk.Label(right, text="Họ", bg="white").pack(anchor="w")
        self.entry_last = tk.Entry(right, width=35)
        self.entry_last.pack(pady=5)

        tk.Label(right, text="Địa chỉ email", bg="white").pack(anchor="w")
        self.entry_email = tk.Entry(right, width=35)
        self.entry_email.pack(pady=5)

        tk.Label(right, text="Mật khẩu", bg="white").pack(anchor="w")
        self.entry_pass = tk.Entry(right, width=35, show="*")
        self.entry_pass.pack(pady=5)

        tk.Label(right, text="Xác nhận mật khẩu", bg="white").pack(anchor="w")
        self.entry_repass = tk.Entry(right, width=35, show="*")
        self.entry_repass.pack(pady=5)

        self.var = tk.IntVar()
        tk.Checkbutton(
            right,
            text="Đồng ý với các điều khoản sử dụng",
            variable=self.var,
            bg="white"
        ).pack(pady=10)

        tk.Button(
            right,
            text="Tạo tài khoản",
            width=20,
            command=self.register
        ).pack(pady=10)

        login_frame = tk.Frame(right, bg="white")
        login_frame.pack()
        tk.Label(login_frame, text="Đã có tài khoản ?", bg="white").pack(side="left")
        tk.Button(
            login_frame,
            text="Đăng nhập",
            command=self.open_login
        ).pack(side="left")

    def register(self):
        name = self.entry_name.get()
        last = self.entry_last.get()
        email = self.entry_email.get()
        password = self.entry_pass.get()
        repass = self.entry_repass.get()
        if password != repass:
            messagebox.showerror("Lỗi", "Mật khẩu không khớp")
            return
        user = {
            "name": name + " " + last,
            "email": email,
            "password": password
        }
        try:
            with open("users.json", "r") as f:
                data = json.load(f)
        except:
            data = []
        data.append(user)
        with open("users.json", "w") as f:
            json.dump(data, f)

        messagebox.showinfo("Thành công", "Đăng ký thành công")
        self.open_login()

    def open_login(self):
        from DangNhap import DangNhapUI
        for w in self.root.winfo_children():
            w.destroy()
        DangNhapUI(self.root)
