def solution(arr):
    lcm = 1
    gcm = {}
    exponent = 0
    for origin_num in arr:
        num = origin_num
        cm = 2
        while cm <= origin_num:
            if num % cm == 0:
                num /= cm
                exponent += 1
            else:
                if (exponent != 0) and ((cm not in gcm) or (gcm[cm] < exponent)):
                    gcm[cm] = exponent
                cm += 1
                exponent = 0

    for num, exp in gcm.items():
        lcm *= num**exp

    return lcm