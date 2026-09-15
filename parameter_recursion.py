def generate(x, n):
    if n == 0:
        return
    generate(x, n - 1)
    print(x)


# generate(15, 4)

"""printing N to 1 using head recursion"""


def generate_series_head(x: int, N: int) -> int:
    if x > N:
        return
    generate_series_head(x + 1, N)
    print(x)


# generate_series_head(1, 5)

"""printing 1-N using head recursion"""


def generate_series(N: int) -> int:
    if N == 0:
        return
    generate_series(N - 1)
    print(N)


"""printing 1 to N using tail recursion"""


def generate_series_tail_to_N(x: int, N: int) -> int:
    if x > N:
        return
    print(x)
    generate_series_tail_to_N(x + 1, N)


"""printing N to 1 using tail recursion"""


def generate_series_tail_to_one(N: int) -> int:
    if N == 0:
        return
    print(N)
    generate_series_tail_to_one(N - 1)


while True:
    print("3 for exit")
    print("Choose 1 for Head Recursion")
    print("Choose 2 for tail Recursion")
    choice = int(input("Enter your number"))

    if choice == 1:
        print("Choose 1 to print 1 to N")
        print("Choose 2 to print N to 1")
        second_choice = int(input("Enter your choice"))

        if second_choice == 1:
            N = int(input("Enter the value of N"))
            generate_series(N)
        if second_choice == 2:
            x = int(input("Enter the value of x"))
            N = int(input("Enter the value of N"))
            generate_series_head(x=x, N=N)
    if choice == 2:
        print("Choose 1 to print 1 to N")
        print("Choose 2 to print N to 1")
        second_choice = int(input("Enter your choice"))

        if second_choice == 1:
            x = int(input("Enter the value of x"))
            N = int(input("Enter the value of N"))
            generate_series_tail_to_N(x=x, N=N)
        if second_choice == 2:
            N = int(input("Enter the value of N"))
            generate_series_tail_to_one(N=N)
    if choice == 3:
        break
