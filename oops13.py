import json
try:
    with open("bank1.json", "r") as file:
        bank  = json.load(file)
except:
    bank = {}

def write():
    print(' successfully')
    with open("bank1.json", "w") as file:
        json.dump(bank, file, indent=4)

"""atm system"""
print('1. bank account')
print('2.ATM')
choose = int(input('enter your choice: '))
if choose == 2 :
    class A:
        def __init__(self):
            self.pin = 123
            self.amount = 1000

    class B(A):
        def input2(self):
            print()
            while True:
                input3 = int(input('enter your pin: '))
                if self.pin == input3:
                    print('pin correct')
                    break
                else:
                    print('invalid pin, try again')

    class C(B):
        def work(self):
            print('1. chack balance ')
            print('2. deposite')
            print('3. withdorw')
        
            self.choose = int(input('enter your choise : '))
            if self.choose == 1:
                print(f'your balanace is {self.amount}')
            elif self.choose == 2:
                self.amount1 = int(input('enter your amount: '))
                self.total=self.amount+self.amount1
                print(self.total)
            elif self.choose==3:
                self.amount1 = int(input('enter your amount:'))
                self.total = self.amount1-self.amount
               
    obj = C()

    obj.input2()
    obj.work()

    """bank system"""
elif choose == 1:
    print('====Welcome====')
    class bank_account:
        def __init__(self):
            
            while True:
                print('1 open bank account:')
                print('2 show account details:')

                self.choose =int(input('enter your choice: '))
                if choose==1:
                    self.account_name=input('enter your Full_Name : ')
                    self.account_age=int(input('enter your Age : '))
                    self.account_no=input('enter your Mobile_Number : ')
                    self.account_bal =int(input('please deposit money fisrt: '))
                    self.account_pin = int(input('please set your account pin '))
                    if self.account_age >= 18:
                        bank[self.account_pin] = {
                            "name": self.account_name,
                            "age": self.account_age,
                            "bal": self.account_bal,
                            "num" :self.account_no
                            }
                        write()
                    else:
                        print('sorry sir you are teenegar!') 

                elif choose == 2:
                    self.id = int(input('enter your pin '))
                    print(bank[self.id]["bal"])

    obj1 = bank_account()                 

