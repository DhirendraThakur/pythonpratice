class vehicle:
    def wheels():
        print ('I have 4 wheels')
        
    def sunroof(self):
        print("I have sun roof") 
        
    def seats():
        print("I am 5 seater vehicals")
        
class car(vehicle):
    
    print("print my id")
    
class bike(vehicle):
    def wheels():
        print ("I have ony 2 wheels")
    
def common_fun(self):
    car.sunroof(self)
    bike.wheels()
    
    
    cars = car()
    vikes = bike()
    
common_fun(car)
common_fun(bike)
