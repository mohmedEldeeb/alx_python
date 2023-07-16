def pow(a, b):
    value = 1
    for _ in range(abs(b)):
        value *= a
    if b < 0:
        value = 1.0 / value
    return value
