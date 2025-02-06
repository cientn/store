class Product:
    """
    A class to represent a product in a grocery store.
    Attributes
    ----------
    barcode : str
        The barcode of the product.
    name : str
        The name of the product.
    amount : int
        The amount of the product in stock.
    expire : str
        The expiration date of the product.
    price : float
        The price of the product.
    Methods
    -------
    get_product():
        Returns the details of the product.
    set_product(barcode, name, amount, expire, price):
        Sets the details of the product.
    __str__():
        Returns a string representation of the product.
    """
    
    def __init__(self, barcode, name, amount, expire, price):
        self.barcode = barcode
        self.name = name
        self.amount = amount
        self.expire = expire
        self.price = price
    # create a method to get and set the product details
    def get_product(self):
        return self.barcode, self.name, self.amount, self.expire, self.price
    def set_product(self, barcode, name, amount, expire, price):
        self.barcode = barcode
        self.name = name
        self.amount = amount
        self.expire = expire
        self.price = price
    def __str__(self):
        return ('{},{},{},{},{}'.format(self.barcode, self.name, self.amount, self.expire, self.price))

class Recipt:
    """
    A class to represent a receipt.

    Attributes
    ----------
    id : int
        Unique identifier for the receipt.
    date : str
        Date of the receipt.
    total : float
        Total amount of the receipt.

    Methods
    -------
    get_recipt():
        Returns the receipt details as a tuple (id, date, total).
    set_recipt(id, date, total):
        Sets the receipt details with the given id, date, and total.
    __str__():
        Returns a string representation of the receipt.
    """
    ''''''
    def __init__(self, id, date, total):
        self.id = id
        self.date = date
        self.total = total
    # create a method to get and set the recipt details
    def get_recipt(self):
        return self.id, self.date, self.total
    def set_recipt(self, id, date, total):
        self.barcode = id
        self.name = date
        self.amount = total
    def __str__(self):
        return ('{},{},{},{}'.format(self.barcode, self.name, self.amount, self.price))
    
class Details:
    """
    A class to represent the details of a product in a receipt.

    Attributes
    ----------
    recipt_id : int
        The id of the receipt.
    product_barcode : str
        The barcode of the product.
    product_amount : int
        The amount of the product in the receipt.
    product_price : float
        The price of the product.

    Methods
    -------
    get_details():
        Returns the details of the product in the receipt.
    set_details(recipt_id, product_barcode, product_amount, product_price):
        Sets the details of the product in the receipt.
    __str__():
        Returns a string representation of the product in the receipt.
    """
    def __init__(self, recipt_id, recipt_date, product_barcode, product_amount, product_price):
        self.recipt_id = recipt_id
        self.recipt_date = recipt_date
        self.product_barcode = product_barcode
        self.product_amount = product_amount
        self.product_price = product_price
    # create a method to get and set the details of the product in the recipt
    def get_details(self):
        return self.recipt_id, self.recipt_date, self.product_barcode, self.product_amount, self.product_price
    def set_details(self, recipt_id, recipt_date, product_barcode, product_amount, product_price):
        self.recipt_id = recipt_id
        self.recipt_date = recipt_date
        self.product_barcode = product_barcode
        self.product_amount = product_amount
        self.product_price = product_price
    def __str__(self):
        return ('{},{},{},{},{}'.format(self.recipt_id, self.recipt_date, self.product_barcode, self.product_amount, self.product_price))