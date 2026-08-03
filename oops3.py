"""class again """

class Home:
    def __init__(self,fullname,roll_no):
        self.name=fullname
        self.roll=roll_no
        print('tv is on ......use it',)

s1 = Home('ajay',101)
print(s1.name)
print(s1.roll)

s2  = Home('akash',102)
print(s2.name)
print(s2.roll)

print(s1.roll)