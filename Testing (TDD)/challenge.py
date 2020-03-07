
def average(num_list):
    """Return the average for a list of numbers
    
    >>> average([1,2])
    1.5

    """
    return sum(num_list) / len(num_list)

print(average([1,2]))