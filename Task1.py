number = int(input())
digit = int(input())
position = int(input())
actual_digit = digit
i = 0
actual_number = number
total = 0
number_i = 0
while number>0:
    number_j = number % 10
    number = (number-number_j) // 10
    i += 1
number = actual_number
if position == 0:
    number_i = number % 10
    position = position+1
else:
    for j in range(position):
        number_i = number % 10
        number = (number-number_i) // 10

if digit>number_i:
    if position>i:
        total_in_j = number_i*10**(position)
        digit = digit*10**(position)
        total = digit + actual_number
        print(total)
    else:
        total_in_j = number_i*10**(position-1)
        digit = digit*10**(position-1)
        total = actual_number-total_in_j+digit
        print(total)
else:
    print(actual_number)
            
            