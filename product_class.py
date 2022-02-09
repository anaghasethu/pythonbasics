class Product:
    def __init__(self,brand,price,stocksLeft):
        self.brand = brand
        self.price = price
        self.stocksLeft = stocksLeft

    def stocksDetails(self):
        print(f"Brand Name : {self.brand} Price : {self.price}  Stocks left in store: {self.stocksLeft}" )

redmi = Product("Redmi",15000,45)
realme= Product("Realme", 13000, 17)
vivo= Product("Vivo", 13999, 11)
iphone= Product("Iphone ", 40000, 9)

brands = input("Enter brand from the list redmi, realme, vivo, iphone- ")
print(brands)
if brands == "redmi":    
    redmi.stocksDetails()
elif brands == "realme":
    realme.stocksDetails()
elif brands == "vivo":
    vivo.stocksDetails()
elif brands == "iphone":
    iphone.stocksDetails()
else:
    print(f"{brands} not found")