def digit_sum(number):
    if number < 10:
        return number
    digit = number % 10
    return digit + digit_sum(number // 10)
number = 5824
result = digit_sum(number)
print("Sum of digits:", result)