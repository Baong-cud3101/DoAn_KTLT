class ManHinhHoSoCaNhan:
    def khi_cap_nhat_ho_so(self): pass




    
import tkinter as tk
from tkinter import messagebox
from dieu_khien.HoSo_Controller import HoSoController
class ManHinhHoSoCaNhan:
    def __init__(self, root, ma_nguoi_dung):
        self.root = root
        self.ma_nd = ma_nguoi_dung
        self.controller = HoSoController()
        frame = tk.Frame(root, bg="white", padx=40, pady=40)
        frame.pack(fill="both", expand=True)
        tk.Label(
            frame,
            text="Cập nhật thông tin cá nhân",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=10)
        tk.Label(frame, text="Mật khẩu cũ", bg="white").pack(anchor="w")
        self.entry_old_pass = tk.Entry(frame, show="*", width=40)
        self.entry_old_pass.pack(pady=5)
        tk.Label(frame, text="Mật khẩu mới", bg="white").pack(anchor="w")
        self.entry_new_pass = tk.Entry(frame, show="*", width=40)
        self.entry_new_pass.pack(pady=5)
        tk.Button(
            frame,
            text="Cập nhật",
            bg="#1cc5d8",
            fg="white",
            command=self.khi_cap_nhat_ho_so
        ).pack(pady=15)
    def khi_cap_nhat_ho_so(self):
        mat_khau_cu = self.entry_old_pass.get()
        mat_khau_moi = self.entry_new_pass.get()
        ket_qua = self.controller.doi_mat_khau(
            self.ma_nd,
            mat_khau_cu,
            mat_khau_moi
        )
        if ket_qua.get("success"):
            messagebox.showinfo("Thành công", "Đổi mật khẩu thành công")
            self.entry_old_pass.delete(0, tk.END)
            self.entry_new_pass.delete(0, tk.END)
            return
        message = ket_qua.get("message", "")
        if message == "SAI_MAT_KHAU_CU":
            messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng")
        elif message == "MAT_KHAU_YEU":
            messagebox.showerror("Lỗi", "Mật khẩu mới quá yếu (>= 6 ký tự)")
        elif message == "THIEU_DU_LIEU":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
        elif message == "KHONG_TON_TAI":
            messagebox.showerror("Lỗi", "Người dùng không tồn tại")
        else:
            messagebox.showerror("Lỗi", message)
