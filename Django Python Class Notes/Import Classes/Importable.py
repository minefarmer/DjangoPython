class Car():
    """ info car """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km_reading = 400
       
        
    def get_des(self):
        """ printing info in the output """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
    
    
    def read_km(self):
        """ print info about km """
        print('this car has ' + str(self.km_reading) + ' km on it.')  # this car has 400 km on it.
        
        
        
    def update_km(self, km):
        """update km """
        if km >= self.km_reading:
            self.km_reading = km
        else:
            print('you can\'t roll back on km')
        
class  ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def des_battery(self):
        """printing info about the battery"""
        print('this car has ' + str(self.battery) + " kwh battery.")
    def fill_gas(self):
        print('this car doesn\'t need gas.')
        
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """printing info about battery"""
        print('this car has a ' + str(self.battery_size) + ' kwh battery.')

my_car = Car('audi', 'a4', 2016)
print(my_car.get_des())  # 2016 Audi A4
