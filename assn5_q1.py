def zerodivision(a,b):
    try:
        c=(a/b)
    except ZeroDivisionError:
        print("error found")
        print("the denominator is 0")
    else:
        print("the result is: ",a/b)
    finally:
        print("executing 'finally' ")

        print("Execution done")
zerodivision(4,0)