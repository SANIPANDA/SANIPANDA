n=input(int("enter the number of terms you want"))
a = 0
b = 1
c= b 
d = 1
while true:
    print(c, end=" ")
    d += 1
    a, b = b, c
    c= a + b
print()
