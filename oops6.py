""""haricical"""

class A:
    def p():
        print('im perent class')

class B(A):
    def c1():
        print('im child class')
class C(A):
    def c2():
        print('im child 2 class')

obj1 = B
obj1.p()
obj1.c1()

obj2 = C
obj2.p()
obj2.c2()
