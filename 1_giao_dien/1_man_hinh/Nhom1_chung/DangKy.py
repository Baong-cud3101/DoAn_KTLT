import tkinter as tk
class DangKyUI:
    def __init__(self, root):
        frame = tk.Frame(root,bg="white",padx=100,pady=40)
        frame.pack(fill="both",expand=True)
        tk.Label(
            frame,
            text="Tạo tài khoản",
            font=("Arial",24,"bold"),
            bg="white"
        ).pack(pady=20)
        fields = [
            "Tên",
            "Họ",
            "Địa chỉ email",
            "Mật khẩu",
            "Xác nhận mật khẩu"
        ]
        for f in fields:
            tk.Label(frame,text=f,bg="white").pack(anchor="w")
            tk.Entry(frame,width=50).pack(pady=5)
        tk.Checkbutton(
            frame,
            text="Đồng ý với các điều khoản sử dụng",
            bg="white"
        ).pack(pady=10)
        tk.Button(
            frame,
            text="Tạo tài khoản",
            width=25
        ).pack(pady=10)
        tk.Label(
            frame,
            text="Đã có tài khoản ? Đăng nhập",
            bg="white"
        ).pack()
