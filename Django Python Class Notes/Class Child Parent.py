# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
class Test():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        full_name = self.name + ' ' + str(self.age)
        print(full_name.title())
    
    
class Test2(Test):
    def __init__(self, name, age):
        super().__init__(name, age)



m = Test('ali', 33)
m.print_info()  # Ali 33

t2 = Test2('carl', 81)
t2.print_info()  # carl 81