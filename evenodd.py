def check_number(number):
    if number % 2 == 0:
        return f"{number} is an even number"
    else:
        return f"{number} is an odd number"
number = int(input("Enter a number: "))
result = check_number(number)
print(result)