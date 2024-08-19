class A:
    def __init__(self) -> None:
        self.salom='hi'
        self.salom1 = 'hi 1'
        self.salom2 = 'hi 2'

    @property
    def m(self):
        return 0

a = A()
print(getattr(a, 'm'))