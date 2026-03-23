import tkinter as tk
from tkinter import messagebox
from dieu_khien.DangKy_Controller import DieuKhienDangKy
class DangKyUI:
    def __init__(self, root):
        self.root = root
        self.controller = DieuKhienDangKy()
        main = tk.Frame(root)
        main.pack(fill="both", expand=True)
        right = tk.Frame(main, bg="white", padx=40, pady=40)
        right.pack(expand=True)
        tk.Label(
            right,
            text="Tạo tài khoản",
            font=("Arial", 22, "bold"),
            bg="white"
        ).pack(pady=15)
        tk.Label(right, text="Họ tên", bg="white").pack(anchor="w")
        self.entry_name = tk.Entry(right, width=35)
        self.entry_name.pack(pady=5)
        tk.Label(right, text="Email", bg="white").pack(anchor="w")
        self.entry_email = tk.Entry(right, width=35)
        self.entry_email.pack(pady=5)
        tk.Label(right, text="Mật khẩu", bg="white").pack(anchor="w")
        self.entry_pass = tk.Entry(right, width=35, show="*")
        self.entry_pass.pack(pady=5)
        tk.Label(right, text="SĐT", bg="white").pack(anchor="w")
        self.entry_sdt = tk.Entry(right, width=35)
        self.entry_sdt.pack(pady=5)
        tk.Button(
            right,
            text="Đăng ký",
            width=20,
            command=self.register
        ).pack(pady=15)
    def register(self):
        du_lieu = {
            "HoTen": self.entry_name.get(),
            "Email": self.entry_email.get(),
            "MatKhau": self.entry_pass.get(),
            "SoDT": self.entry_sdt.get()
        }

        res = self.controller.dang_ky(du_lieu)

        if not res["success"]:
            messagebox.showerror("Lỗi", res["message"])
            return

        self.ma_nd = res["MaND"]

        messagebox.showinfo(
            "Thông báo",
            "OTP đã gửi (xem console)"
        )

        self.nhap_otp()

    def nhap_otp(self):
        popup = tk.Toplevel(self.root)
        popup.title("Xác thực OTP")

        tk.Label(popup, text="Nhập OTP:").pack(pady=10)

        entry = tk.Entry(popup)
        entry.pack(pady=10)
        def xac_nhan():
            otp = entry.get()

            res = self.controller.xac_thuc_otp(self.ma_nd, otp)

            if res["success"]:
                messagebox.showinfo("Thành công", "Đăng ký thành công")
                popup.destroy()
            else:
                messagebox.showerror("Lỗi", res["message"])
        tk.Button(
            popup,
            text="Xác nhận",
            command=xac_nhan
        ).pack(pady=10)
