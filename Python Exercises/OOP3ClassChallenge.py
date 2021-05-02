
# parent class
class Vehicle:
    def __init__(self, manufacturer, power_source, vehicle_type):
        self.manufacturer = manufacturer
        self.power_source = power_source
        self.vehicle_type = vehicle_type

    def information(self):
        msg = f"\nManufacturer: {self.manufacturer}" \
              "\nPower Source: {self.power_source}" \
              "\nVehicle Type: {self.vehicle_type}"
        return msg


if __name__ == "__main__":
    car = Vehicle("Toyota","battery","automobile")
    print(car.information())
