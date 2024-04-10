class Medicine:
    def __init__(self, med_id, name, quantity, price):
        self.__med_id = med_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.__quantity = new_quantity
            print(f"Quantity of{self.__name} upadated_Quantity {self.__quantity}")
            print("-------------------------------------------")

        else:
            print("Give correct Quantity......")
            print("-------------------------------------------")

    def calculate_total_value(self):
        return self.__quantity * self.__price


    def display_info(self):
        print(f"Medicine ID: {self.__med_id}")
        print(f"Name: {self.__name}")
        print(f"Quantity: {self.__quantity}")
        print(f"Price: {self.__price}")
        print(f"Total Value: {self.calculate_total_value()}")

med_id = str(input("Enter Medicine med_id : "))
name = str(input("Enter Medicine name : "))
quan =int(input("Enter Medicine quantity : "))
price =int(input("Enter Medicine price : "))
print("===================================================")

Medicine1 = Medicine(med_id, name, quan, price)
Medicine1.display_info()
print("===================================================")

Up_quan =int(input("enter new Quantity : "))
Medicine1.update_quantity(Up_quan)
Medicine1.display_info()