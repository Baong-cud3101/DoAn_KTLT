import tkinter as tk
from Nhom1_chung.Trangchu import TrangChuUI

class DangNhapUI:
    def __init__(self, root):
        self.root = root
        frame = tk.Frame(root)
        frame.pack(fill="both",expand=True)
        left = tk.Frame(frame,bg="#1cc5d8",width=450)
        left.pack(side="left",fill="y")
        tk.Label(
            left,
            text="LOGO",
            bg="#1cc5d8",
            fg="white",
            font=("Arial",40,"bold")
        ).place(relx=0.5,rely=0.5,anchor="center")

        right = tk.Frame(frame,bg="white",padx=60,pady=60)
        right.pack(side="right",expand=True)
        tk.Label(
            right,
            text="Đăng nhập",
            font=("Arial",24,"bold"),
            bg="white"
        ).pack(pady=20)
        tk.Label(right,text="Email hoặc tên đăng nhập",bg="white").pack(anchor="w")
        self.user = tk.Entry(right,width=35)
        self.user.pack(pady=8)
        tk.Label(right,text="Mật khẩu",bg="white").pack(anchor="w")
        self.pw = tk.Entry(right,width=35,show="*")
        self.pw.pack(pady=8)

        tk.Button(
            right,
            text="Đăng nhập",
            width=20,
            command=self.login
        ).pack(pady=20)
        tk.Label(right,text="Quên mật khẩu",fg="blue",bg="white").pack()
        tk.Label(right,text="Chưa có tài khoản ? Đăng ký",bg="white").pack(pady=10)
    def login(self):
        for w in self.root.winfo_children():
            w.destroy()
        TrangChuUI(self.root)
