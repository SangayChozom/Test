num = int(input("Enter the number for which you want the multioplication table: "))
limit = int(input("Enter the limit upto which you want the multiplication table to be generated: "))

i = 1
print(f"Multiplication table for {num} up to {limit}:")
for i in range(1, limit+1):
    print(f"{num} x {i} = {num * i}")
