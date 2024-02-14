'''def sum(a, b):
    c = a + b  # a and b is formal argument
    print(c)


x = 10
y = 20
sum(x, y)  # x and y are actual arguments


def sub(p, q):
    print(p - q)


sub(50, 5)

def cart(item: object, price: object) -> object:
    print(f'{item}, "cost is :",{price}')


cart(item="bangles", price=22000)
cart(item="handbag", price=1000000)
cart(price=12000, item="shirt")

def test(a: object, b: object) -> object:
    print(f'{a}, "cost is : , {b}')


test(a="rohit", b=1000)
test(a="suman", b=1000)


def detail(Id: object, name: object) -> object:
    print(f'Emp id is: ", {Id}')
    print(f'Emp name is: , {name}')


detail(Id=1, name="rohit")
detail(Id=2, name="Suman")

def date(first, second):
    print(f'Emp id is: ",{first}')
    print(f'Emp name is: ", {second}')

date(1, second=" rohit jaiswar ")


def roh(item: object, price=20) -> object:
    print(f'{item}, "cost is : ", {price}')
    return 0


roh(item="pen")
roh(item="handbag", price=10000)
roh(price=500, item="shirt")


def total(x, *y):
    sum = 0
    for i in y:
        sum+=i
    print(x+sum)

total(15, 84, 85)
total(15, 80, 5, 15)
total(25, 84)


def m1(**q: object) -> object:
    print(q)

m1(id=1, name="rohit", qualification="B.E")
m1(id=8, name="rohit", qualification="B.E")

def quest(**x):
    for k, v, in x.items():
        print(k, "=", v)

quest(a=10, b=12, c=14)
quest(id=10000, name="Rohit")'''



