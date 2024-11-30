a, b = 0, 1
print("Fibonacci series between 0 and 50:")

for _ in range(50):
    if a > 50:  
        break
    print(a, end=" ")  
    a, b = b, a + b  