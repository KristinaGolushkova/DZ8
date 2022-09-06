class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiplication(self, a=0, b=0):
        return self.a * self.b

    def addition(self, a=0, b=0):
        return self.a + self.b

    def division(self, a=0, b=0):
        return self.a / self.b

    def subtraction(self, a=0, b=0):
        return self.a - self.b


v = Math(22, 15)

print(v.addition())
print(v.multiplication())
print(v.division())
print(v.subtraction())
