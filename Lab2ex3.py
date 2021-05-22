a = input("Input value A: ")
b = input("Input value B: ")
c = input("Input value C: ")

print(a)
print(b)
print(c)

if a > b and a > c:
    print("The greatest value is A: ",a)

if b > a and b > c:
    print("The greatest value is B: ",b)

if c > a and c > b:
    print("The greatest value is C: ",c)

if a < b and a < c:
    print("The smallest value is A: ",a)

if b < a and b < c:
    print("The smallest value is B: ",b)

if c < a and c < b:
    print("The smallest value is C: ",c)
