
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

# child class 1
class Automobile(Vehicle):
    def __init__(self, manufacturer, power_source, vehicle_type, num_wheels):
        # with super(), you don't have to use the name of the parent element or use self like the following:
        # Vehicle.__init__(self, manufacturer, power_source, vehicle_type
        super().__init__(manufacturer, power_source, vehicle_type)
        self.num_wheels = num_wheels
        

# Create method with same name as parent class and override its definition
    def information(self):
        msg = (f'\nManufacturer: {self.manufacturer}\
                 \nPower Source: {self.power_source}\
                 \nVehicle Type: {self.vehicle_type}\
                 \nNumber of Wheels: {self.num_wheels}') # this line is different from parent class
        return(msg)
        
# child class 2
class Airplane(Vehicle):
    def __init__(self, manufacturer, power_source, vehicle_type, num_engines):
        # with super(), you don't have to use the name of the parent element or use self like the following:
        # Vehicle.__init__(self, manufacturer, power_source, vehicle_type
        super().__init__(manufacturer, power_source, vehicle_type)
        self.num_engines = num_engines
        

# Create method with same name as parent class and override its definition
    def information(self):
        msg = (f'\nManufacturer: {self.manufacturer}\
                 \nPower Source: {self.power_source}\
                 \nVehicle Type: {self.vehicle_type}\
                 \nNumber of Engines: {self.num_engines}')  # this line is different from parent class
        return(msg)
        
# Main method here
if __name__ == "__main__":
    car = Automobile("Toyota","battery","automobile",4)
    print(car.information())

    plane = Airplane("Grumann","jet fuel","airplane",2)
    print(plane.information())
