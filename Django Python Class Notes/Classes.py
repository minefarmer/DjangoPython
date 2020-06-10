# step 1 11
# step 2 31
# 
# 
# 
# 
# 
# 
# 

# class Test():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(self.name.title() + ' is now sitting')  # line 24 ** Carl is now sitting
        
#     def sit2(self):
#         print(self.name.title(), str(self.age))  # line 25 ** Carl 81



# m = Test('carl', 81)
# m.sit()
# m.sit2()





class Test(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + ' is now sitting')  # line 45 ** Ali is now sitting
        
    def sit2(self):
        print(self.name.title(), str(self.age))  # line 46 ** Carl is now sitting


person1 = Test('ali', 33)
person2 = Test('carl', 81)

person1.sit()
person2.sit()