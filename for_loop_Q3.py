def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)  
    sum_of_powers = 0
    
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    return sum_of_powers == number

num = int(input("Enter a number to check if it's an Armstrong number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
