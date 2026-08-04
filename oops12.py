"""non parameterized """

class A:
    def __init__(self):
        self.name = 'ajay'
        self.id = 101
    def base1(self):
        print(self.id)
        print(self.name)

obj = A()
obj.base1()
