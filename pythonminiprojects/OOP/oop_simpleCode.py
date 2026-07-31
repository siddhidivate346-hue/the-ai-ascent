class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


c1 = Car("BMW", 900000)
c2 = Car("Tesla", 1200000)

print("Car 1 Details:")
c1.show_details()

print("\nCar 2 Details:")
c2.show_details()