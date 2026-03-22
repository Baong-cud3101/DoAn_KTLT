import tkinter as tk
from tkinter import messagebox
import json
from TrangChu import TrangChuUI
def open_register(self):
    from DangKy import DangKyUI


class DangNhapUI:
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
            text="Đăng nhập",
            font=("Arial", 22, "bold"),
            bg="white"
        ).pack(pady=20)

        tk.Label(right, text="Email hoặc tên đăng nhập", bg="white").pack(anchor="w")
        self.entry_email = tk.Entry(right, width=35)
        self.entry_email.pack(pady=5)

        tk.Label(right, text="Mật khẩu", bg="white").pack(anchor="w")
        self.entry_pass = tk.Entry(right, width=35, show="*")
        self.entry_pass.pack(pady=5)

        tk.Button(
            right,
            text="Đăng nhập",
            width=20,
            command=self.login
        ).pack(pady=15)
        tk.Label(
            right,
            text="Quên mật khẩu",
            fg="blue",
            bg="white"
        ).pack()
        register_frame = tk.Frame(right, bg="white")
        register_frame.pack(pady=10)
        tk.Label(register_frame, text="Chưa có tài khoản ?", bg="white").pack(side="left")
        tk.Button(
            register_frame,
            text="Đăng ký",
            command=self.open_register
        ).pack(side="left")

    def login(self):
        email = self.entry_email.get()
        password = self.entry_pass.get()
        try:
            with open("users.json", "r") as f:
                data = json.load(f)
        except:
            messagebox.showerror("Lỗi", "Chưa có tài khoản nào")
            return
        for user in data:
            if user["email"] == email and user["password"] == password:
                for w in self.root.winfo_children():
                    w.destroy()
                TrangChuUI(self.root, user["name"])
                return
        messagebox.showerror("Lỗi", "Sai thông tin đăng nhập")

    def open_register(self):
        for w in self.root.winfo_children():
            w.destroy()
        DangKyUI(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Finance App")
    root.geometry("1000x600")
    DangNhapUI(root)

    root.mainloop()
