from abc import ABC,abstractmethod
class Calculator(ABC):
    global v1
    v1=10
    _v1=15
    __v3=20
    def __init__(self):
        print('Super Class')
    @abstractmethod
    def summation(self):
        pass
    def subtraction(self,n1,n2):
        return n1-n2
    def multiplication(self,n1,n2):
        return n1*n2
    def get_global_data(self):
        
        print(v1)
    def general():
        print('General Function')
    def change(f):
        global v1
        print(v1)
        v1=f
        print(v1)
    def get_v1():
        print(v1)
