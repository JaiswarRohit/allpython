class R1:
    def s1(self):
        self.a=11
        self.b=12
        self.c=13
        for i in range(self.a, self.c):
            print(self.a, self.b, self.c)

s = R1()
s.s1()
