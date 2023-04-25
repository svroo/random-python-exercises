# Write a python function that takes a sequence of numbers
# and determines whether all the numbers are different from each other.

# @autor : Rodrigo Salazar

def test(list_one = list()):
    """
    In this function you will find out if 
    there are diferent numbers from each other
    """
    if len(list_one) == len(set(list_one)):
        return True
    else:
        return False

print(test([1,2,3,44,10, 15, 22, 1]))
