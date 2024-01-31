def approximation_method():
    x0 = float(input('Enter a number: '))
    tol = float(input("Enter a tolerance: "))
    iter = 0
    diff = x0
    x = x0
    print(iter, " : ", x0)
    while diff >= tol:
        iter = iter + 1
        y = x
        x = (x / 2) + (1 / x)
        print(iter, " : ", x)
        diff = abs(x - y)
    print("Convergence after", iter, " iterations")


def main():
    approximation_method()


if __name__ == "__main__":
    main()
