import tkinter as tk
from tkinter import messagebox
import json

class DangKyUI:

    def __init__(self,root):
        self.root = root
        frame = tk.Frame(root,bg="white",padx=100,pady=50)
        frame.pack(fill="both",expand=True)
        tk.Label(
            frame,
            text="Tạo tài khoản",
            font=("Arial",24,"bold"),
            bg="white"
        ).pack(pady=20)

        tk.Label(frame,text="Tên",bg="white").pack(anchor="w")
        self.entry_name = tk.Entry(frame,width=40)
        self.entry_name.pack(pady=5)

        tk.Label(frame,text="Email",bg="white").pack(anchor="w")
        self.entry_email = tk.Entry(frame,width=40)
        self.entry_email.pack(pady=5)

        tk.Label(frame,text="Mật khẩu",bg="white").pack(anchor="w")
        self.entry_pass = tk.Entry(frame,width=40,show="*")
        self.entry_pass.pack(pady=5)

        tk.Label(frame,text="Xác nhận mật khẩu",bg="white").pack(anchor="w")
        self.entry_repass = tk.Entry(frame,width=40,show="*")
        self.entry_repass.pack(pady=5)

        tk.Button(
            frame,
            text="Tạo tài khoản",
            width=25,
            command=self.register
        ).pack(pady=20)

    def register(self):
        name=self.entry_name.get()
        email=self.entry_email.get()
        password=self.entry_pass.get()
        repass=self.entry_repass.get()
        if password!=repass:
            messagebox.showerror("Lỗi","Mật khẩu không khớp")
            return
        user={
            "name":name,
            "email":email,
            "password":password
        }
        try:
            with open("users.json","r") as f:
                data=json.load(f)
        except:
            data=[]
        data.append(user)
        with open("users.json","w") as f:
            json.dump(data,f)
        messagebox.showinfo("Thành công","Đăng ký thành công, vui lòng đăng nhập lại")
        from DangNhap import DangNhapUI
        for w in self.root.winfo_children():
            w.destroy()
        DangNhapUI(self.root)
