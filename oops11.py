"""oops  peramerzind """

class A :
    def __init__(self,name ,id):
        self.name=name
        self.id=id
        print(self.name)
        print(self.id)

    def show(self):
        print(self.name)
        print(self.id)

obj = A('ajay',101)
obj.show()

        