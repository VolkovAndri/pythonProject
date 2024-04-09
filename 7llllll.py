class ClassA:
    def __init__(self):
        self.a = 0

    def method_a(self):
        print("Method A from ClassA")


class ClassB:
    def __init__(self):
        self.b = 1

    def method_b(self):
        print("Method B from ClassB")


class ComplexClass(ClassA, ClassB):
    def __init__(self):
        ClassA.__init__(self)
        ClassB.__init__(self)

    def method_c(self):
        print("Method C from ComplexClass")


obj = ComplexClass()
print(obj.a)
print(obj.b)
obj.method_a()
obj.method_b()
obj.method_c()