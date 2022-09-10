def flip_num(x):
    num = x
    flip = 0
    while num:
        flip = flip * 10 + num % 10
        num //= 10

    return flip

x = 1234548494
print(flip_num(x))
