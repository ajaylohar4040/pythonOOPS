"""class """

class a :
    def p():
        print('hello im perent class')

class b(a):
    def c():
        print('hello im child class')
class c(b):
    def c2():
        print('im child class2')

obj=c
obj.p()
obj.c()
obj.c2()