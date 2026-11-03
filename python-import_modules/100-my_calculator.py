#!/usr/bin/python3                                                                                                                                  
import sys
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return None
    return a / b
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "\x2a":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, \x2a and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, result))
