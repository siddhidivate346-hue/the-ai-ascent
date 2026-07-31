class UPI:
    def pay(self):
        print("Payment done using UPI")

class CARD:
    def pay(self):
        print("payment done using card")

class NETBANKING:
    def pay(self):
        print("payment done using net banking")

print("choose payment menthod")
print("1.UPI")
print("2.CARD")
print("3.NET BANKING")

choice = int(input("enter your choice: "))
if choice == 1:
    p = UPI()

elif choice == 2:
    p = CARD()

elif choice == 3:
    p = NETBANKING()

else:
    print("INVALID CHOICE")
    exit()
p.pay()


