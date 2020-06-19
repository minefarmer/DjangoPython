# Not using self for self.model  * 11
# Above corrected  * 31
# Moving on 300 km added  * 51
# Updating km  * 81
# 
# 
# 
# 
# 

# class Car():
#     """ info car """
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_des(self):
#         """ printing info in the output """
#         long_name = str(self.year) + ' ' + self.make + ' ' + model 
#         return long_name.title()

# my_new_car = Car('audi', 'a4', 2016)

# my_new_car.get_des()  # Traceback (most recent call last):
#                         # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Classes Cars.py", line 24, in <module>
#                         #     my_new_car.get_des()
#                         # File "c:/Users/pgold/Github/DjangoPython/Django Python Class Notes/Classes Cars.py", line 19, in get_des 
#                         #     long_name = str(self.year) + ' ' + self.make + ' ' + model
#                         # NameError: name 'model' is not defined

# class Car():
#     """ info car """
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_des(self):
#         """ printing info in the output """
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
#         return long_name.title()

# my_new_car = Car('audi', 'a4', 2016)

# print(my_new_car.get_des())  # 2016 Audi A4






# class Car():
#     """ info car """
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.km_reading = 0
        
#     def get_des(self):
#         """ printing info in the output """
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
#         return long_name.title()
    
    
#     def read_km(self):
#         """ print info about km """
#         print('this car has ' + str(self.km_reading) + ' km on it.')  # this car has 300 km on it.
        
        
        
#     def update_km(self, km):
#         """update km """
#         self.km_reading = km
# my_new_car = Car('audi', 'a4', 2016)

# print(my_new_car.get_des())  # 2016 Audi A4 
# my_new_car.update_km(300)
# print(my_new_car.read_km())  # None


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
        
my_new_car = Car('audi', 'a4', 2016)

print(my_new_car.get_des())  # 2016 Audi A4 
my_new_car.update_km(300)
print(my_new_car.read_km())  # None