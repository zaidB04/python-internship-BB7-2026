class Bird:
    def fly(self):
        print("Bird flies using wings.")


class Airplane:
    def fly(self):
        print("Airplane flies using engines.")


class Drone:
    def fly(self):
        print("Drone flies using propellers.")


def make_fly(obj):
    obj.fly()


b = Bird()
a = Airplane()
d = Drone()

make_fly(b)
make_fly(a)
make_fly(d)