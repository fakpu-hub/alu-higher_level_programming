#!/usr/bin/python3
import sys
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div

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
    
