import math


def fun(x):
    return pow(10 - x*x*x, 0.5)/2



def fixedpoint():
    p0 = float(input("Enter initial approximation "))
    tol = float(input("Enter tolerance "))
    n0 = float(input("enter maximum number of iterations "))
    itr = 1
    while itr < n0:
        p = fun(p0)
        if math.isnan(p):
            print("The result diverges")
            break

        if abs(p - p0) < tol:
            print("success p= ", p, "after ", itr, "iterations")
            flag=0
            break
        itr=itr+1
        p0=p




def main():
    fixedpoint()


if __name__ == "__main__":
    main()
