class test:
    def __init__(self):
        self.name = "Rohit"
        self.age = 22

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


t1 = test()
t1.age = 30
t2 = test()

if t1.compare(t2):
    print("They are same")
else:
    print("they are different age")