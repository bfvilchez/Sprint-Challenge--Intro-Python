# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels

    def drive(self):
        return "vroooom"

    def police(self):
        return """ Woop-woop! That's the sound of da police 
                   Woop-woop! That's the sound of da beast
                   Woop-woop! That's the sound of da police
                   Woop-woop! That's the sound of da beast (Yes indeed)
                   Woop-woop! That's the sound of da police
                   Woop-woop! That's the sound of da beast
                   Woop-woop! That's the sound of da police
                   Woop-woop! That's the sound of da beast (Yes indeed) """     



# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, wheels = 2):
        super().__init__(wheels)
    
    def drive(self):
        return "BRAAAP!!"

    def randomStatement(self):
        return "Motorcycles are too dangerous, nobody wants to be a pancake"

    def police(self): 
        return """Just a cast away, an island lost at sea, oh
                  Another lonely day, no one here but me, oh
                  More loneliness than any man could bear
                  Rescue me before I fall into despair, oh
                  I'll send an SOS to the world
                  I'll send an SOS to the world
                  I hope that someone gets my
                  I hope that someone gets my
                  I hope that someone gets my message in a bottle, yeah
                  Message in a bottle yeah """
vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
for vehicle in vehicles: 
    print(vehicle.drive())
    print(vehicle.num_wheels)
    print(vehicle.police())