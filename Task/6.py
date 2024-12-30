a= int(input("Enter a number: "))
print(f"Multiplication table for {a}:")
for i in range(1, 11):
    print(f"{a} x {i} = {a * i}")