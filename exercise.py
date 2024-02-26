age = int(input("Enter your age: "))
status = input("Are you a student?(yes/no): ")

if age <= 12:
    print("You are eligible for a discount on the movie ticket")
elif 13 <= age <= 18 and status == "yes":
    print("You are eligible for a discount on the movie ticket")
else:
    print("You are not eligable for discount")
