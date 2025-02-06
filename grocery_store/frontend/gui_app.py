# Add the parent directory of 'middleware' to the Python path
import os
import sys
from pathlib import Path
import datetime
import tkinter as tk
from tkinter import Button, Canvas, Entry, PhotoImage, ttk, messagebox
import cv2
import pyzbar


sys.path.append(str(Path(__file__).resolve().parent.parent))

from middleware.product8recipt import Product, Recipt
from backend import conn2db
# from pyzbar.pyzbar import decode


class Home:
    '''Class chứa các thành phần giao diện của cửa sổ chính, bao gồm:
    - Hình ảnh nền
    - Các nút chức năng
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Quản lý Bán Hàng")
        self.root.geometry("1512x982")
        self.root.configure(bg = "#FFFFFF")
        self.root.resizable(False, False)
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\chien\OneDrive\Application\grocery_store\frontend\assets\frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.canvas = Canvas(
            root,
            bg = "#FFFFFF",
            height = 982,
            width = 1512,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            867.0,
            536.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            90.0,
            223.0,
            982.0,
            fill="#FFFFFE",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1512.0,
            90.0,
            fill="#4795BC",
            outline="")

        def button_inentory_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Invenroty(root)
            root.mainloop()
            
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=button_inentory_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=11.0,
            y=517.0,
            width=200.0,
            height=40.0
        )
            
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 repeat to home page clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=11.0,
            y=446.0,
            width=200.0,
            height=40.0
        )

        def button_summary_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Summary(root)
            root.mainloop()
                    
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=button_summary_clicked,
            relief="flat"
        )
        self.button_3.place(
            x=11.0,
            y=589.0,
            width=200.0,
            height=40.0
        )

        def button_warehouse_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Warehouse(root)
            root.mainloop()
            
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=button_warehouse_clicked,
            relief="flat"
        )
        self.button_4.place(
            x=707.0,
            y=108.0,
            width=320.0,
            height=96.0
        )

        def button_product_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Invenroty(root)
            root.mainloop()
            
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=button_product_clicked,
            relief="flat"
        )
        self.button_5.place(
            x=1107.0,
            y=108.0,
            width=320.0,
            height=96.0
        )

        
        def button_sell_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Sell(root)
            root.mainloop()
            
        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=button_sell_clicked,
            relief="flat"
        )
        self.button_6.place(
            x=307.0,
            y=108.0,
            width=320.0,
            height=96.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            111.0,
            210.0,
            image=self.image_image_2
        )
        
       
        
        
class Invenroty:
    '''Class chứa các thành phần giao diện của cửa sổ quản lý hàng hóa, bao gồm:
    - Bảng hiển thị hàng hóa
    - Các nút chức năng
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Kho hàng hóa")
        self.root.geometry("1512x982")
        self.root.configure(bg = "#FFFFFF")
        self.root.resizable(False, False)
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\chien\OneDrive\Application\grocery_store\frontend\assets\frame1")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.canvas = Canvas(
            root,
            bg = "#F3F9FB",
            height = 982,
            width = 1512,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            284.0,
            299.0,
            1401.0,
            928.0,
            fill="#F3F9FB",
            outline="")

        self.canvas.create_rectangle( # background table
            284.0,
            299.0,
            1464.0,
            928.0,
            fill="#FFFFFE",
            outline="")

        self.canvas.create_rectangle( # background title table
            284.0,
            299.0,
            1464.0,
            351.0,
            fill="#E7EFF2",
            outline="")

        self.canvas.create_rectangle(
            283.0,
            350.0,
            1464.0,
            351.0,
            fill="#E0E0E0",
            outline="")

        self.canvas.create_text(
            500.0,
            313.0,
            anchor="nw",
            text="Sản phẩm",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            324.0,
            313.0,
            anchor="nw",
            text="Barcode",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            828.0,
            313.0,
            anchor="nw",
            text="Số lượng",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            1030.0,
            313.0,
            anchor="nw",
            text="Hạn SD",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            1307.0,
            313.0,
            anchor="nw",
            text="Giá",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_rectangle( # menu bar
            0.0,
            90.0,
            223.0,
            982.0,
            fill="#FFFFFE",
            outline="")
        # tạo bảng hiển thị danh sách các sản phẩm lấy từ cơ sở dữ liệu với chức năng cuộn
        frame = tk.Frame(self.root)
        frame.place(x=284, y=351, width=1180, height=577)

        canvas = tk.Canvas(frame, bg="#FFFFFE")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#FFFFFE")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        table = ttk.Treeview(scrollable_frame, selectmode='browse')
        table['columns'] = ('1', '2', '3', '4', '5')
        # table['show'] = 'headings'
        # table.heading('1', text='Barcode')
        # table.heading('2', text='Tên sản phẩm')
        # table.heading('3', text='Số lượng')
        # table.heading('4', text='Hạn SD')
        # table.heading('5', text='Giá')

        table.column('#1', stretch=False, minwidth=25, width=30, anchor='c')
        table.column('#2', stretch=False, minwidth=25, width=62, anchor='c')
        table.column('#3', stretch=False, minwidth=35, width=87, anchor='w')
        table.column('#4', stretch=False, minwidth=50, width=65, anchor='w')
        table.column('#5', stretch=False, minwidth=25, width=35, anchor='w')

        table.pack(fill='both', expand=True)
        
        # Lấy dữ liệu từ cơ sở dữ liệu
        conn = conn2db.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        conn.close()

        for i, product in enumerate(products, start=1):
            bg_color = "#F3F9FB" if i % 2 == 0 else "#FFFFFE"
            tk.Label(table, text=product[0], bg=bg_color, font=("Lato Bold", 20 * -1)).grid(row=i, column=0, sticky="w", padx=10, pady=5)
            tk.Label(table, text=product[1], bg=bg_color, font=("Lato Bold", 20 * -1)).grid(row=i, column=1, sticky="nsew", padx=20, pady=5)
            tk.Label(table, text=product[2], bg=bg_color, font=("Lato Bold", 20 * -1)).grid(row=i, column=2, sticky="w", padx=20, pady=5)
            tk.Label(table, text=product[3], bg=bg_color, font=("Lato Bold", 20 * -1)).grid(row=i, column=3, sticky="w", padx=20, pady=5)
            tk.Label(table, text=product[4], bg=bg_color, font=("Lato Bold", 20 * -1)).grid(row=i, column=4, sticky="w", padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('vista')
        style.configure('Treeview')
        table.tag_configure('oddrow', background='#90e0ef')
        
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            111.0,  
            210.0,
            image=self.image_image_1
        )

        def button_home_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Home(root)
            root.mainloop()
        
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=button_home_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=11.0,
            y=444.0,
            width=200.0,
            height=40.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 repeat to inventory page clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=12.0,
            y=516.0,
            width=200.0,
            height=40.0
        )

        def button_summary_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Summary(root)
            root.mainloop()
            
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=button_summary_clicked,
            relief="flat"
        )
        self.button_3.place(
            x=12.0,
            y=588.0,
            width=200.0,
            height=40.0
        )

        self.canvas.create_text(
            285.0,
            140.0,
            anchor="nw",
            text="Kho hàng",
            fill="#112E3F",
            font=("Lato Bold", 32 * -1)
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=271.0,
            y=217.0,
            width=71.0,
            height=30.0
        )

        def button_expire_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Invenroty(root).expire_product()
            root.mainloop()
            
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=button_expire_clicked,
            relief="flat"
        )
        self.button_5.place(
            x=383.0,
            y=216.0,
            width=130.0,
            height=34.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1512.0,
            90.0,
            fill="#4795BC",
            outline="")

        self.canvas.create_rectangle(
            293.0,
            255.0,
            318.0,
            259.0,
            fill="#495C69",
            outline="")
        
    def expire_product(self):
        '''Chuyển sang thẻ hàng hóa hết hạn sử dụng từ cửa sổ quản lý hàng hóa
        - Hiển thị danh sách hàng hóa hết hạn sử dụng
        - Các nút chức năng
        '''
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\chien\OneDrive\Application\grocery_store\frontend\assets\frame3")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.canvas = Canvas(
            self.root,
            bg = "#F3F9FB",
            height = 982,
            width = 1512,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            284.0,
            299.0,
            1401.0,
            928.0,
            fill="#F3F9FB",
            outline="")

        self.canvas.create_rectangle(
            284.0,
            299.0,
            1464.0,
            928.0,
            fill="#FFFFFE",
            outline="")

        self.canvas.create_rectangle(
            284.0,
            299.0,
            1464.0,
            351.0,
            fill="#E7EFF2",
            outline="")

        self.canvas.create_rectangle(
            283.0,
            350.0,
            1464.0,
            351.0,
            fill="#E0E0E0",
            outline="")

        self.canvas.create_text(
            500.0,
            313.0,
            anchor="nw",
            text="Sản phẩm",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            324.0,
            313.0,
            anchor="nw",
            text="Barcode",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            828.0,
            313.0,
            anchor="nw",
            text="Sô lượng",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            1030.0,
            313.0,
            anchor="nw",
            text="Hạn SD",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            1268.0,
            313.0,
            anchor="nw",
            text="Ngày còn lại",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            285.0,
            140.0,
            anchor="nw",
            text="Kho hàng",
            fill="#112E3F",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1512.0,
            90.0,
            fill="#4795BC",
            outline="")

        self.canvas.create_rectangle(
            435.0,
            255.0,
            460.0,
            259.0,
            fill="#495C69",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            90.0,
            223.0,
            982.0,
            fill="#FFFFFE",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            111.0,
            210.0,
            image=self.image_image_1
        )

        def button_home_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Home(root)
            root.mainloop()
            
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=button_home_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=11.0,
            y=444.0,
            width=200.0,
            height=40.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 repeat to inventory page clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=12.0,
            y=516.0,
            width=200.0,
            height=40.0
        )

        def button_summary_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Summary(root)
            root.mainloop()
            
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=button_summary_clicked,
            relief="flat"
        )
        self.button_3.place(
            x=12.0,
            y=588.0,
            width=200.0,
            height=40.0
        )

        def button_product_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Invenroty(root)
            root.mainloop()
            
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=button_product_clicked,
            relief="flat"
        )
        self.button_4.place(
            x=271.0,
            y=217.0,
            width=71.0,
            height=30.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=383.0,
            y=216.0,
            width=130.0,
            height=34.0
        )
    
class Sell:
    '''Class chứa các thành phần giao diện của cửa sổ bán hàng hóa, bao gồm:
    - Bảng hiển thị hóa đơn bán hàng hóa khi quét từ mã vạch
    - Các nút chức năng
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Bán hàng hóa")
        self.root.geometry("1512x982")
        self.root.configure(bg = "#FFFFFF")
        self.root.resizable(False, False)
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\chien\OneDrive\Application\grocery_store\frontend\assets\frame4")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.canvas = Canvas(
            root,
            bg = "#F3F9FB",
            height = 982,
            width = 1512,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            287.0,
            140.0,
            anchor="nw",
            text="Bán hàng",
            fill="#112E3F",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1512.0,
            90.0,
            fill="#4795BC",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=277.0,
            y=217.0,
            width=57.0,
            height=34.0
        )

        def button_history_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Sell(root).history()
            root.mainloop()
            
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=button_history_clicked,
            relief="flat"
        )
        self.button_2.place(
            x=403.0,
            y=215.0,
            width=88.0,
            height=36.0
        )

        self.canvas.create_rectangle(
            293.0,
            255.0,
            318.0,
            259.0,
            fill="#495C69",
            outline="")

        self.canvas.create_rectangle(
            283.0,
            289.0,
            1398.0,
            859.0,
            fill="#F3F9FB",
            outline="")

        self.canvas.create_rectangle(
            284.0,
            289.0,
            1464.0,
            859.0,
            fill="#FFFFFE",
            outline="")

        self.canvas.create_rectangle(
            282.0,
            340.9999999999997,
            1463.0,
            342.0,
            fill="#E0E0E0",
            outline="")

        self.canvas.create_rectangle(
            283.0,
            289.0,
            1463.0,
            341.0,
            fill="#E7EFF2",
            outline="")

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=744.0,
            y=875.0,
            width=193.0,
            height=60.0
        )

        self.canvas.create_text(
            400.0,
            300.0,
            anchor="nw",
            text="ID:",
            fill="#112E3F",
            font=("Lato Bold", 24 * -1)
        )

        self.canvas.create_text(
            650.0,
            300.0,
            anchor="nw",
            text="Ngày:",
            fill="#112E3F",
            font=("Lato Bold", 24 * -1)
        )

        self.canvas.create_text(
            1000.0,
            300.0,
            anchor="nw",
            text="Tổng:",
            fill="#112E3F",
            font=("Lato Bold", 24 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            90.0,
            223.0,
            982.0,
            fill="#FFFFFE",
            outline="")

        def button_inventory_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Invenroty(root)
            root.mainloop()
            
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=button_inventory_clicked,
            relief="flat"
        )
        self.button_4.place(
            x=11.0,
            y=517.0,
            width=200.0,
            height=40.0
        )

        def button_home_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Home(root)
            root.mainloop()
        
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=button_home_clicked,
            relief="flat"
        )
        self.button_5.place(
            x=11.0,
            y=446.0,
            width=200.0,
            height=40.0
        )

        def button_summary_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Summary(root)
            root.mainloop()
            
        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=button_summary_clicked,
            relief="flat"
        )
        self.button_6.place(
            x=11.0,
            y=589.0,
            width=200.0,
            height=40.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            111.0,
            210.0,
            image=self.image_image_1
        )
        
    def history(self):
        '''Chuyển sang thẻ lịch sử bán hàng từ cửa sổ bán hàng
        - Hiển thị lịch sử bán hàng
        - Các nút chức năng
        '''
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\chien\OneDrive\Application\grocery_store\frontend\assets\frame5")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.canvas = Canvas(
            self.root,
            bg = "#F3F9FB",
            height = 982,
            width = 1512,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            287.0,
            140.0,
            anchor="nw",
            text="Bán hàng",
            fill="#112E3F",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1512.0,
            90.0,
            fill="#4795BC",
            outline="")

        self.canvas.create_rectangle(
            435.0,
            255.0,
            460.0,
            259.0,
            fill="#495C69",
            outline="")

        self.canvas.create_rectangle(
            293.0,
            295.0,
            1410.0,
            950.0,
            fill="#F3F9FB",
            outline="")

        self.canvas.create_rectangle(
            284.0,
            289.0,
            1464.0,
            944.0,
            fill="#FFFFFE",
            outline="")

        self.canvas.create_rectangle(
            284.0,
            289.0,
            1464.0,
            341.0,
            fill="#E7EFF2",
            outline="")

        self.canvas.create_rectangle(
            283.0,
            341.0,
            1464.0,
            342.0,
            fill="#E0E0E0",
            outline="")

        self.canvas.create_text(
            647.0,
            303.0,
            anchor="nw",
            text="Day",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            325.0,
            303.0,
            anchor="nw",
            text="ID",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            983.0,
            303.0,
            anchor="nw",
            text="Price",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_text(
            1328.0,
            303.0,
            anchor="nw",
            text="Look at",
            fill="#495C69",
            font=("Lato Bold", 20 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            90.0,
            223.0,
            982.0,
            fill="#FFFFFE",
            outline="")

        def button_inventory_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Invenroty(root)
            root.mainloop()
            
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=button_inventory_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=11.0,
            y=517.0,
            width=200.0,
            height=40.0
        )
        
        def button_home_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Home(root)
            root.mainloop()
            
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=button_home_clicked,
            relief="flat"
        )
        self.button_2.place(
            x=11.0,
            y=446.0,
            width=200.0,
            height=40.0
        )

        def button_summary_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Summary(root)
            root.mainloop()
            
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=button_summary_clicked,
            relief="flat"
        )
        self.button_3.place(
            x=11.0,
            y=589.0,
            width=200.0,
            height=40.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            111.0,
            210.0,
            image=self.image_image_1
        )

        def button_sell_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Sell(root)
            root.mainloop()
            
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=button_sell_clicked,
            relief="flat"
        )
        self.button_4.place(
            x=277.0,
            y=217.0,
            width=57.0,
            height=34.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=403.0,
            y=215.0,
            width=88.0,
            height=36.0
        )
     
                        
            
class Warehouse:
    '''Class chứa các thành phần giao diện của cửa sổ nhập hàng vào kho, bao gồm:
    - Các entry để nhập thông tin hàng hóa
    - Các nút chức năng
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Kho hàng")
        self.root.geometry("1512x982")
        self.root.configure(bg = "#FFFFFF")
        self.root.resizable(False, False)
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\chien\OneDrive\Application\grocery_store\frontend\assets\frame2")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.canvas = Canvas(
            root,
            bg = "#F3F9FB",
            height = 982,
            width = 1512,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1512.0,
            90.0,
            fill="#4795BC",
            outline="")

        self.canvas.create_rectangle(
            284.0,
            108.0,
            1464.0,
            958.0,
            fill="#FFFFFE",
            outline="")

        self.canvas.create_rectangle(
            283.0,
            159.0,
            1464.0,
            160.0,
            fill="#E0E0E0",
            outline="")

        self.canvas.create_rectangle(
            284.0,
            109.0,
            1464.0,
            161.0,
            fill="#E7EFF2",
            outline="")

        self.canvas.create_text(
            804.0,
            115.0,
            anchor="nw",
            text="Nhập kho",
            fill="#495C69",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_text(
            565.0,
            243.0,
            anchor="nw",
            text="Barcode",
            fill="#495C69",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_text(
            565.0,
            325.0,
            anchor="nw",
            text="Tên",
            fill="#495C69",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_text(
            525.0,
            406.0,
            anchor="nw",
            text="Số lượng",
            fill="#495C69",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_text(
            565.0,
            488.0,
            anchor="nw",
            text="Hạn SD",
            fill="#495C69",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_text(
            565.0,
            570.0,
            anchor="nw",
            text="Giá",
            fill="#495C69",
            font=("Lato Bold", 32 * -1)
        )
            
        # Hàm xử lý khi nhấn nút Thêm hàng hóa
        def add_product():
            '''Thêm thông tin hàng hóa vào kho
            - Lưu thông tin hàng hóa vào database
            - Hiển thị thông tin hàng hóa trên bảng
            '''
            # Lấy thông tin hàng hóa từ entry
            barcode = self.entry_barcode.get()
            product_name = self.entry_product_name.get()
            amount = self.entry_amount.get()
            expire = self.entry_expire.get()
            price = self.entry_price.get()
            print(barcode, product_name, amount, expire, price)


            # Validate the inputs
            if not barcode.isdigit() or len(barcode) != 13:
                messagebox.showerror("Invalid Input", "Barcode must be a 13-digit number.")
                return
            if not amount.isdigit():
                messagebox.showerror("Invalid Input", "Amount must be an integer.")
                return
            try:
                day, month, year = map(int, expire.split('/'))
                expire_date = datetime.date(year, month, day)
            except ValueError:
                messagebox.showerror("Invalid Input", "Expire date must be in the format dd/mm/yy.")
                return
            try:
                price = float(price)
            except ValueError:
                messagebox.showerror("Invalid Input", "Price must be a real number.")
                return
            new_product = Product(barcode, product_name, amount, expire_date, price)
            # Add product to database
            conn2db.add_product_2db(new_product)
            messagebox.showinfo("Success", "Product added successfully.")
            
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=add_product,
            relief="flat"
        )
        self.button_1.place(
            x=698.0,
            y=833.0,
            width=315.0,
            height=60.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            1010.0,
            268.0,
            image=self.entry_image_1
        )
        self.entry_barcode = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        # Thay đổi cỡ chữ khi click chuột vào entry
        self.entry_barcode.bind("<Key>", lambda event: self.entry_barcode.config(font=("Lato Bold", 15)))
        
        
        # Hiển thị entry khi click vào background mã vạch
        def show_entry_barcode(event):
            self.entry_barcode.place(
                x=785.0,
                y=243.0,
                width=450.0,
                height=48.0
            )
            self.canvas.delete(self.entry_bg_1)
            self.entry_barcode.focus_set()
            # def scan_barcode():
            #     '''Sử dụng camera để quét mã vạch và trả về giá trị mã vạch'''
            #     cap = cv2.VideoCapture(0)
            #     barcode_data = None

            #     while True:
            #         ret, frame = cap.read()
            #         if not ret:
            #             break

            #         barcodes = pyzbar.decode(frame)
            #         for barcode in barcodes:
            #             barcode_data = barcode.data.decode("utf-8")
            #             cv2.rectangle(frame, (barcode.rect.left, barcode.rect.top), 
            #                           (barcode.rect.left + barcode.rect.width, barcode.rect.top + barcode.rect.height), 
            #                           (0, 255, 0), 2)
            #             cv2.putText(frame, barcode_data, (barcode.rect.left, barcode.rect.top - 10), 
            #                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            #         cv2.imshow("Barcode Scanner", frame)
            #         if cv2.waitKey(1) & 0xFF == ord('q') or barcode_data:
            #             break

            #     cap.release()
            #     cv2.destroyAllWindows()
            #     return barcode_data

            # # Sử dụng hàm scan_barcode để quét mã vạch và điền vào entry_barcode
            # barcode = scan_barcode()
            # if barcode:
            #     self.entry_barcode.insert(0, barcode)
            #     while not barcode:
            #         barcode = scan_barcode()
            #     if barcode:
            #         self.entry_barcode.insert(0, barcode)

        def hide_entry_barcode(event):
            if self.entry_barcode.get() == "":
                self.entry_barcode.place_forget()
                self.entry_bg_1 = self.canvas.create_image(
                    1010.0,
                    268.0,
                    image=self.entry_image_1
                )
                self.canvas.tag_bind(self.entry_bg_1, "<Button-1>", show_entry_barcode)

        self.canvas.tag_bind(self.entry_bg_1, "<Button-1>", show_entry_barcode)
        self.entry_barcode.bind("<FocusOut>", hide_entry_barcode)

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            1010.0,
            428.0,
            image=self.entry_image_2
        )
        self.entry_amount = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        # Thay đổi cỡ chữ khi click chuột vào entry
        self.entry_amount.bind("<Key>", lambda event: self.entry_amount.config(font=("Lato Bold", 15)))
        
        
        # Hiển thị entry khi click vào background số lượng
        def show_entry_amount(event):
            self.entry_amount.place(
                x=785.0,
                y=403.0,
                width=450.0,
                height=48.0
            )
            self.canvas.delete(self.entry_bg_2)
            self.entry_amount.focus_set()

        def hide_entry_amount(event):
            if self.entry_amount.get() == "":
                self.entry_amount.place_forget()
                self.entry_bg_2 = self.canvas.create_image(
                    1010.0,
                    428.0,
                    image=self.entry_image_2
                )
                self.canvas.tag_bind(self.entry_bg_2, "<Button-1>", show_entry_amount)

        self.canvas.tag_bind(self.entry_bg_2, "<Button-1>", show_entry_amount)
        self.entry_amount.bind("<FocusOut>", hide_entry_amount)
        

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            1010.0,
            348.0,
            image=self.entry_image_3
        )
        self.entry_product_name = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        
        # Thay đổi cỡ chữ nhập vào từ bàn phím của entry
        self.entry_product_name.bind("<Key>", lambda event: self.entry_product_name.config(font=("Lato Bold", 15)))
        
        # Hiển thị entry khi click vào background tên hàng hóa
        def show_entry_product_name(event):
            self.entry_product_name.place(
                x=785.0,
                y=323.0,
                width=450.0,
                height=48.0
            )
            self.canvas.delete(self.entry_bg_3)
            self.entry_product_name.focus_set()

        def hide_entry_product_name(event):
            if self.entry_product_name.get() == "":
                self.entry_product_name.place_forget()
                self.entry_bg_3 = self.canvas.create_image(
                    1010.0,
                    348.0,
                    image=self.entry_image_3
                )
                self.canvas.tag_bind(self.entry_bg_3, "<Button-1>", show_entry_product_name)

        self.canvas.tag_bind(self.entry_bg_3, "<Button-1>", show_entry_product_name)
        self.entry_product_name.bind("<FocusOut>", hide_entry_product_name)
        
        
        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            1010.0,
            508.0,
            image=self.entry_image_4
        )
        self.entry_expire = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        # Thay đổi cỡ chữ khi click chuột vào entry
        self.entry_expire.bind("<Key>", lambda event: self.entry_expire.config(font=("Lato Bold", 15)))
        
        # Hiển thị entry khi click vào background hạn sử dụng
        def show_entry_expire(event):
            self.entry_expire.place(
                x=785.0,
                y=483.0,
                width=450.0,
                height=48.0
            )
            self.canvas.delete(self.entry_bg_4)
            self.entry_expire.focus_set()

        def hide_entry_expire(event):
            if self.entry_expire.get() == "":
                self.entry_expire.place_forget()
                self.entry_bg_4 = self.canvas.create_image(
                    1010.0,
                    508.0,
                    image=self.entry_image_4
                )
                self.canvas.tag_bind(self.entry_bg_4, "<Button-1>", show_entry_expire)

        self.canvas.tag_bind(self.entry_bg_4, "<Button-1>", show_entry_expire)
        self.entry_expire.bind("<FocusOut>", hide_entry_expire)
        

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            1010.0,
            588.0,
            image=self.entry_image_5
        )
        self.entry_price = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        # Thay đổi cỡ chữ khi click chuột vào entry
        self.entry_price.bind("<Key>", lambda event: self.entry_price.config(font=("Lato Bold", 15)))
       
        # Hiển thị entry khi click vào background giá
        def show_entry_price(event):
            self.entry_price.place(
                x=785.0,
                y=563.0,
                width=450.0,
                height=48.0
            )
            self.canvas.delete(self.entry_bg_5)
            self.entry_price.focus_set()

        def hide_entry_price(event):
            if self.entry_price.get() == "":
                self.entry_price.place_forget()
                self.entry_bg_5 = self.canvas.create_image(
                    1010.0,
                    588.0,
                    image=self.entry_image_5
                )
                self.canvas.tag_bind(self.entry_bg_5, "<Button-1>", show_entry_price)

        self.canvas.tag_bind(self.entry_bg_5, "<Button-1>", show_entry_price)
        self.entry_price.bind("<FocusOut>", hide_entry_price)


        self.canvas.create_rectangle(
            0.0,
            90.0,
            223.0,
            982.0,
            fill="#FFFFFE",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            111.0,
            210.0,
            image=self.image_image_1
        )

        def button_home_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Home(root)
            root.mainloop()
        
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=button_home_clicked,
            relief="flat"
        )
        self.button_2.place(
            x=11.0,
            y=444.0,
            width=200.0,
            height=40.0
        )

        def button_inventory_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Invenroty(root)
            root.mainloop()
            
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=button_inventory_clicked,
            relief="flat"
        )
        self.button_3.place(
            x=12.0,
            y=516.0,
            width=200.0,
            height=40.0
        )

        def button_summary_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Summary(root)
            root.mainloop()
            
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=button_summary_clicked,
            relief="flat"
        )
        self.button_4.place(
            x=12.0,
            y=588.0,
            width=200.0,
            height=40.0
        )
        
        
class Summary:
    '''Class chứa các thành phần giao diện của cửa sổ thống kê doanh thu hàng hóa, bao gồm:
    - Hiển thị thống kê doanh thu hàng hóa
    - Các nút chức năng
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Thống kê hàng hóa")
        self.root.geometry("1512x982")
        self.root.configure(bg = "#FFFFFF")
        self.root.resizable(False, False)
        
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\chien\OneDrive\Application\grocery_store\frontend\assets\frame6")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        self.canvas = Canvas(
            root,
            bg = "#F3F9FB",
            height = 982,
            width = 1512,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            254.0,
            140.0,
            anchor="nw",
            text="Tổng kết ngày",
            fill="#112E3F",
            font=("Lato Bold", 32 * -1)
        )

        self.canvas.create_text(
            451.0,
            249.0,
            anchor="nw",
            text="Số hóa đơn",
            fill="#112E3F",
            font=("Lato ExtraBold", 32 * -1)
        )

        self.canvas.create_text(
            494.0,
            289.0,
            anchor="nw",
            text="15",
            fill="#112E3F",
            font=("Lato ExtraBold", 64 * -1)
        )

        self.canvas.create_text(
            1023.0,
            303.0,
            anchor="nw",
            text="1500000",
            fill="#112E3F",
            font=("Lato ExtraBold", 64 * -1)
        )

        self.canvas.create_text(
            1023.0,
            249.0,
            anchor="nw",
            text="Tổng thu",
            fill="#112E3F",
            font=("Lato ExtraBold", 32 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1512.0,
            90.0,
            fill="#4795BC",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            90.0,
            223.0,
            982.0,
            fill="#FFFFFE",
            outline="")

        self.canvas.create_rectangle(
            292.0,
            542.0,
            1409.0,
            881.0,
            fill="#F3F9FB",
            outline="")

        self.canvas.create_rectangle(
            292.0,
            542.0,
            1409.0,
            881.0,
            fill="#FFFFFE",
            outline="")

        self.canvas.create_text(
            715.0,
            561.0,
            anchor="nw",
            text="Doanh thu 30 ngày",
            fill="#112E3F",
            font=("Lato Bold", 32 * -1)
        )

        def button_inventory_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")
            app = Invenroty(root)
            root.mainloop()
            
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=button_inventory_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=11.0,
            y=517.0,
            width=200.0,
            height=40.0
        )

        def button_home_clicked():
            self.root.destroy()
            root = tk.Tk()
            root.geometry("+0+0")  # Set window position to (0, 0)
            app = Home(root)
            root.mainloop()
            
        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=button_home_clicked,
            relief="flat"
        )
        self.button_2.place(
            x=11.0,
            y=446.0,
            width=200.0,
            height=40.0
        )
                
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 hit repeat summary page clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=11.0,
            y=589.0,
            width=200.0,
            height=41.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            111.0,
            210.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            341.0,
            303.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            895.0,
            303.0,
            image=self.image_image_3
        )
        
        

# Tạo cửa sổ chính
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("+0+0")  # Set window position to (0, 0)
    app = Home(root)
    root.mainloop()
    


# # Đóng kết nối cơ sở dữ liệu khi thoát ứng dụng
# conn.close()
