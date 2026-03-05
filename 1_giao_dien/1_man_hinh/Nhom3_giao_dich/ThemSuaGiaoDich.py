import tkinter as tk
class ThemSuaGiaoDichUI:
    def __init__(self,root):
        frame = tk.Frame(root,padx=50,pady=40)
        frame.pack(fill="both",expand=True)

        tk.Label(
            frame,
            text="Thêm giao dịch",
            font=("Arial",20,"bold")
        ).pack(pady=20)
        fields = ["Ngày","Mô tả","Danh mục","Số tiền"]

        for f in fields:
            tk.Label(frame,text=f).pack(anchor="w")
            tk.Entry(frame,width=40).pack(pady=6)
        tk.Button(
            frame,
            text="Lưu giao dịch",
            width=25
        ).pack(pady=20)
