#1
four_digit_number = input("Type four digit number\n")

first_digit = four_digit_number[0]
second_digit = four_digit_number[1]
third_digit = four_digit_number[2]
four_digit = four_digit_number[3]

result = int(first_digit) + int(second_digit) + int(third_digit) + int(four_digit)
print(result)

#2
import random
f = open ("number.txt", "wt")
for i in range (500): 
    num = random.randint(1,500)

    f.write(str(num) + "\n")
f.close() 
