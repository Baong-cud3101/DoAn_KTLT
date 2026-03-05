import tkinter as tk

class TrangChuUI:
    def __init__(self, root):
        main = tk.Frame(root)
        main.pack(fill="both", expand=True)
        sidebar = tk.Frame(main, bg="#eeeeee", width=200)
        sidebar.pack(side="left", fill="y")
        buttons = [
            "Trang chủ",
            "Giao dịch",
            "Ngân sách",
            "Đầu tư",
            "Vay nợ",
            "Báo cáo",
            "Cài đặt"
        ]
        for b in buttons:
            tk.Button(
                sidebar,
                text=b,
                width=20
            ).pack(pady=5)
        content = tk.Frame(main, bg="white")
        content.pack(side="right", expand=True, fill="both")
        tk.Label(
            content,
            text="Chào bạn, Nguyễn Văn A",
            font=("Arial",16),
            bg="white"
        ).pack(pady=10)
        stats = tk.Frame(content,bg="white")
        stats.pack()
        for t in ["Tổng thu","Tổng chi","Số dư"]:
            box = tk.Frame(stats,bg="#dddddd",width=180,height=70)
            box.pack(side="left",padx=20,pady=20)
            tk.Label(box,text=t,bg="#dddddd").place(relx=0.5,rely=0.5,anchor="center")
