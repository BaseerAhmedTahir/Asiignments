name = input("Enter your name: ")

num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))

numbers = [num1, num2, num3]

even_odds = []

for num in numbers:
    if num % 2 == 0:
        even_odds.append((num, "even"))
    else:
        even_odds.append((num, "odd"))

print(f"\nHello, {name}! Let's explore your favorite numbers:")

for num, even_odd in even_odds:
    print(f"The number {num} is {even_odd}.")

for num in numbers:
    square = num ** 2
    print(f"The number {num} and its square: ({num}, {square})")

total_sum = num1 + num2 + num3

print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

if total_sum <= 1:
    is_prime = False
elif total_sum <= 3:
    is_prime = True
elif total_sum % 2 == 0 or total_sum % 3 == 0:
    is_prime = False
else:
    is_prime = True
    i = 5
    while i * i <= total_sum:
        if total_sum % i == 0 or total_sum % (i + 2) == 0:
            is_prime = False
            break
        i += 6

if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")
