
# parent class
class Vehicle:
    def __init__(self, manufacturer, power_source, vehicle_type):
        self.manufacturer = manufacturer
        self.power_source = power_source
        self.vehicle_type = vehicle_type

    def information(self):
        # each set of quotes needs a separate f string (if I begin/end quotes on eachc line)
        # or just one set and use the '\' as a continuation for the next line

        #msg = (f'\nManufacturer: {self.manufacturer}'
        #       f'\nPower Source: {self.power_source}'
        #       f'  \nVehicle Type: {self.vehicle_type}')

        msg = (f'\nManufacturer: {self.manufacturer}\
                 \nPower Source: {self.power_source}\
                 \nVehicle Type: {self.vehicle_type}')
        return(msg)

# child class
class Automobile(Vehicle):
    def __init__(self, manufacturer, power_source, vehicle_type, num_wheels):
        # with super(), you don't have to use the name of the parent element or use self like the following:
        # Vehicle.__init__(self, manufacturer, power_source, vehicle_type
        super().__init__(manufacturer, power_source, vehicle_type)
        self.num_wheels = num_wheels

# Create method to use the method from the parent method to gather the general info,
# then append num_wheels to msg
    def details(self):
        msg = (f'{self.information()} \nNumber Wheels: {self.num_wheels}')
        return(msg)
        
if __name__ == "__main__":
    car = Automobile("Toyota","battery","automobile",4)
    #print(car.details()) #+ f'\nNumber of Wheels: {car.num_wheels}') # method inherited from parent class
    print(car.information())
