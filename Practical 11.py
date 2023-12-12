t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

half_length = len(t1) // 2
first_half = t1[:half_length]
second_half = t1[half_length:]

print(*first_half) 
print(*second_half)  

even_numbers = ()
for num in t1:
    if num % 2 == 0:
        even_numbers += (num,)

print(even_numbers)

t2 = (11, 13, 15)
t3 = t1+t2
print(t3)

print(max(t3))
print(min(t3))