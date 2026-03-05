import tkinter as tk

class TrangChuUI:
    def __init__(self,root):
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
            tk.Button(
                sidebar,
                text=m,
                width=18
            ).pack(pady=6)

        content = tk.Frame(main,bg="white")
        content.pack(side="right",expand=True,fill="both")
        header = tk.Frame(content,bg="white")
        header.pack(fill="x",pady=10)
        tk.Label(
            header,
            text="Chào bạn, Nguyễn Văn A",
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

        chart = tk.Frame(content,bg="white")
        chart.pack(pady=30)
        line = tk.Frame(chart,bg="#e5e5e5",width=400,height=200)
        line.pack(side="left",padx=30)
        tk.Label(line,text="Biểu đồ thu chi").place(relx=0.5,rely=0.5,anchor="center")
        pie = tk.Frame(chart,bg="#e5e5e5",width=300,height=200)
        pie.pack(side="right",padx=30)

        tk.Label(pie,text="Cơ cấu chi").place(relx=0.5,rely=0.5,anchor="center")
        warn = tk.Frame(content,bg="#eaeaea",width=800,height=150)
        warn.pack(pady=20)
        tk.Label(
            warn,
            text="Cảnh báo ngân sách",
            bg="#eaeaea",
            font=("Arial",12,"bold")
        ).place(x=20,y=10)
