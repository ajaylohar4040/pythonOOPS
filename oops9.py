class A:
    def get_number(self):
        self.num = int(input("Enter number: "))


class B(A):
    def count_digits(self):
        count = 0
        temp = self.num

        while temp != 0:
            count += 1
            temp //= 10

        print("Total digits =", count)


obj = B()
obj.get_number()
obj.count_digits()