PRICE_INDEX = 0
QUANTITY_INDEX = 1

message_not_enough_fuel = "Not enough fuel!"
message_price_must_be_number = "Price must be a positive number!"
message_quantity_must_be_number = "Quantity must be a positive number!"
message_invalid_fuel_type = "Fuel not supported by this pump. We only support STANDARD, PREMIUM, DIESEL and ALCOHOL"

# Initial prices are invalid and the is 0 quantity of every fuel!
fuel_types = {
    "STANDARD": [-1, 0],
    "PREMIUM": [-1, 0],
    "DIESEL": [-1, 0],
    "ALCOHOL": [-1, 0]
}


class FuelPump:
    def __init__(self):
        self.fuel_types = fuel_types
        self.current_fuel_type = "STANDARD"

    def __str__(self):
        if self.fuel_types.get(self.current_fuel_type)[PRICE_INDEX] > -1:
            price_message = self.fuel_types.get(self.current_fuel_type)[PRICE_INDEX]
        else:
            price_message = "Not set yet."
        return f"Current fuel Type: {self.current_fuel_type}\n" \
               f"Fuel Price: {price_message}\n" \
               f"Fuel Quantity: {self.fuel_types.get(self.current_fuel_type)[QUANTITY_INDEX]}\n" + \
               self.describe_other_fuel_types()

    def get_price(self):
        return self.fuel_types.get(self.current_fuel_type)[PRICE_INDEX]

    def set_price(self, fuel_type, new_price):
        if self.is_fuel_type_valid(fuel_type):
            for key in self.fuel_types.keys():
                if key == fuel_type:
                    try:
                        new_price = float(new_price)
                        if new_price >= 0:
                            self.fuel_types[key][PRICE_INDEX] = new_price
                        else:
                            print(message_price_must_be_number)
                    except ValueError:
                        print(message_price_must_be_number)
        else:
            print(message_invalid_fuel_type)

    def get_quantity(self):
        return self.fuel_types.get(self.current_fuel_type)[QUANTITY_INDEX]

    def set_quantity(self, fuel_type, quantity):
        if self.is_fuel_type_valid(fuel_type):
            for key in self.fuel_types.keys():
                if key == fuel_type:
                    try:
                        quantity = float(quantity)
                        if quantity >= 0:
                            self.fuel_types[key][QUANTITY_INDEX] = quantity
                        else:
                            print(message_quantity_must_be_number)
                    except ValueError:
                        print(message_quantity_must_be_number)
        else:
            print(message_invalid_fuel_type)

    def get_fuel_type(self):
        return self.current_fuel_type

    def set_fuel_type(self, fuel_type):
        if self.is_fuel_type_valid(fuel_type):
            self.current_fuel_type = fuel_type
        else:
            print(message_invalid_fuel_type)

    def is_fuel_type_valid(self, some_fuel_type):
        return some_fuel_type in self.fuel_types.keys()

    def is_fuel_enough(self, amount_of_fuel):
        return amount_of_fuel < self.get_quantity()

    def describe_other_fuel_types(self):
        fuel_types_string = "The other fuels in this pump are as follows:\n"
        for key in self.fuel_types.keys():
            if key != self.current_fuel_type:
                fuel_price = self.fuel_types.get(key)[PRICE_INDEX]
                if fuel_price > 0:
                    fuel_types_string += f"{key}' price is: ${fuel_price} and there are " \
                                         f"{self.fuel_types.get(key)[QUANTITY_INDEX]} liters of it in this pump.\n"
                else:
                    fuel_types_string += f"{key}'S price has not been set yet and there are " \
                                         f"{self.fuel_types.get(key)[QUANTITY_INDEX]} liters of it in this pump.\n"

        return fuel_types_string

    def fill_with_price(self, payment):
        price = self.get_price()
        if price == -1:
            print(f"{self.current_fuel_type}'S price has not been set yet")
            return 0

        amount_of_fuel = payment / price

        if self.is_fuel_enough(amount_of_fuel):
            self.fuel_types.get(self.current_fuel_type)[QUANTITY_INDEX] = self.get_quantity() - amount_of_fuel
            return amount_of_fuel
        else:
            print(message_not_enough_fuel)
            return 0

    def fill_with_liters(self, liters):
        if self.is_fuel_enough(liters):
            self.fuel_types.get(self.current_fuel_type)[QUANTITY_INDEX] = self.get_quantity() - liters
            return liters * self.get_price()
        else:
            print(message_not_enough_fuel)
            return 0


