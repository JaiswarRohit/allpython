class Computer:
    def __init__(self, cpu, ram):  # Special Method
        self.cpu = cpu
        self.ram = ram

    def config(self):   # Method Creating
        print("Config is", self.cpu, self.ram)

a = Computer('i5', 16)     # Object Creating
b = Computer('Ryzen 3', 8)

a.config()
b.config()

