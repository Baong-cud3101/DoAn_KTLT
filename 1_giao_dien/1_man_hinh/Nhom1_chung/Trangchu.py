import tkinter as tk
class TrangChuUI:
    def __init__(self,root,username):
        main = tk.Frame(root)
        main.pack(fill="both",expand=True)
        sidebar = tk.Frame(main,bg="#eeeeee",width=220)
        sidebar.pack(side="left",fill="y")
        tk.Label(
            sidebar,
            text="App Logo",
            bg="#eeeeee",
            font=("Arial",14,"bold")
        ).pack(pady=20)
        menus = [
            "Trang chủ",
            "Thu và chi",
            "Ngân sách",
            "Đầu tư",
            "Khoản vay",
            "Báo cáo",
            "Cài đặt"
        ]
        for m in menus:
            tk.Button(sidebar,text=m,width=18).pack(pady=6)
        content = tk.Frame(main,bg="white")
        content.pack(side="right",expand=True,fill="both")
        header = tk.Frame(content,bg="white")
        header.pack(fill="x",pady=10)
        tk.Label(
            header,
            text=f"Chào bạn, {username}",
            font=("Arial",16),
            bg="white"
        ).pack(side="left",padx=20)
        tk.Button(
            header,
            text="Thêm giao dịch"
        ).pack(side="right",padx=20)
        stat = tk.Frame(content,bg="white")
        stat.pack(pady=20)
        titles = ["Tổng thu","Tổng chi","Số dư"]
        for t in titles:
            box = tk.Frame(stat,bg="#dddddd",width=220,height=80)
            box.pack(side="left",padx=20)
            tk.Label(box,text=t,bg="#dddddd").place(relx=0.5,rely=0.5,anchor="center")
