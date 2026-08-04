"""using class """

class A:
    def prompt(self):
        self.b=int(input('enter your number'))

class B(A):
    def count(self):
        self.c=0
        while self.b!=0:
            self.c +=1
            self.b=int(self.b/10)
        print(self.c)
class C(B):
    def summ(self):
        for i in self.count():
            summ+=1
            print(summ)


obj = C()
obj.prompt()
obj.count()
obj.summ
