a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
v=input("What operation?(type: add/sub/mul/divq/divw/exp)")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divw(a,b):
    return a/b
def exp(a,b):
    return a**b

if v == "add":
    print("Result: ", add(a,b))
elif v == "sub":
    print("Result: ", sub(a,b))
elif v == "mul":
    print("Result: ", mul(a,b))
elif v == "divq":
    print("Result: ", divq(a,b))
elif v == "divw":
    print("Result: ", divw(a,b))
elif v == "exp":
    print("Result: ", exp(a,b))
else:
    print("nigga do as i say")
