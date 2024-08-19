class Product:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


products : list[Product] = []
product1 = Product("Iphone 15 Pro Max" , "1300" , 50)
product2 = Product("Iphone 14 Pro Max" , "1000" , 20)

products.append(product1)
products.append(product2)

for product in products:
    print(f"""
    name : {product.name}
    price : {product.price}
    """)