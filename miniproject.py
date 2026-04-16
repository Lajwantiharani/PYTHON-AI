first  = input("1st num")
op = input("op (+,-,*,/,%)")
second = input ("2nd num")

first = int(first)
second = int(second)

if op == "+":
    print(first + second)
elif op == "-":
    print(first - second)    
elif op == "*":
    print(first * second)
elif op == "/":
    print(first / second)
elif op == "%":
    print(first % second)
else:
    print("invalid op")