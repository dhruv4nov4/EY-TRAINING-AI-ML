for i in range(1,6):
    print(i)

print("New Program")

def multiplication_table(num):
    print(f"multiplication of {num}")
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
number = int(input("Enter a number: "))
multiplication_table(number)