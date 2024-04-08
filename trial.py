def count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count
number = int(input('Введите число: '))
print(f'Кол-во цифр в числе {number} равно {count(number)}')