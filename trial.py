def count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count
number = int(input('Введите число: '))
print(f'Кол-во цифр в числе {number} равно {count(number)}')

def text(txt):
    lettersCount = 0
    for i in txt:
        if letter == i:
           lettersCount += 1
    return lettersCount
txt = input('Введите текст:')
letter = input('Введите букву для поиска:')
print(f'Кол-во букв {letter} в тексте равно {text(txt)}')