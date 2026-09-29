
#abstract method
#1. Need to implement compulsory in subclass
#2. No body only definition


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def stop():
        pass
# v1 = Vehicle()  #Can't instantiate

class Bike(Vehicle):
    def start(self):
        print('Start method....')
    def stop(self):
        print('Stop method...')

b1 = Bike()
b1.stop()
