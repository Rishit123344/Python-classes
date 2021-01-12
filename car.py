class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedlimit = speedlimit
    def start(self):
        print('started')   
    def stop(self):
        print('stop')
    def accelerating(self):
        print('accelerating')    
car = Car("A6","Blue","Honda",200) 
print(car.start())
print(car.speedlimit)       
         