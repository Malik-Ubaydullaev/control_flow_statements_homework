def main(a):
    result = False
    a1 = a % 10
    a2 = a // 10
    b = str(a1) + str(a2)
    new_a = int(b)
    
    if new_a == a or new_a < a:
        result = True
    else:
        result = False
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    return result