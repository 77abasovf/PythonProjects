a = int(input("-> "))
even_sum = 0
odd_sum = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i


print(f"Sum of Even numbers: {even_sum}")
print(f"Sum of Odd numbers: {odd_sum}")
