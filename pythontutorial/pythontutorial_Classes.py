# define the Vehicle class
class Vehicle:

    def __init__(self, name, color, kind, value):
        self.name = name
        self.color = color
        self.kind = kind
        self.value = value

    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle(name='Fer', kind='convertible', color='red', value=60000.00)
car2 = Vehicle(name='Jump', kind='van', color='blue', value=10000.00)


# test code
print(car1.description())
print(car2.description())

#what is should be
# define the Vehicle class
#class Vehicle:
 #   name = ""
  #  kind = "car"
   # color = ""
   # value = 100.00
#    def description(self):
#        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#        return desc_str
#
# your code goes here
#car1 = Vehicle()
#car1.name = "Fer"
#car1.color = "red"
#car1.kind = "convertible"
#car1.value = 60000.00
#
#car2 = Vehicle()
#car2.name = "Jump"
#car2.color = "blue"
#car2.kind = "van"
#car2.value = 10000.00
#
# test code
#print(car1.description())
#print(car2.description())