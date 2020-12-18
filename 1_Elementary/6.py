def end_zeros(num: int) -> int:

    sum = 0
    
    for number in list(reversed(str(num))):
        if int(number) == 0:
            sum += 1
        else:
            return sum
    return sum