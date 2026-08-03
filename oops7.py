"""solve q"""

class A:
    def input1 (self):
        self.A1 = int(input('enter your 1st number:'))
        self.B1 = int(input('enter your 2nd number:'))

class B(A):
    def ac(self):
        self.c=self.A1+self.B1
        print(self.c)

obj = B()
obj.input1()
obj.ac()

    

