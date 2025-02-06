import sqlite3

def connect_db():
    # Tạo kết nối tới cơ sở dữ liệu
    conn = sqlite3.connect('grocery_store_database.db')
    cusor = conn.cursor()

    # Tạo bảng sản phẩm
    cusor.execute('''CREATE TABLE IF NOT EXISTS products (
                products_barcode TEXT PRIMARY KEY,
                products_name TEXT,
                products_amount INTEGER,
                products_expiry DATE,
                products_price REAL)''')

    # Tạo bảng hóa đơn
    cusor.execute('''CREATE TABLE IF NOT EXISTS recipts (
                recipts_id INTEGER PRIMARY KEY,
                recipts_invoice_print_day DATE,
                recipts_total_price REAL)''')

    # Tạo bảng chi tiết hóa đơn
    cusor.execute('''CREATE TABLE IF NOT EXISTS recipts_detail (
                recipts_id INTEGER,
                recipts_invoice_print_day DATE,
                products_barcode TEXT,
                products_name TEXT,
                products_amount INTEGER,
                products_price REAL,
                FOREIGN KEY (recipts_id) REFERENCES recipts (recipts_id),
                FOREIGN KEY (products_barcode) REFERENCES products (products_barcode))''')

    conn.commit()
    return conn

def add_product_2db(product):
    # Câu lệnh SQL để chèn dữ liệu
    sql = '''
            INSERT INTO products (products_barcode, products_name, products_amount, products_expiry, products_price) 
            VALUES (?, ?, ?, ?, ?)
            '''
            
    # Dữ liệu cần chèn vào bảng
    data = (product.barcode, product.name, product.amount, product.expire, product.price)
    
    # Thực thi câu lệnh chèn dữ liệu
    conn = connect_db()
    cusor = conn.cursor()
    cusor.execute(sql, data)

    # Xác nhận thay đổi trong cơ sở dữ liệu
    conn.commit()

    # Đóng kết nối
    conn.close()
    return 0


def tinh_tien():
    # Logic xử lý tính tiền và cập nhật cơ sở dữ liệu
    pass

def tong_ket_ngay():
    # Logic xử lý tổng kết ngày
    pass

def xem_kho():
    # Logic hiển thị danh sách sản phẩm trong kho
    pass

def nhap_kho():
    # Logic nhập hàng vào kho
    pass