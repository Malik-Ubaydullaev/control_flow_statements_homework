def main(a):
    message = ''
    a1 = pow(0, a)
    b = a // 10
    a2 = pow(0, b)
    c = b // 10
    a3 = pow(0, c)
    if a % 2 == 0 and (a1 == 0 and a2 == 0 and a3 != 0):
        message = "two-digit even number"
    if a % 2 != 0 and (a1 == 0 and a2 == 0 and a3 != 0):
        message = "two-digit odd number"
    
    if a % 2 == 0 and (a1 == 0 and a2 == 0 and a3 == 0):
        message = "three-digit even number"
    if a % 2 != 0 and (a1 == 0 and a2 == 0 and a3 == 0):
        message = "three-digit odd number"
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    return message