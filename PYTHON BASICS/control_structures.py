def classify_number(num):
    return "Even" if num % 2 == 0 else "Odd"

user_input = int(input("Enter an integer: "))
print(f"The number {user_input} is {classify_number(user_input)}.")

even_numbers = [n for n in range(1, 51) if n % 2 == 0]
print("Even numbers from 1 to 50:", even_numbers)

count = 10
while count > 0:
    print(count)
    count -= 1
