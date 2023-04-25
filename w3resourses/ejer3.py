# In mathematics, a square number or perfect 
# square is an integer that is the square of an integer;
#  in other words, it is the product of some integer with itself.

# Autor: Rodrigo Salazar

n = 25
def is_square(n):
    if n < 0 :
        return False
    sqrt = int(n ** 0.5)
    print(sqrt)

    return (sqrt ** 2) == n

print(is_square(25))
