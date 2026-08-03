"""print marksheet """

class A:
    def marks(self):
        self.m1 = int(input('enter your marks:'))
        self.m2 = int(input('enter your marks:'))
        self.m3 = int(input('enter your marks:'))
        self.m4 = int(input('enter your marks:'))
        self.m5 = int(input('enter your marks:'))

class B(A):
    def total(self):
        self.t=self.m1+self.m2+self.m3+self.m4+self.m5
        print(self.t)
class C(B):
    def per(self):
        self.per1 = self.t/500*100
        print(self.per1)
class D(C):
    def div(self):
        if self.per1 >=80 and self.per1 <=100:
            print("A")
        elif self.per1 >=60 and self.per1 <80:
            print("B")
        elif self.per1 >=40 and self.per1 <60:
            print("C")
        else:
            print('fail')
obj = D()
obj.marks()
obj.total()
obj.per()
obj.div()

            
        