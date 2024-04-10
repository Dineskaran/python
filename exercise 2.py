class PizzaOrder:
    def __init__(self):
        self.size = None
        self.quantity = None


    def get_size_and_quantity(self):
        while True:
            self.size = input("Enter size (small, medium, large): ")
            self.quantity = input("enter the Quantity")

    try:
        if self.size not in ('self','medium', 'large'):
            raise ValueError("Invalid Size")
        self.quantity = int(self.quantity)
        if self.quantity <=0:
            raise ValueError("Quantity must be only positive")

    except ValueError as e:
        print(e)

    def calculate_total_price(self, sales_tax=None):
        price = {'small': 100, 'medium': 200, 'large': 300}
        subtotal = price.get(self.size) * self.quantity
        seles_tex = 0.18 * subtotal
        total_price = subtotal + sales_tax
order = PizzaOrder()
order.get_size_and_quantity()
total_price = order.calculate_total_price
print("total_price : ", total_price)



