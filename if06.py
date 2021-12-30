def main(a,b,c):
    count_positive = 0
    count_negative = 0
    message = ''
    if a > 0:
        count_positive += 1
    if a < 0:
        count_negative += 1
    
    if b > 0:
        count_positive += 1
    if b < 0:
        count_negative += 1
    
    if c > 0: 
        count_positive += 1
    if c < 0:
        count_negative += 1
    
    if count_positive > count_negative:
        message = "there are a lot of positive numbers"
    if count_positive < count_negative:
        message = "there are a lot of negative numbers"
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    return message