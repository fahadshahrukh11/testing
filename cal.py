a = float(input("Enter ur 1st num"))
b = input("mathematical operation")
c = float(input("Enter ur 2nd num"))
d = 0

if b == "+":
    d = a + c

elif b == "-":
    d = a - c

elif b == "*":
    d = a * c

elif b == "/":
    d = a / c

else:
    print("error")
print (d)
