#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is 
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = 0

if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = (-number % 10) * -1

message = f"Last digit of {number} is {lastDigit}"

if lastDigit == 0:
    print(f"{message} and is 0")
elif lastDigit > 5 and lastDigit % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
