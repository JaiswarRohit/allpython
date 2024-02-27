def a():
    print("result 1 is ", __name__)


def s():
    print("result 2 is ", __name__)

def main():
    a()
    s()

if __name__ == "__main__":
    main()

