class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def driver(self, distance):
        print("need %d hour(s)" %(distance / self.speed))

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def driver(self, distance):
        Vehicle.driver(self, distance)
        print("need %d fuels" %(distance * self.fuel))


b = Bike(15.0)
c = Car(80.0, 0.012)
b.driver(90.0)
c.driver(100.0)