from calculator import Calculator

class Advanced_Calculator(Calculator):
    def __init__(self):
        super().__init__()
        print('Subclass==================')
        
    def powr(self, n1,power):
        return n1**power
    def summation(self, n1,n2,n3):
        return n1+n2+n3