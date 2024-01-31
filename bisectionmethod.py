def fun(x):
    return pow(x, 3) + 4 * pow(x, 2) - 10


def bisectionmethod():
    x = float(input("input lower end value "))
    y = float(input("higher end value "))
    itr = 0
    tol = float(input("enter tolerance "))
    max = float(input("enter max value "))

    while abs(y - x) > tol and itr < max:
        itr = itr + 1
        p = (x + y) / 2
        if (fun(x) < 0 < fun(p)) or (fun(x) > 0 > fun(p)):
            y = p
        else:
            x = p

    print("Converged to ", p, "in ", itr, " iterations")


def main():
    bisectionmethod()


if __name__ == "__main__":
    main()
