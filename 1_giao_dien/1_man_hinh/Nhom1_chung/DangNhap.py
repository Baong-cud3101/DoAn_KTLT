import tkinter as tk
class DangNhapUI:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack(fill="both", expand=True)
        left = tk.Frame(frame, bg="#1cc5d8", width=400)
        left.pack(side="left", fill="y")
        tk.Label(
            left,
            text="APP",
            font=("Arial",40),
            fg="white",
            bg="#1cc5d8"
        ).place(relx=0.5,rely=0.5,anchor="center")
        right = tk.Frame(frame, bg="white", padx=40, pady=40)
        right.pack(side="right", expand=True)
        tk.Label(right,text="Đăng nhập",font=("Arial",22),bg="white").pack(pady=20)
        tk.Label(right,text="Email hoặc tên đăng nhập",bg="white").pack(anchor="w")
        tk.Entry(right,width=35).pack(pady=5)
        tk.Label(right,text="Mật khẩu",bg="white").pack(anchor="w")
        tk.Entry(right,width=35,show="*").pack(pady=5)
        tk.Button(right,text="Đăng nhập",width=20).pack(pady=20)
        tk.Label(right,text="Quên mật khẩu",fg="blue",bg="white").pack()
        tk.Label(right,text="Chưa có tài khoản? Đăng ký",bg="white").pack(pady=10)
