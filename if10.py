def main(temp):
    message = ''
    if temp < 0:
        message = "Freezing"
    if temp >= 1 and temp <= 10:
        message = "Very Cold"
    if temp >= 11 and temp <= 20:
        message = "Cold"
    if temp >=21 and temp <= 30:
        message = "Normal"
    if temp >= 31 and temp <= 40:
        message = "Hot"
    if temp > 40:
        message = "Very Hot"
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    return message