def main(a):
    message =''
    if a > 0 and a % 2 == 0:
        message = "positive even number"
    if a > 0 and a % 2 != 0:
        message = "positive odd number"
    
    if a < 0 and a % 2 == 0:
        message = "negative even number"
    if a < 0 and a % 2 != 0:
        message = "negative odd number"
    if a == 0:
        message = "the number is zero"
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    return message