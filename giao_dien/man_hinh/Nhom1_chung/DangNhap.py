import tkinter as tk
from tkinter import messagebox
from dieu_khien.DangNhap_Controller import DieuKhienDangNhap
from giao_dien.man_hinh.Nhom1_chung.TrangChu import TrangChuUI
from giao_dien.man_hinh.Nhom1_chung.DangKy import DangKyUI
class DangNhapUI:
    def __init__(self, root):
        self.root = root
        self.controller = DieuKhienDangNhap()
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
        tk.Label(right, text="Email", bg="white").pack(anchor="w")
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
        ket_qua = self.controller.dang_nhap(email, password)
        if ket_qua.get("success"):
            messagebox.showinfo("Thành công", "Đăng nhập thành công")
            for w in self.root.winfo_children():
                w.destroy()
            TrangChuUI(self.root, email)
            return
        message = ket_qua.get("message", "")
        if message == "TAI_KHOAN_BI_KHOA":
            messagebox.showerror("Lỗi", "Tài khoản đã bị khóa")
        elif message == "SAI_MAT_KHAU":
            messagebox.showerror("Lỗi", "Sai mật khẩu")
        elif message == "KHONG_TON_TAI":
            messagebox.showerror("Lỗi", "Tài khoản không tồn tại")
        else:
            messagebox.showerror("Lỗi", message)
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
