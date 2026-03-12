import tkinter as tk
from tkinter import messagebox
import json


class QuenMatKhauUI:
    def __init__(self, root):

        self.root = root
        frame = tk.Frame(root, bg="white", padx=80, pady=60)
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text="ĐẶT LẠI MẬT KHẨU CỦA BẠN",
            font=("Arial", 20, "bold"),
            bg="white"
        ).pack(anchor="w", pady=10)

        tk.Label(
            frame,
            text="CHÚNG TÔI SẼ GỬI CHO BẠN MỘT EMAIL ĐỂ CÀI LẠI MẬT KHẨU.",
            font=("Arial", 12),
            bg="white"
        ).pack(anchor="w", pady=10)
        tk.Label(
            frame,
            text="EMAIL*",
            bg="white"
        ).pack(anchor="w", pady=10)

        self.entry_email = tk.Entry(frame, width=60)
        self.entry_email.pack(ipady=8)
        tk.Button(
            frame,
            text="GỬI",
            bg="black",
            fg="white",
            width=40,
            height=2,
            command=self.send_email
        ).pack(pady=20)

        tk.Button(
            frame,
            text="HUỶ",
            width=40,
            height=2,
            command=self.back_login
        ).pack()

        bottom = tk.Frame(frame, bg="white")
        bottom.pack(pady=30)

        tk.Label(
            bottom,
            text="ĐÃ CÓ TÀI KHOẢN?",
            bg="white"
        ).pack(side="left")

        tk.Button(
            bottom,
            text="ĐĂNG NHẬP",
            bd=0,
            fg="blue",
            command=self.back_login
        ).pack(side="left")

    def send_email(self):
        email = self.entry_email.get()
        try:
            with open("users.json", "r") as f:
                data = json.load(f)
        except:
            messagebox.showerror("Lỗi", "Không tìm thấy dữ liệu tài khoản")
            return

        for user in data:
            if user["email"] == email:
                messagebox.showinfo(
                    "Thành công",
                    "Email đặt lại mật khẩu đã được gửi"
                )
                return
        messagebox.showerror("Lỗi", "Email không tồn tại")

    def back_login(self):
        from DangNhap import DangNhapUI
        for w in self.root.winfo_children():
            w.destroy()
        DangNhapUI(self.root)
