def digital_root(n):
    digits = [int(x) for x in str(n)]
    suma = 0
    for digit in digits:
        suma += digit
    if suma > 9:
        return digital_root(suma)
    else:
        return suma
# other solution
# def digital_root(n):
#   return n%9 or n and 9
# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

print(digital_root(493193))
