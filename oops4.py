"""class """

class a :
    def p():
        print('hello im perent class')

class b(a):
    def c():
        print('hello im child class')

obj=b
obj.p()
obj.c()