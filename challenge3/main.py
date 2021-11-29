from fuel_pump import FuelPump, fuel_types, QUANTITY_INDEX

if __name__ == '__main__':
    # FuelPump example.
    some_fuel_pump = FuelPump()
    print(some_fuel_pump)

    # Operations with STANDARD fuel type
    # Testing the validations
    some_fuel_pump.fill_with_price(100)
    some_fuel_pump.fill_with_liters(500)
    some_fuel_pump.set_price("STANDARD", -20)
    some_fuel_pump.set_quantity("STANDARD", -5)
    some_fuel_pump.set_price("SOME INVALID FUEL TYPE", 20)
    some_fuel_pump.set_quantity("SOME INVALID FUEL TYPE", 20)

    # Initiating the values for quantity and price of STANDARD fuel
    some_fuel_pump.set_quantity("STANDARD", 15)
    some_fuel_pump.set_price("STANDARD", 100)
    print(some_fuel_pump)

    # Filling the tank with the current fuel type in the fuel pump (STANDARD)
    # The operations below will fail due to the fuel pump not having enough fuel
    some_fuel_pump.fill_with_price(99999999)
    some_fuel_pump.fill_with_liters(15000)

    # The following operations will work as expected
    some_fuel_pump.fill_with_price(150)
    print(some_fuel_pump)
    some_fuel_pump.fill_with_liters(13)
    print(some_fuel_pump)

    # Operations with PREMIUM fuel type to demonstrate how to change fuel type.
    some_fuel_pump.set_quantity("PREMIUM", 5)
    some_fuel_pump.set_price("PREMIUM", 500)
    print(some_fuel_pump)
    some_fuel_pump.set_fuel_type("SOME INVALID FUEL")
    some_fuel_pump.set_fuel_type("PREMIUM")
    print(some_fuel_pump)

    # The current fuel type now is PREMIUM, so all the "fill" operations are using PREMIUM fuel
    some_fuel_pump.fill_with_liters(3)
    print(some_fuel_pump)
    some_fuel_pump.fill_with_price(250)
    print(some_fuel_pump)

