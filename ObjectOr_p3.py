class A:
    def __init__(self):
        self.name = "ich bin öffentlich"
        self._name = "ich bin protected"
        self.__name = "ich bin private"

z = A()

print(z.name)

#print(z.__name)
print(z._A__name)

#print(z.__name)

class B(A):
    def __init__(self):
        super().__init__()

class C(A):
    def __init__(self):
        super().__init__()

t=B()
print(t._name)

t=C()
print(t._name)
print(t._A__name)
