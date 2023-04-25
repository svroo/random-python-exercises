# Excersice from codewars

# Welcome. In this kata, you are asked to squeare every digit of a number
# and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, 
# because 9^2 is 81 and 1^2 is 1 (81-1-1-81)

# Autor: Rodrigo Salazar

def square_digit(num = int()):
# num = 9119
    num_str = str(num)

    square = [str(int(num) * int(num)) for num in num_str]
    
    return int(''.join(square))


print(square_digit(9119))