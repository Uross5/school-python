from Db import Db


class Product(Db):

    allowed_types=("iOS","android")
    number_of_products=0
    number_of_types={
        "android":0,
        "iOS":0
    }


    def __init__(self):

        super().__init__()


    def create(self,name,price,amount,type):
        if amount<1:
            raise ValueError("amount must be greater than 0")
        if type not in Product.allowed_types:
            raise ValueError("Invalid type")
        if self.check_product_exists(name):
            raise ValueError("Product already exists")

        self.name=name
        self.price=price
        self.amount=amount
        self.type=type

        cursor=self.connection.cursor()
        cursor.execute("INSERT INTO products (name,price,amount,type) VALUES (%s, %s, %s, %s)",(
            name,price,amount,type))
        self.connection.commit()
        cursor.close()
        self.increment_number_of_proucts(type,amount)

    def increment_number_of_proucts(self,type,amount):
        Product.number_of_products += 1
        Product.number_of_types[type] += amount

    def check_product_exists(self,name):
        cursor=self.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name=%s",(name,))
        self.connection.commit()
        result=cursor.fetchone()
        cursor.close()
        return result





