# 1.1
print(31, 18, 79)

# 1.2
print(47, ' ', 52, ' ', 150, sep='')

# 1.3
print(50)
print(10)

# 1.4
print(5)
print(10)
print(21)

# 1.5
print(1)
print(2)

# 1.6
print(f"{3.1415926:.3f}")

# 1.7
print(f"{2.71828:.1f}")

# 1.8
n = int(input("Введите число: "))
print("Вы ввели число", n)

# 1.9
n = int(input("Введите число: "))
print(n, "— вот какое число Вы ввели")

# 1.10
name = input("Введите имя: ")
print(name)

# 1.11
team = input("Введите название футбольной команды: ")
print(team, "— это чемпион!")

# 1.12
name = input("Введите имя: ")
print("Привет,", name + "!")

# 1.13
n = int(input("Введите целое число: "))
print(f"Следующее за числом {n} число – {n+1}.")
print(f"Для числа {n} предыдущее число – {n-1}.")

# 1.14
a, b, c = map(int, input("Введите три числа через пробел: ").split())
print(a, ' ', b, ' ', c, sep='')

# 5.1
for _ in range(9):
    print(20, end=' ')
print()

# 5.2
num = int(input("Введите число: "))
times = int(input("Сколько раз вывести? "))
for _ in range(times):
    print(num, end=' ')
print()

# 5.3а
for i in range(20, 36):
    print(i)

# 5.3б
a = int(input("Введите a (<=50): "))
for i in range(a, 51):
    print(i)

# 5.3в
b = int(input("Введите b (>10): "))
for i in range(10, b+1):
    print(i**3)

# 5.3г
a = int(input("Введите a: "))
b = int(input("Введите b (>a): "))
for i in range(a, b+1):
    print(i)

# 5.4а
for i in range(10, 26):
    print(i, i+0.4)

# 5.4б
for i in range(25, 36):
    print(i, i+0.5, i-0.2)

# 5.5а
for i in range(21, 9, -1):
    print(i, i-1.8)

# 5.5б
for i in range(45, 24, -1):
    print(i, i-0.5, i-0.8)

# 5.6а
for i in range(21, 36):
    print(i, i-0.6)

# 5.6б
for i in range(16, 25):
    print(i, i-0.5, i+0.8)

# 5.7
price = 20.4
for i in range(2, 21):
    print(i, 'шт. -', round(price * i, 2), 'руб.')

# 5.8
print("Фунты    Кг")
for pounds in range(1, 11):
    kg = pounds * 0.453
    print(pounds, '      ', round(kg, 2))

# 5.9
print("Дюймы   Сантиметры")
for inches in range(10, 23):
    cm = inches * 2.54
    print(inches, '      ', round(cm, 2))

# 5.10
rate = float(input("Введите курс доллара к рублю: "))
for dollars in range(1, 21):
    rubles = dollars * rate
    print(dollars, 'USD =', round(rubles, 2), 'RUB')

# 5.11
import math
R = 6350
for h in range(1, 11):
    d = math.sqrt((R + h)**2 - R**2)
    print(f"Высота {h} км: расстояние до горизонта {round(d, 2)} км")

# 5.12
import math
p0 = 1.29
z = 1.25e-4
print("Высота (м)   Плотность (кг/м³)")
for h in range(0, 1100, 100):
    p = p0 * math.exp(-h * z)
    print(h, '         ', round(p, 4))

# 5.13
for i in range(1, 10):
    print(f"{i} × 7 = {i*7}")

# 5.14
for i in range(1, 10):
    print(f"9 × {i} = {9*i}")

# 5.15
n = int(input("Введите n (1–9): "))
for i in range(1, 10):
    print(f"{i} × {n} = {i*n}")

# 5.16
import math
for i in range(2, 16):
    print(math.sin(i))

# 5.17
for x in range(4, 29):
    t = x + 3
    y = 3*t**2 + 4.87*t - 3
    print(f"x={x}, y={y:.2f}")

# 5.18
for a in range(2, 18):
    t = 3*a
    z = 4.3*t**2 - 8*t + 13
    print(f"a={a}, z={z:.2f}")

# 5.19
import math
x = 0.1
while x <= 1.5:
    print(math.sin(x))
    x += 0.1

# 5.20
import math
x = 0.1
while x < 1.0:
    print(math.sqrt(x))
    x += 0.1

# 5.21
price_per_kg = float(input("Введите стоимость 1 кг сыра: "))
for grams in range(50, 1001, 50):
    cost = (grams / 1000) * price_per_kg
    print(f"{grams} г = {cost:.2f} руб.")

# 5.22
price_per_kg = float(input("Введите стоимость 1 кг конфет: "))
for grams in range(100, 2001, 100):
    cost = (grams / 1000) * price_per_kg
    print(f"{grams} г = {cost:.2f} руб.")

# 5.23
x = 2.1
while x <= 2.8:
    print(x)
    x += 0.1

# 5.24
x = 3.2
while x <= 3.9:
    print(x)
    x += 0.1

# 5.25
x = 2.2
while x <= 4.2:
    print(x)
    x += 0.2

# 5.26
x = 4.4
while x <= 6.4:
    print(x)
    x += 0.2

# 5.27а
total = sum(range(200, 601))
print("Сумма от 200 до 600:", total)

# 5.27б
a = int(input("Введите a (<=400): "))
total = sum(range(a, 401))
print("Сумма от", a, "до 400:", total)

# 5.27в
b = int(input("Введите b (>= -15): "))
total = sum(range(-15, b+1))
print("Сумма от -15 до", b, ":", total)

# 5.27г
a = int(input("Введите a: "))
b = int(input("Введите b (>= a): "))
total = sum(range(a, b+1))
print(f"Сумма от {a} до {b}: {total}")

# 5.28а
product = 1
for i in range(7, 15):
    product *= i
print("Произведение от 7 до 14:", product)

# 5.28б
a = int(input("Введите a (1–15): "))
product = 1
for i in range(a, 16):
    product *= i
print("Произведение от", a, "до 15:", product)

# 5.28в
b = int(input("Введите b (1–10): "))
product = 1
for i in range(1, b+1):
    product *= i
print("Произведение от 1 до", b, ":", product)

# 5.28г
a = int(input("Введите a: "))
b = int(input("Введите b (>= a): "))
product = 1
for i in range(a, b+1):
    product *= i
print(f"Произведение от {a} до {b}: {product}")

# 5.29а
total = sum(range(1, 751))
avg = total / 750
print("Среднее арифметическое от 1 до 750:", avg)

# 5.29б
b = int(input("Введите b (>=150): "))
total = sum(range(150, b+1))
count = b - 150 + 1
avg = total / count
print(f"Среднее от 150 до {b}: {avg}")

# 5.29в
a = int(input("Введите a (<=200): "))
total = sum(range(a, 201))
count = 200 - a + 1
avg = total / count
print(f"Среднее от {a} до 200: {avg}")

# 5.29г
a = int(input("Введите a: "))
b = int(input("Введите b (>= a): "))
total = sum(range(a, b+1))
count = b - a + 1
avg = total / count
print(f"Среднее от {a} до {b}: {avg}")

# 5.30а
total = sum(i**3 for i in range(25, 41))
print("Сумма кубов от 25 до 40:", total)

# 5.30б
a = int(input("Введите a (0–50): "))
total = sum(i**2 for i in range(a, 51))
print(f"Сумма квадратов от {a} до 50: {total}")

# 5.30в
n = int(input("Введите n (1–100): "))
total = sum(i**2 for i in range(1, n+1))
print(f"Сумма квадратов от 1 до {n}: {total}")

# 5.30г
a = int(input("Введите a: "))
b = int(input("Введите b (>= a): "))
total = sum(i**2 for i in range(a, b+1))
print(f"Сумма квадратов от {a} до {b}: {total}")

# 5.31
n = int(input("Введите n: "))
total = sum((n + i)**2 for i in range(n+1))
print(f"Сумма от n^2 до (2n)^2: {total}")

# 5.32
n = int(input("Введите n: "))
total = sum(1/i for i in range(1, n+1))
print(f"Сумма 1 + 1/2 + ... + 1/{n}: {total:.4f}")

# 5.33
total = sum(i/(i+1) for i in range(2, 11))
print(f"2/3 + 3/4 + ... + 10/11: {total:.4f}")

# 5.34
n = int(input("Введите n: "))
total = sum(i**2 for i in range(1, n+1))
print(f"Сумма квадратов от 1 до {n}: {total}")

# 5.35
n = int(input("Введите n (>=2): "))
total = sum(i*(i+1) for i in range(1, n))
print(f"1×2 + 2×3 + ... + (n-1)×n: {total}")

import random
import math

# 11.1
arr = [37, 0, 50, 46, 34, 46, 0, 13]
print("Массив 11.1:", arr)

# 11.2
arr = []
for i in range(10):
    arr.append(int(input(f"Введите элемент {i+1}: ")))
print("Массив 11.2:", arr)

# 11.3а
arr = [random.random() for _ in range(15)]
print("11.3а (случайные 0–1):", arr[:5], "...")

# 11.3б
arr = [22 + random.random() for _ in range(15)]
print("11.3б (22–23):", arr[:5], "...")

# 11.3в
arr = [random.random() * 10 for _ in range(15)]
print("11.3в (0–10):", arr[:5], "...")

# 11.3г
arr = [random.uniform(-50, 50) for _ in range(15)]
print("11.3г (-50–50):", arr[:5], "...")

# 11.3д
arr = [random.randint(0, 10) for _ in range(15)]
print("11.3д (целые 0–10):", arr)

# 11.4
arr = ['#'] * 20
print("11.4:", ''.join(arr))

# 11.5
arr = [random.randint(163, 190) for _ in range(12)]
print("Росты 12 человек:", arr)

# 11.6
arr = [random.randint(50, 100) for _ in range(20)]
print("Веса 20 человек:", arr)

# 11.7
n = int(input("Введите n: "))
a = int(input("Введите a: "))
b = int(input("Введите b (>a): "))
arr = [random.randint(a, b) for _ in range(n)]
print(f"Массив из {n} чисел от {a} до {b}:", arr)

# 11.8
arr = [10, 20, 30, 40, 50]
index = int(input(f"Введите индекс (0–{len(arr)-1}): "))
print(f"Элемент с индексом {index}: {arr[index]}")

# 11.9
arr = [1, 2, 3, 4, 5]
print("Обратный порядок:", arr[::-1])

# 11.10
arr = list(range(1, 13))
print("Массив 1..12:", arr)

# 11.11
arr = list(range(1, 26))
arr.extend([100, 200])
print("Массив 1..25 + 100, 200:", arr)

# 11.12
arr = list(range(20, 0, -1))
print("Массив 20..1:", arr)

# 11.13
n = int(input("Введите n: "))
arr = [2**i for i in range(1, n+1)]
print(f"Степени двойки от 2^1 до 2^{n}:", arr)

# 11.14
n = int(input("Введите n (≤99999): "))
digits = [int(d) for d in str(n)][::-1]
arr = digits + [0]*(5 - len(digits))
print("Цифры в обратном порядке:", arr[:len(digits)])

# 11.15а – убывающая
arr = list(range(10, 2, -1))
print("Убывающая последовательность:", arr)

# 11.15б – возрастающая
arr = list(range(3, 11))
print("Возрастающая последовательность:", arr)

# 11.16а – арифметическая прогрессия
a = int(input("Введите первый член a: "))
p = int(input("Введите разность p: "))
arr = [a + i*p for i in range(10)]
print("Первые 10 членов арифм. прогрессии:", arr)

# 11.16б – геометрическая прогрессия
a = int(input("Введите первый член a: "))
z = int(input("Введите знаменатель z: "))
arr = [a * (z**i) for i in range(20)]
print("Первые 20 членов геом. прогрессии:", arr)

# 11.17 – числа Фибоначчи
fib = [1, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
print("Первые 10 чисел Фибоначчи:", fib)

# 11.18а – числа, кратные 15 или 17, начиная с 500
arr = []
num = 500
while len(arr) < 20:
    if num % 15 == 0 or num % 17 == 0:
        arr.append(num)
    num += 1
print("20 чисел, кратных 15 или 17 (с 500):", arr)

# 11.18б – первые 30 простых чисел
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2
while len(primes) < 30:
    if is_prime(num):
        primes.append(num)
    num += 1
print("Первые 30 простых чисел:", primes)

# 11.19 – первые 10 простых чисел, начиная с 100
primes = []
num = 100
while len(primes) < 10:
    if is_prime(num):
        primes.append(num)
    num += 1
print("10 простых чисел с 100:", primes)

# 11.20 – тест на таблицу умножения
results = []
for _ in range(20):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = int(input(f"{a} × {b} = ? "))
    results.append(answer == a*b)
print("Правильных ответов:", sum(results))

# 11.21 – массив из 20 неповторяющихся чисел
arr = random.sample(range(1, 101), 20)
print("20 неповторяющихся чисел:", arr)

import random
import math

# 11.22а – все неотрицательные элементы
arr = [random.randint(-10, 10) for _ in range(10)]
print("Массив:", arr)
print("Неотрицательные:", [x for x in arr if x >= 0])

# 11.22б – все элементы ≤ 100
arr = [random.randint(80, 120) for _ in range(10)]
print("Массив:", arr)
print("Элементы ≤ 100:", [x for x in arr if x <= 100])

# 11.23а – все чётные элементы
arr = [random.randint(1, 50) for _ in range(10)]
print("Массив:", arr)
print("Чётные:", [x for x in arr if x % 2 == 0])

# 11.23б – элементы, оканчивающиеся на 0
arr = [random.randint(10, 100) for _ in range(10)]
print("Массив:", arr)
print("Оканчивающиеся на 0:", [x for x in arr if x % 10 == 0])

# 11.24а – двузначные числа
arr = [random.randint(1, 200) for _ in range(15)]
print("Массив:", arr)
print("Двузначные:", [x for x in arr if 10 <= x <= 99])

# 11.24б – трёхзначные числа
print("Трёхзначные:", [x for x in arr if 100 <= x <= 999])

# 11.25а – элементы с чётными индексами (второй, четвёртый...)
arr = [random.randint(1, 20) for _ in range(10)]
print("Массив:", arr)
print("Элементы с чётными индексами (1,3,5...):", [arr[i] for i in range(1, len(arr), 2)])

# 11.25б – каждый третий элемент
print("Каждый третий элемент:", [arr[i] for i in range(2, len(arr), 3)])

# 11.26 – сначала неотрицательные, потом отрицательные
arr = [random.randint(-5, 5) for _ in range(10)]
print("Массив:", arr)
sorted_arr = [x for x in arr if x >= 0] + [x for x in arr if x < 0]
print("Сначала неотрицательные, потом отрицательные:", sorted_arr)

# 11.27 – сначала чётные, потом нечётные
arr = [random.randint(1, 20) for _ in range(10)]
print("Массив:", arr)
sorted_arr = [x for x in arr if x % 2 == 0] + [x for x in arr if x % 2 != 0]
print("Сначала чётные, потом нечётные:", sorted_arr)

# 11.28 – номера элементов, оканчивающихся на 0
arr = [random.randint(10, 100) for _ in range(15)]
print("Массив:", arr)
indices = [i for i, x in enumerate(arr) if x % 10 == 0]
print("Индексы элементов, оканчивающихся на 0:", indices)

# 11.29 – дни без осадков
precipitation = [random.randint(0, 10) for _ in range(31)]  # январь
print("Осадки за январь:", precipitation)
dry_days = [i+1 for i, p in enumerate(precipitation) if p == 0]
print("Дни без осадков:", dry_days)

# 11.30 – команды с < 3 побед
wins = [random.randint(0, 10) for _ in range(20)]
print("Победы 20 команд:", wins)
teams = [i+1 for i, w in enumerate(wins) if w < 3]
print("Номера команд с <3 побед:", teams)

# 11.31 – элементы на чётных и нечётных местах
arr = [random.randint(1, 30) for _ in range(10)]
print("Массив:", arr)
even_pos = [arr[i] for i in range(0, len(arr), 2)]
odd_pos = [arr[i] for i in range(1, len(arr), 2)]
print("На чётных позициях:", even_pos)
print("На нечётных позициях:", odd_pos)

# 11.32а – отрицательные → модуль
arr = [random.uniform(-10, 10) for _ in range(8)]
print("Исходный массив:", [round(x, 2) for x in arr])
arr = [abs(x) if x < 0 else x for x in arr]
print("После замены отрицательных на модуль:", [round(x, 2) for x in arr])

# 11.32б – элементы с нечётными индексами → квадратный корень
arr = [random.uniform(1, 20) for _ in range(8)]
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if i % 2 != 0:
        arr[i] = math.sqrt(arr[i])
print("После замены нечётных индексов на корень:", [round(x, 2) for x in arr])

# 11.33а – элементы >10 → квадратный корень
arr = [random.uniform(5, 15) for _ in range(8)]
print("Исходный массив:", [round(x, 2) for x in arr])
arr = [math.sqrt(x) if x > 10 else x for x in arr]
print("После замены >10 на корень:", [round(x, 2) for x in arr])

# 11.33б – элементы с чётными индексами → модуль
arr = [random.uniform(-5, 5) for _ in range(8)]
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] = abs(arr[i])
print("После замены чётных индексов на модуль:", [round(x, 2) for x in arr])

# 11.34а – вычитание элементов
arr = [random.uniform(-10, 10) for _ in range(10)]
k1, k2 = 2, 5
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if arr[i] > 0:
        arr[i] -= arr[k1]
    else:
        arr[i] -= arr[k2]
print(f"После вычитания (положительные - arr[{k1}], остальные - arr[{k2}]):", [round(x, 2) for x in arr])

# 11.34б – изменение по чётности индекса
arr = [random.uniform(-10, 10) for _ in range(10)]
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] += 1
    else:
        arr[i] -= 1
print("После +1 на чётных индексах, -1 на нечётных:", [round(x, 2) for x in arr])

# 11.35а – прибавление элементов
arr = [random.uniform(-10, 10) for _ in range(10)]
m1, m2 = 1, 4
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] += arr[m1]
    else:
        arr[i] += arr[m2]
print(f"После прибавления (отрицательные + arr[{m1}], остальные + arr[{m2}]):", [round(x, 2) for x in arr])

# 11.35б – изменение по чётности индекса (второй вариант)
arr = [random.uniform(-10, 10) for _ in range(10)]
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] *= 2
    else:
        arr[i] -= 1
print("После ×2 на чётных индексах, -1 на нечётных:", [round(x, 2) for x in arr])

# 11.36а – вычитание числа n из отрицательных
arr = [random.uniform(-5, 5) for _ in range(10)]
k1, n = 2, 3
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if arr[i] > 0:
        arr[i] -= arr[k1]
    elif arr[i] < 0:
        arr[i] -= n
print(f"После (положительные - arr[{k1}], отрицательные - {n}):", [round(x, 2) for x in arr])

# 11.36б – разные операции для разных знаков
arr = [random.uniform(-5, 5) for _ in range(10)]
a, b, c = 2, 3, 1
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if arr[i] > 0:
        arr[i] -= a
    elif arr[i] < 0:
        arr[i] += b
    else:
        arr[i] += c
print(f"После (положительные -{a}, отрицательные +{b}, нули +{c}):", [round(x, 2) for x in arr])

# 11.37а – прибавление/вычитание
arr = [random.uniform(-5, 5) for _ in range(10)]
a1, b = 2, 3
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] += arr[a1]
    elif arr[i] == 0:
        arr[i] -= b
print(f"После (отрицательные + arr[{a1}], нули -{b}):", [round(x, 2) for x in arr])

# 11.37б – вычитание/прибавление
arr = [random.uniform(-5, 5) for _ in range(10)]
a, b, c = 1, 2, 0.5
print("Исходный массив:", [round(x, 2) for x in arr])
for i in range(len(arr)):
    if arr[i] > 0:
        arr[i] -= a
    elif arr[i] < 0:
        arr[i] -= b
    else:
        arr[i] += c
print(f"После (положительные -{a}, отрицательные -{b}, нули +{c}):", [round(x, 2) for x in arr])

# 11.38а – элементы, оканчивающиеся на 4, уменьшить вдвое
arr = [random.randint(10, 50) for _ in range(10)]
print("Исходный массив:", arr)
arr = [x//2 if x % 10 == 4 else x for x in arr]
print("После уменьшения вдвое оканчивающихся на 4:", arr)

# 11.38б – чётные → квадрат, нечётные ×2
arr = [random.randint(1, 20) for _ in range(10)]
print("Исходный массив:", arr)
arr = [x**2 if x % 2 == 0 else x*2 for x in arr]
print("После (чётные → квадрат, нечётные ×2):", arr)

# 11.38в – чётные +a, элементы с чётными индексами -b
arr = [random.randint(1, 20) for _ in range(10)]
a, b = 3, 2
print("Исходный массив:", arr)
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] += a
    if i % 2 == 0:
        arr[i] -= b
print(f"После (чётные +{a}, чётные индексы -{b}):", arr)

# 11.39а – кратные 10 → 0
arr = [random.randint(10, 100) for _ in range(10)]
print("Исходный массив:", arr)
arr = [0 if x % 10 == 0 else x for x in arr]
print("После замены кратных 10 на 0:", arr)

# 11.39б – нечётные ×2, чётные //2
arr = [random.randint(1, 20) for _ in range(10)]
print("Исходный массив:", arr)
arr = [x*2 if x % 2 != 0 else x//2 for x in arr]
print("После (нечётные ×2, чётные //2):", arr)

# 11.39в – нечётные -m, нечётные индексы +n
arr = [random.randint(1, 20) for _ in range(10)]
m, n = 3, 2
print("Исходный массив:", arr)
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        arr[i] -= m
    if i % 2 != 0:
        arr[i] += n
print(f"После (нечётные -{m}, нечётные индексы +{n}):", arr)

# 11.40а – квадратный корень из элемента
arr = [random.uniform(1, 30) for _ in range(10)]
index = random.randint(0, len(arr)-1)
print("Массив:", [round(x, 2) for x in arr])
print(f"Квадратный корень из элемента {index} ({arr[index]}): {math.sqrt(arr[index]):.2f}")

# 11.40б – среднее арифметическое двух элементов
i, j = random.sample(range(len(arr)), 2)
avg = (arr[i] + arr[j]) / 2
print(f"Среднее арифметическое элементов {i} и {j}: {avg:.2f}")

# 11.41а – является ли s-й элемент положительным
arr = [random.randint(-10, 10) for _ in range(10)]
s = random.randint(0, len(arr)-1)
print("Массив:", arr)
print(f"Элемент {s} ({arr[s]}) положительный? {arr[s] > 0}")

# 11.41б – является ли k-й элемент чётным
k = random.randint(0, len(arr)-1)
print(f"Элемент {k} ({arr[k]}) чётный? {arr[k] % 2 == 0}")

# 11.41в – сравнение k-го и s-го элементов
print(f"Элемент {k} ({arr[k]}) {'>' if arr[k] > arr[s] else '<' if arr[k] < arr[s] else '='} элемента {s} ({arr[s]})")

# 11.42а – сумма всех элементов
arr = [random.randint(1, 20) for _ in range(10)]
total = sum(arr)
print("Массив:", arr)
print("Сумма всех элементов:", total)

# 11.42б – произведение всех элементов
product = 1
for x in arr:
    product *= x
print("Произведение всех элементов:", product)

# 1.14 (вывод трёх чисел с двумя пробелами)
a, b, c = map(int, input("Введите три числа: ").split())
print(a, '  ', b, '  ', c, sep='')

# 1.15 (вывод четырёх чисел с одним пробелом)
nums = list(map(int, input("Введите четыре числа: ").split()))
print(*nums)

# 1.16 (вывод с переменными)
t = int(input("t = "))
v = int(input("v = "))
x = int(input("x = "))
y = int(input("y = "))
print("100", t)
print("1949", v)
print(x, "25")
print(x, y)

# 2.1 (вычисление функций)
x = float(input("x = "))
y1 = 17*x**2 - 6*x + 13
print("y =", y1)

a = float(input("a = "))
y2 = 3*a**2 + 5*a - 21
print("y =", y2)

# 2.2 (вычисление дроби)
a = float(input("a = "))
result = (a**2 + 10) / (a**2 + 1)**0.5
print("Результат:", result)

# 2.3 (тригонометрия)
import math
a = float(input("a = "))
res1 = (2*a + math.sin(abs(3*a))) / 3.56
print("Результат 1:", res1)

x = float(input("x = "))
res2 = math.sin((3.2 + math.sqrt(1+x)) / (15*x))
print("Результат 2:", res2)

# 2.4 (периметр квадрата)
side = float(input("Сторона квадрата: "))
print("Периметр:", 4*side)

# 2.5 (диаметр окружности)
radius = float(input("Радиус окружности: "))
print("Диаметр:", 2*radius)

# 2.6 (горизонт)
R = 6350
h = float(input("Высота над Землёй (км): "))
d = (2*R*h + h**2)**0.5
print("Расстояние до горизонта:", round(d, 2), "км")

# 2.7 (куб)
edge = float(input("Длина ребра куба: "))
print("Объём:", edge**3)
print("Площадь боковой поверхности:", 4*edge**2)

# 2.8 (окружность и круг)
radius = float(input("Радиус: "))
print("Длина окружности:", 2*math.pi*radius)
print("Площадь круга:", math.pi*radius**2)

# 2.9 (функции двух переменных)
x, y = map(float, input("x y: ").split())
z = 2*x**3 - 3.44*x*y + 2.3*x**2 - 7.1*y + 2
print("z =", z)

a, b = map(float, input("a b: ").split())
x = 3.14*(a+b)**3 + 2.75*b**2 - 12.7*a - 4.1
print("x =", x)

# 2.10 (среднее арифметическое и геометрическое)
import math
a, b = map(int, input("Два целых числа: ").split())
print("Среднее арифметическое:", (a+b)/2)
print("Среднее геометрическое:", math.sqrt(a*b))

# 2.11 (плотность)
volume = float(input("Объём тела: "))
mass = float(input("Масса тела: "))
print("Плотность:", mass/volume)

# 2.12 (плотность населения)
people = int(input("Численность населения: "))
area = float(input("Площадь территории: "))
print("Плотность населения:", people/area, "чел./км²")

# 2.13 (линейное уравнение)
a, b = map(float, input("a b (a≠0): ").split())
print("x =", -b/a)

# 2.14 (гипотенуза)
a, b = map(float, input("Катеты: ").split())
c = (a**2 + b**2)**0.5
print("Гипотенуза:", c)

# 2.15 (площадь кольца)
R1, R2 = map(float, input("Внешний и внутренний радиусы: ").split())
print("Площадь кольца:", math.pi*(R1**2 - R2**2))

# 2.16 (периметр прямоугольного треугольника)
a, b = map(float, input("Катеты: ").split())
c = (a**2 + b**2)**0.5
print("Периметр:", a + b + c)

# 2.17 (периметр равнобедренной трапеции)
base1, base2, height = map(float, input("Основания и высота: ").split())
side = ((base2 - base1)/2)**2 + height**2
side = side**0.5
print("Периметр:", base1 + base2 + 2*side)

# 2.18 (функции двух переменных)
x, y = map(float, input("x y: ").split())
z = (x + (2+y)/x**2) / (y + 1/(x**2+10)**0.5)
q = 7.25*math.sin(x) - abs(y)
print("z =", z)
print("q =", q)

# 2.19 (ещё функции)
a, b = map(float, input("a b: ").split())
x = (2/(a**2+25) + b) / (b + (a+b)/2)**0.5
y = (abs(a) + 2*math.sin(b)) / (5.5*a)
print("x =", x)
print("y =", y)

# 2.20 (функции четырёх переменных)
e, f, g, h = map(float, input("e f g h: ").split())
a = (e - 3/f)**3 + g
b = math.sin(e) + math.cos(h)**2
c = (35*g) / (e*f - 3)
print("a =", a)
print("b =", b)
print("c =", c)

# 3.1 (метры в сантиметрах)
cm = int(input("Расстояние в см: "))
print("Полных метров:", cm // 100)

# 3.2 (центнеры в килограммах)
kg = int(input("Масса в кг: "))
print("Полных центнеров:", kg // 100)

# 3.3 (недели в днях)
days = 234
print("Полных недель:", days // 7)

# 3.4 (деление яблок)
N = int(input("Число школьников: "))
k = int(input("Число яблок: "))
print("Каждому достанется:", k // N)
print("Останется в корзинке:", k % N)

# 3.5 (квадраты в прямоугольнике)
print("Квадратов со стороной 130 мм:", 543 // 130)

# 3.6 (номер купе)
place = int(input("Номер места: "))
print("Номер купе:", (place - 1) // 4 + 1)

# 3.7 (этаж по номеру квартиры)
flat = int(input("Номер квартиры: "))
print("Этаж:", (flat - 1) // 3 + 1)

# 3.8 (ряд в кинотеатре)
ticket = int(input("Номер билета: "))
print("Ряд:", (ticket - 1) // 15 + 1)

# 3.9 (время из секунд)
n = int(input("Секунд с начала суток: "))
print("Часов:", n // 3600)
print("Минут с начала часа:", (n % 3600) // 60)
print("Секунд с начала минуты:", n % 60)

# 3.16 (десятки и единицы)
num = int(input("Двузначное число: "))
print("Десятков:", num // 10)
print("Единиц:", num % 10)

# 3.17 (сумма цифр двузначного числа)
num = int(input("Двузначное число: "))
print("Сумма цифр:", num//10 + num%10)

# 3.18 (перестановка цифр)
num = int(input("Двузначное число: "))
print("Число после перестановки:", (num%10)*10 + num//10)

# 3.19 (цифры трёхзначного числа)
num = input("Трёхзначное число: ")
print(','.join(num))

# 3.20 (операции с трёхзначным числом)
num = int(input("Трёхзначное число: "))
a, b, c = num//100, (num//10)%10, num%10
print("Единиц:", c)
print("Десятков:", b)
print("Сумма цифр:", a+b+c)
print("Произведение цифр:", a*b*c)

# 3.21 (число наоборот)
num = int(input("Трёхзначное число: "))
a, b, c = num//100, (num//10)%10, num%10
print("Число наоборот:", c*100 + b*10 + a)

# 3.22 (перемещение первой цифры в конец)
num = int(input("Трёхзначное число: "))
a, b, c = num//100, (num//10)%10, num%10
print("Новое число:", b*100 + c*10 + a)

# 3.23 (перемещение последней цифры в начало)
num = int(input("Трёхзначное число: "))
a, b, c = num//100, (num//10)%10, num%10
print("Новое число:", c*100 + a*10 + b)

# 3.24 (перестановка первой и второй цифр)
num = int(input("Трёхзначное число: "))
a, b, c = num//100, (num//10)%10, num%10
print("Новое число:", b*100 + a*10 + c)

# 3.25 (перестановка второй и третьей цифр)
num = int(input("Трёхзначное число: "))
a, b, c = num//100, (num//10)%10, num%10
print("Новое число:", a*100 + c*10 + b)

# 3.26 (все перестановки цифр)
from itertools import permutations
num = input("Трёхзначное число с разными цифрами: ")
perms = [''.join(p) for p in permutations(num)]
print("Все перестановки:", *perms)

# 3.27 (сумма цифр 4- и 5-значного числа)
num = input("4-значное число: ")
print("Сумма цифр:", sum(map(int, num)))
num = input("5-значное число: ")
print("Сумма цифр:", sum(map(int, num)))

# 4.1 (большее/меньшее из двух чисел)
a, b = map(float, input("Два различных числа: ").split())
print("Большее:", max(a, b))
print("Меньшее:", min(a, b))

# 4.2 (кусочная функция)
import math
x = float(input("x = "))
if x > 0:
    y = math.sin(x)**2
else:
    y = 1 - 2*math.sin(x**2)
print("y =", y)

# 4.3 (другая кусочная функция)
x = float(input("x = "))
if x > 0:
    y = math.sin(x**2)
else:
    y = 1 + 2*math.sin(x)**2
print("y =", y)

# 4.4 (область I или II)
x, y = map(float, input("x y: ").split())
if x < 4:
    print("Точка в области I")
else:
    print("Точка в области II")

# 4.5 (другой рисунок областей)
x, y = map(float, input("x y: ").split())
if y > 3:
    print("Точка в области I")
else:
    print("Точка в области II")

# 5.31 (сумма квадратов)
n = int(input("n = "))
total = sum((n + i)**2 for i in range(n+1))
print("Сумма:", total)

# 5.32 (гармонический ряд)
n = int(input("n = "))
total = sum(1/i for i in range(1, n+1))
print("Сумма:", total)

# 5.33 (сумма дробей)
total = sum(i/(i+1) for i in range(2, 11))
print("Сумма 2/3 + 3/4 + ... + 10/11:", total)

# 5.34 (сумма квадратов)
n = int(input("n = "))
total = sum(i**2 for i in range(1, n+1))
print("Сумма квадратов:", total)

# 5.35 (сумма произведений)
n = int(input("n (>=2): "))
total = sum(i*(i+1) for i in range(1, n))
print("1×2 + 2×3 + ... + (n-1)×n:", total)

# 5.36 (сумма степеней 1/3)
total = sum(1/(3**i) for i in range(9))
print("Сумма 1 + 1/3 + 1/9 + ... + 1/3^8:", total)

# 5.37 (знакочередующийся гармонический ряд)
n = int(input("n = "))
total = sum((1/i) * ((-1)**(i+1)) for i in range(1, n+1))
print("Сумма 1 - 1/2 + 1/3 - ...:", total)

# 5.38 (сумма нечётных степеней)
x = 2
total = sum(x**(2*i+1) / (2*i+1) for i in range(6))
print("Сумма x + x^3/3 + ... + x^11/11 при x=2:", total)

# 5.39 (сумма со знаками)
x = 2
total = sum(( (i+1)/(i+2) ) * (x**i) * ((-1)**i) for i in range(11))
print("Сумма 1 - 2/3*x + 3/4*x^2 - ... при x=2:", total)

# 5.40 (сумма цифр 9-значного числа)
num = input("9-значное число: ")
print("Сумма цифр:", sum(map(int, num)))

# 4.6 (графически заданные функции)
x = float(input("x = "))
if 0 <= x <= 2:
    y = x
else:
    y = 2
print("y =", y)

# 4.7 (сложная кусочная функция)
import math
x = float(input("x = "))
if math.sin(x) < 0:
    k = x**2
else:
    k = abs(x)

if k < x:
    f = k*x
else:
    f = k + x
print("f(x) =", f)

# 4.8 (другая сложная функция)
x = float(input("x = "))
if math.sin(x) >= 0:
    k = x**2
else:
    k = abs(x)

if x < k:
    f = abs(x)
else:
    f = k*x
print("f(x) =", f)

# 4.9 (максимум и минимум двух чисел)
a, b = map(float, input("Два различных числа: ").split())
if a > b:
    max_val, min_val = a, b
else:
    max_val, min_val = b, a
print("Максимум:", max_val)
print("Минимум:", min_val)

# 4.10 (сравнение расстояний)
km = float(input("Расстояние в км: "))
feet = float(input("Расстояние в футах: "))
meters = feet * 0.3048 / 1000  # переводим в км
print("Меньшее расстояние:", min(km, meters), "км")

# 4.11 (сравнение скоростей)
kmh = float(input("Скорость в км/ч: "))
ms = float(input("Скорость в м/с: "))
kmh2 = ms * 3.6
print("Большая скорость:", max(kmh, kmh2))

# 4.12 (площадь круга vs квадрата)
import math
radius = float(input("Радиус круга: "))
side = float(input("Сторона квадрата: "))
circle_area = math.pi * radius**2
square_area = side**2
print("Большая площадь у", "круга" if circle_area > square_area else "квадрата")

# 4.13 (плотность материалов)
v1, m1 = map(float, input("Объём и масса первого тела: ").split())
v2, m2 = map(float, input("Объём и масса второго тела: ").split())
d1, d2 = m1/v1, m2/v2
print("Большая плотность у", "первого" if d1 > d2 else "второго", "тела")

# 4.14 (ток в цепи)
R1, U1 = map(float, input("Сопротивление и напряжение на первом участке: ").split())
R2, U2 = map(float, input("Сопротивление и напряжение на втором участке: ").split())
I1, I2 = U1/R1, U2/R2
print("Меньший ток на", "первом" if I1 < I2 else "втором", "участке")

# 4.15 (наличие корней квадратного уравнения)
a, b, c = map(float, input("Коэффициенты a b c (a≠0): ").split())
D = b**2 - 4*a*c
print("Уравнение имеет корни" if D >= 0 else "Корней нет")

# 4.16 (решение квадратного уравнения)
a, b, c = map(float, input("a b c (a≠0): ").split())
D = b**2 - 4*a*c
if D >= 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print("Корни:", x1, x2)
else:
    print("Корней нет")

# 4.17 (возраст в годах)
birth_year = int(input("Год рождения: "))
birth_month = int(input("Месяц рождения: "))
curr_year = int(input("Текущий год: "))
curr_month = int(input("Текущий месяц: "))
age = curr_year - birth_year - (1 if curr_month < birth_month else 0)
print("Возраст:", age, "лет")

# 4.18 (круг в квадрате и наоборот)
import math
circle_area = float(input("Площадь круга: "))
square_area = float(input("Площадь квадрата: "))
circle_radius = (circle_area / math.pi)**0.5
square_side = square_area**0.5
print("Круг поместится в квадрате?", circle_radius*2 <= square_side)
print("Квадрат поместится в круге?", square_side*2**0.5 <= circle_radius*2)

# 4.22 (деление нацело)
m, n = map(int, input("Два целых числа: ").split())
if m % n == 0:
    print("Частное:", m // n)
else:
    print(f"{m} на {n} нацело не делится")

# 4.23 (является ли делителем)
a = int(input("a = "))
n = int(input("n = "))
print(f"{a} является делителем {n}" if n % a == 0 else f"{a} не является делителем {n}")

# 4.24 (чётность и окончание на 7)
num = int(input("Натуральное число: "))
print("Чётное?", num % 2 == 0)
print("Оканчивается на 7?", num % 10 == 7)

# 4.25 (следующее чётное)
n = int(input("Целое число: "))
print("Следующее чётное:", n + 2 if n % 2 == 0 else n + 1)

# 4.26 (сравнение цифр двузначного числа)
num = int(input("Двузначное число: "))
a, b = num // 10, num % 10
if a > b:
    print("Первая цифра больше")
elif a < b:
    print("Вторая цифра больше")
else:
    print("Цифры равны")

# 4.27 (проверка равенства квадрата числа и суммы кубов цифр)
num = int(input("Двузначное число: "))
a, b = num // 10, num % 10
print("Равенство выполняется" if num**2 == 4*(a**3 + b**3) else "Не выполняется")

# 4.28 (сумма цифр двузначного числа)
num = int(input("Двузначное число: "))
s = num//10 + num%10
print("Сумма цифр двузначна?", 10 <= s <= 99)
a = int(input("Число a: "))
print("Сумма цифр > a?", s > a)

# 4.29 (кратность суммы цифр)
num = int(input("Двузначное число: "))
s = num//10 + num%10
print("Сумма цифр кратна 3?", s % 3 == 0)
a = int(input("Число a: "))
print("Сумма цифр кратна a?", s % a == 0)

# 4.30 (палиндром трёхзначный)
num = int(input("Трёхзначное число: "))
a, b, c = num//100, (num//10)%10, num%10
print("Палиндром?", a == c)

# 5.41 (произведение и сумма последних n цифр)
num = int(input("Натуральное число: "))
n = int(input("n: "))
total, product = 0, 1
for _ in range(n):
    digit = num % 10
    total += digit
    product *= digit
    num //= 10
print("Сумма:", total)
print("Произведение:", product)

# 5.42 ("Странный муж")
N = 100
distance = 0
total_path = 0
for i in range(1, N+1):
    if i % 2 == 1:
        distance += 1/i
    else:
        distance -= 1/i
    total_path += 1/i
print("Расстояние от дома после 100 этапов:", distance)
print("Общий путь:", total_path)

# 5.43 (последовательность a_k = k*a_{k-1} + 1/k)
n = int(input("n = "))
a = [1] * (n+1)
for k in range(1, n+1):
    a[k] = k*a[k-1] + 1/k
print("Последовательность:", a[1:])

# 5.44 (числа Фибоначчи)
n = int(input("n (≥3): "))
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(f"{n}-й член:", fib[-1])
print("Первые n членов:", fib)

# 5.45 (члены Фибоначчи с 3-го по 10-й)
fib = [1, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
print("3-й – 10-й члены:", fib[2:])

# 5.46 (последовательность дробей)
k = int(input("k = "))
num1, num2 = 1, 2
den1, den2 = 1, 1
for i in range(3, k+1):
    num1, num2 = num2, num1 + num2
    den1, den2 = den2, den1 + den2
print(f"{k}-й член: {num2}/{den2}")

# 5.47 (последовательность v_i)
n = int(input("n (≥4): "))
v = [0, 0, 1.5]  # v1, v2, v3
for i in range(4, n+1):
    vi = ((i-1)/(i**2+1))*v[-1] - v[-2] + v[-3]
    v.append(vi)
print(f"v_{n} = {v[-1]}")

# 5.48 (амеба)
cells = 1
for hours in range(3, 25, 3):
    cells *= 2
    print(f"Через {hours} часов: {cells} клеток")

# 5.49 (банковский вклад)
deposit = 1000
for month in range(1, 11):
    increase = deposit * 0.02
    deposit += increase
    print(f"Прирост за {month}-й месяц: {increase:.2f} руб.")

deposit = 1000
for month in range(1, 13):
    deposit *= 1.02
    if month >= 3:
        print(f"Сумма через {month} месяцев: {deposit:.2f} руб.")

# 5.50 (лыжник)
distance = 10
total = 0
for day in range(2, 11):
    distance *= 1.1
    print(f"День {day}: {distance:.2f} км")
    if day <= 7:
        total += distance
print(f"Суммарный путь за первые 7 дней: {total:.2f} км")

# 5.51 (урожайность)
area = 100
yield_per_hectare = 20
total_yield = 0
for year in range(1, 9):
    if year > 1:
        area *= 1.05
        yield_per_hectare *= 1.02
    if year >= 2:
        print(f"Урожайность {year}-го года: {yield_per_hectare:.2f} ц/га")
    if 4 <= year <= 7:
        print(f"Площадь {year}-го года: {area:.2f} га")
    total_yield += area * yield_per_hectare
    if year == 6:
        print(f"Урожай за первые 6 лет: {total_yield:.2f} ц")

# 5.52 (шары)
import math
V = 0
r = 5  # внутренний радиус первого шара в см
for i in range(12):
    V += 4/3 * math.pi * (r/100)**3  # переводим в метры, затем в литры
    r += 0.5  # толщина стенки 5 мм
print(f"Суммарный объем: {V*1000:.2f} л")  # м³ → литры

# 5.53 (сумма степеней двойки)
total = 0
term = 4  # 2^2
for _ in range(9):  # 2^2 до 2^10
    total += term
    term *= 2
print("Сумма 2^2 + 2^3 + ... + 2^10:", total)

# 5.54 (степени числа)
a = float(input("a = "))
n = int(input("n = "))
power = 1
for i in range(1, n+1):
    power *= a
    print(f"{a}^{i} = {power}")

# 5.55 (знакочередующаяся сумма квадратов)
total = 0
sign = -1
for i in range(1, 11):
    total += sign * i**2
    sign *= -1
print("-1^2 + 2^2 - 3^2 + ... + 10^2 =", total)

# 5.56 (площадь арки синусоиды методом прямоугольников)
import math
area = 0
dx = 0.001
x = 0
while x <= math.pi:
    area += math.sin(x) * dx
    x += dx
print("Площадь одной арки синусоиды ≈", area)

# 5.57 (площадь под параболой)
def f(x):
    return 0.3*(x-1)**2 + 3

area = 0
dx = 0.001
x = 2
while f(x) <= 4:
    area += (f(x) - 2) * dx
    x += dx
print("Площадь фигуры ≈", area)

# 5.58 (площадь другой фигуры)
def f(x):
    return 0.4*(x+2)**2 + 1

area = 0
dx = 0.001
x = -2
while f(x) <= 2:
    area += (f(x) - 0) * dx
    x += dx
print("Площадь фигуры ≈", area)

# 5.59 (факториал)
n = int(input("n: "))
fact = 1
for i in range(2, n+1):
    fact *= i
print(f"{n}! = {fact}")

# 5.60 (умножение без умножения)
n = int(input("Целое число n: "))
a = float(input("Вещественное число a: "))
product = 0
for _ in range(abs(n)):
    product += a
if n < 0:
    product = -product
print(f"{a} * {n} = {product}")

# 5.61 (умножение сложением, два способа)
x = int(input("x: "))
y = int(input("y: "))
# Способ 1
product = 0
for _ in range(y):
    product += x
print(f"{x} * {y} = {product} (способ 1)")
# Способ 2
product = 0
for _ in range(x):
    product += y
print(f"{x} * {y} = {product} (способ 2)")

# 5.62 (степень без степени)
a = float(input("a: "))
n = int(input("n: "))
result = 1
for _ in range(n):
    result *= a
print(f"{a}^{n} = {result}")

# 5.63 (цепочка квадратов)
result = 20**2
for i in range(19, 0, -1):
    result = (abs(result - i**2))**2
print("Результат:", result)

# 5.64 (число наоборот для 7-значного)
num = input("7-значное число: ")
print("Число наоборот:", num[::-1])

# 5.65 (квадрат как сумма нечётных)
n = int(input("n: "))
total = 0
for i in range(1, 2*n, 2):
    total += i
print(f"{n}^2 = 1+3+...+{2*n-1} = {total}")

# 5.66 (сумма квадратов через нечётные)
total = 0
odd = 1
for i in range(1, 13):
    square = 0
    for _ in range(i):
        square += odd
        odd += 2
    total += square
    odd = 1  # сброс для следующего квадрата
print("Сумма квадратов от 1 до 12:", total)

# 5.67 (куб как сумма последовательных нечётных)
n = int(input("n: "))
first = n*(n-1) + 1
total = sum(first + 2*i for i in range(n))
print(f"{n}^3 = {first}+{first+2}+... = {total}")

# 5.68 (сумма факториалов)
n = int(input("n (1 < n ≤ 10): "))
total = 0
fact = 1
for i in range(1, n+1):
    fact *= i
    total += fact
print(f"1! + 2! + ... + {n}! = {total}")

# 5.69 (сумма 1/k!)
n = int(input("n (1 < n ≤ 10): "))
total = 1
fact = 1
for i in range(1, n+1):
    fact *= i
    total += 1/fact
print(f"1 + 1/1! + 1/2! + ... + 1/{n}! = {total}")

# 5.70 (сумма x^k/k!)
import math
x = float(input("x = "))
n = int(input("n (1 < n ≤ 10): "))
total = 1
fact = 1
power = 1
for i in range(1, n+1):
    fact *= i
    power *= x
    total += power / fact
print(f"1 + x/1! + x^2/2! + ... + x^{n}/{n}! = {total}")

# 5.71 (цепочка корней)
import math
total = math.sqrt(50)
for i in range(49, 0, -1):
    total = math.sqrt(i + total)
print("√(1+√(2+√(3+...+√(50)))) ≈", total)

# 6.1 (целочисленное деление и остаток без операторов // и %)
a = int(input("a: "))
b = int(input("b (a > b): "))
# Целочисленное деление
quotient = 0
temp = a
while temp >= b:
    temp -= b
    quotient += 1
print("Целочисленное деление:", quotient)
# Остаток
remainder = a
while remainder >= b:
    remainder -= b
print("Остаток:", remainder)

# 6.2 (натуральные числа ≤ n)
n = int(input("n: "))
i = 1
while i <= n:
    print(i, end=' ')
    i += 1
print()

# 6.3 (нечётные числа от 10 до 100)
i = 11
while i <= 99:
    print(i, end=' ')
    i += 2
print()

# 6.4 (минимальное число >190, кратное 17)
num = 191
while num % 17 != 0:
    num += 1
print("Минимальное число >190, кратное 17:", num)

# 6.5 (максимальное число ≤5000, кратное 139)
num = 5000
while num % 139 != 0:
    num -= 1
print("Максимальное число ≤5000, кратное 139:", num)

# 6.6 (нахождение числа по факториалу)
fact = int(input("Факториал: "))
n = 1
prod = 1
while prod < fact:
    n += 1
    prod *= n
print("Число:", n if prod == fact else "не факториал")

# 6.7 (числа, квадрат которых ≤ n)
n = int(input("n: "))
i = 1
while i**2 <= n:
    print(i, end=' ')
    i += 1
print()

# 6.8 (первое число, квадрат которого > n, разными способами)
n = int(input("n: "))
# Способ 1
i = 1
while i**2 <= n:
    i += 1
print("Первое число (способ 1):", i)
# Способ 2
for i in range(1, 101):
    if i**2 > n:
        print("Первое число (способ 2):", i)
        break

# 6.9 (ввод чётного числа с проверкой)
while True:
    num = int(input("Введите чётное число: "))
    if num % 2 == 0:
        break
    print("Ошибка: число нечётное!")

# 6.10 (ввод пароля)
PASSWORD = 1234
while True:
    pwd = int(input("Введите пароль: "))
    if pwd == PASSWORD:
        print("Добро пожаловать!")
        break
    print("Неверный пароль!")

# 6.11 (ввод 10 чисел, прерывание при 0)
count = 0
while count < 10:
    num = int(input("Введите число: "))
    if num == 0:
        break
    count += 1
print("Введено чисел:", count)

# 6.12 (последовательность до 0)
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    print("Вы ввели число:", num)

# 6.13 (цикл с предусловием и постусловием)
# а) с предусловием
i = 10
while i <= 30:
    print(i)
    i += 1
# б) с постусловием (эмулируем, т.к. в Python нет do-while)
i = 10
while True:
    print(i)
    i += 1
    if i > 30:
        break

# 6.14 (от 100 до 80)
i = 100
while i >= 80:
    print(i)
    i -= 1

# 6.15 (перевод на Python)
n = 21
while n <= 151:
    print(2 * n)
    n += 10

# 6.16
n = 2.0
while n <= 12:
    print(n)
    n += 0.5

# 6.17 (числа 1.0, 1.5, ..., 13.5)
x = 1.0
while x <= 13.5:
    print(x)
    x += 0.5

# 6.18 (квадратные корни от a до b)
a = int(input("a: "))
b = int(input("b (b > a): "))
# а) с предусловием
i = a
while i <= b:
    print(i**0.5)
    i += 1
# б) с постусловием
i = a
while True:
    print(i**0.5)
    i += 1
    if i > b:
        break

# 6.19 (цифры числа столбиком)
num = int(input("Натуральное число: "))
while num > 0:
    print(num % 10)
    num //= 10

# 6.20 (операции с цифрами)
num = int(input("Натуральное число: "))
s, count, product, squares, cubes = 0, 0, 1, 0, 0
first_digit = None
temp = num
while temp > 0:
    digit = temp % 10
    s += digit
    count += 1
    product *= digit
    squares += digit**2
    cubes += digit**3
    temp //= 10
first_digit = digit  # последняя полученная цифра - первая в числе
last_digit = num % 10
print("Сумма цифр:", s)
print("Количество цифр:", count)
print("Произведение цифр:", product)
print("Среднее арифметическое:", s/count)
print("Сумма квадратов цифр:", squares)
print("Сумма кубов цифр:", cubes)
print("Первая цифра:", first_digit)
print("Сумма первой и последней цифр:", first_digit + last_digit)

# 6.21 (вторая цифра с начала)
num = int(input("n (>9): "))
while num >= 100:
    num //= 10
print("Вторая цифра:", num % 10)

# 6.22 (третья цифра с начала)
num = int(input("n (>99): "))
while num >= 1000:
    num //= 10
print("Третья цифра:", num % 10)

# 6.23 (сумма m последних цифр)
num = int(input("Натуральное число: "))
m = int(input("m: "))
s = 0
for _ in range(m):
    if num == 0:
        break
    s += num % 10
    num //= 10
print("Сумма последних", m, "цифр:", s)

# 6.24 (знакопеременные суммы цифр)
num = int(input("Натуральное число: "))
# а) с конца
temp = num
s1, sign = 0, 1
while temp > 0:
    s1 += sign * (temp % 10)
    sign *= -1
    temp //= 10
print("Знакопеременная сумма с конца:", s1)
# б) с начала
digits = []
temp = num
while temp > 0:
    digits.append(temp % 10)
    temp //= 10
digits.reverse()
s2, sign = 0, 1
for d in digits:
    s2 += sign * d
    sign *= -1
print("Знакопеременная сумма с начала:", s2)

# 6.25 (наименьший делитель >1)
n = int(input("Натуральное число: "))
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        print("Наименьший делитель:", i)
        break
else:
    print("Наименьший делитель:", n)

# 6.26 (кратные 13 < 100)
# а) без условия
for i in range(13, 100, 13):
    print(i, end=' ')
print()
# б) с условием
i = 13
while i < 100:
    print(i, end=' ')
    i += 13
print()

# 6.27 (первые 15 чисел, кратные 19, с 100)
count, num = 0, 100
while count < 15:
    if num % 19 == 0:
        print(num, end=' ')
        count += 1
    num += 1
print()

# 6.28 (первые 20 чисел, кратные 13 или 17, с 500)
count, num = 0, 500
while count < 20:
    if num % 13 == 0 or num % 17 == 0:
        print(num, end=' ')
        count += 1
    num += 1
print()

# 6.29 (первые 10 чисел, оканчивающихся на 7, кратных 9, с 100)
count, num = 0, 100
while count < 10:
    if num % 10 == 7 and num % 9 == 0:
        print(num, end=' ')
        count += 1
    num += 1
print()

# 6.30 (целочисленное деление и остаток для любых a,b)
a = int(input("a: "))
b = int(input("b: "))
# Целочисленное деление
quotient = 0
if b > 0:
    while a >= b:
        a -= b
        quotient += 1
else:
    while a <= b:
        a -= b
        quotient += 1
print("Целочисленное деление:", quotient)
print("Остаток:", a)

# 6.31 (банковский вклад)
deposit = 1000
month = 0
increase = 0
while increase <= 30:
    month += 1
    increase = deposit * 0.02
    deposit += increase
print("Прирост превысит 30 руб. через", month, "месяцев")

deposit = 1000
month = 0
while deposit <= 1200:
    month += 1
    deposit *= 1.02
print("Вклад превысит 1200 руб. через", month, "месяцев")

# 6.32 (лыжник)
distance = 10
day = 1
while distance <= 20:
    day += 1
    distance *= 1.1
print("Больше 20 км пробежит в день", day)

distance = 10
total = 10
day = 1
while total <= 100:
    day += 1
    distance *= 1.1
    total += distance
print("Суммарный пробег превысит 100 км в день", day)

# 6.33 (урожайность)
area = 100
yield_per_ha = 20
year = 1
while yield_per_ha <= 22:
    year += 1
    yield_per_ha *= 1.02
print("Урожайность превысит 22 ц/га в году", year)

area = 100
year = 1
while area <= 120:
    year += 1
    area *= 1.05
print("Площадь превысит 120 га в году", year)

area = 100
yield_per_ha = 20
total_yield = area * yield_per_ha
year = 1
while total_yield <= 800:
    year += 1
    area *= 1.05
    yield_per_ha *= 1.02
    total_yield += area * yield_per_ha
print("Общий урожай превысит 800 ц в году", year)

# 6.34 (кратные взаимно простых чисел)
m = int(input("m: "))
n = int(input("n (взаимно простые): "))
for k in range(1, m*n+1):
    if k % m == 0 or k % n == 0:
        print(k, end=' ')
print()

# 6.35 (анализ цифр числа)
num = int(input("Натуральное число: "))
count3 = 0
last_digit = num % 10
count_last = 0
even_count = 0
sum_gt5 = 0
product_gt7 = 1
count0_5 = 0
temp = num
while temp > 0:
    digit = temp % 10
    if digit == 3:
        count3 += 1
    if digit == last_digit:
        count_last += 1
    # Для чётности цифр используем трюк без составного условия
    even_count += (digit % 2 == 0)
    if digit > 5:
        sum_gt5 += digit
    if digit > 7:
        product_gt7 *= digit
    if digit == 0 or digit == 5:
        count0_5 += 1
    temp //= 10
print("Цифр 3:", count3)
print("Последняя цифра встречается раз:", count_last)
print("Чётных цифр:", even_count)
print("Сумма цифр >5:", sum_gt5)
print("Произведение цифр >7:", product_gt7)
print("Цифр 0 и 5 всего:", count0_5)

# 6.36 (анализ цифр с параметром)
num = int(input("Натуральное число: "))
a = int(input("a (0-8): "))
x = int(input("x: "))
y = int(input("y: "))
count_a = 0
sum_gt_a = 0
even_sum = 0
count_xy = 0
temp = num
while temp > 0:
    digit = temp % 10
    if digit == a:
        count_a += 1
    if digit > a:
        sum_gt_a += digit
    if digit % 2 == 0:
        even_sum += digit
    if digit == x or digit == y:
        count_xy += 1
    temp //= 10
print("Цифр", a, "встречается:", count_a)
print("Сумма цифр >", a, ":", sum_gt_a)
print("Сумма чётных цифр:", even_sum)
print("Цифр", x, "и", y, "всего:", count_xy)

# 6.37 (номер цифры 8 с конца)
num = int(input("Натуральное число: "))
pos = 1
found = False
temp = num
while temp > 0:
    if temp % 10 == 8:
        print("Номер цифры 8 с конца:", pos)
        found = True
        break
    pos += 1
    temp //= 10
if not found:
    print("Цифры 8 нет (0)")

# 6.38 (номер цифры 3 с конца, самая правая)
num = int(input("Натуральное число: "))
pos = 1
last_pos = 0
temp = num
while temp > 0:
    if temp % 10 == 3:
        last_pos = pos
    pos += 1
    temp //= 10
print("Номер самой правой цифры 3 с конца:", last_pos if last_pos > 0 else 0)

# 6.39 (цифры числа с начала)
num = int(input("Натуральное число: "))
digits = []
temp = num
while temp > 0:
    digits.append(temp % 10)
    temp //= 10
for d in reversed(digits):
    print(d)

# 6.40 (сколько раз встречается первая цифра)
num = int(input("Натуральное число: "))
first_digit = int(str(num)[0])
count = 0
temp = num
while temp > 0:
    if temp % 10 == first_digit:
        count += 1
    temp //= 10
print("Первая цифра встречается раз:", count)

# 6.41 (максимальная и минимальная цифра)
num = int(input("Натуральное число: "))
max_digit = 0
min_digit = 9
temp = num
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    temp //= 10
print("Максимальная цифра:", max_digit)
print("Минимальная цифра:", min_digit)

# 6.42 (анализ max и min цифр)
num = int(input("Натуральное число: "))
max_digit = 0
min_digit = 9
temp = num
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    temp //= 10
print("Максимальная цифра:", max_digit)
print("Минимальная цифра:", min_digit)
print("Разность max-min:", max_digit - min_digit)
print("Сумма max+min:", max_digit + min_digit)

# 6.43 (кратность суммы max и min)
num = int(input("Натуральное число: "))
a = int(input("a: "))
max_digit = 0
min_digit = 9
temp = num
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    temp //= 10
print("Сумма max+min кратна", a, "?", (max_digit + min_digit) % a == 0)

# 6.44 (чётность разности max и min)
num = int(input("Натуральное число: "))
max_digit = 0
min_digit = 9
temp = num
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    temp //= 10
print("Разность max-min чётная?", (max_digit - min_digit) % 2 == 0)

# 6.45 (номера max и min цифр в числе с разными цифрами)
num = int(input("Натуральное число с разными цифрами: "))
max_digit = -1
min_digit = 10
max_pos_from_end = 0
min_pos_from_end = 0
max_pos_from_start = 0
min_pos_from_start = 0
temp = num
pos_from_end = 1
while temp > 0:
    digit = temp % 10
    if digit > max_digit:
        max_digit = digit
        max_pos_from_end = pos_from_end
    if digit < min_digit:
        min_digit = digit
        min_pos_from_end = pos_from_end
    pos_from_end += 1
    temp //= 10

# Для позиций от начала нужно перевернуть
digits = []
temp = num
while temp > 0:
    digits.append(temp % 10)
    temp //= 10
digits.reverse()
for i, digit in enumerate(digits, 1):
    if digit == max_digit:
        max_pos_from_start = i
    if digit == min_digit:
        min_pos_from_start = i

print("Максимальная цифра", max_digit)
print("Её номер с конца:", max_pos_from_end)
print("Её номер с начала:", max_pos_from_start)
print("Минимальная цифра", min_digit)
print("Её номер с конца:", min_pos_from_end)
print("Её номер с начала:", min_pos_from_start)

# 6.46 (номера max и min в одном цикле)
num = int(input("Натуральное число с разными цифрами: "))
max_digit = -1
min_digit = 10
max_pos_end = 0
min_pos_end = 0
max_pos_start = 0
min_pos_start = 0
temp = num
pos_end = 1
digits_rev = []
while temp > 0:
    digit = temp % 10
    digits_rev.append(digit)
    if digit > max_digit:
        max_digit = digit
        max_pos_end = pos_end
    if digit < min_digit:
        min_digit = digit
        min_pos_end = pos_end
    pos_end += 1
    temp //= 10

digits = list(reversed(digits_rev))
for i, digit in enumerate(digits, 1):
    if digit == max_digit:
        max_pos_start = i
    if digit == min_digit:
        min_pos_start = i

print("Max цифра:", max_digit, "номера:", max_pos_end, "(с конца)", max_pos_start, "(с начала)")
print("Min цифра:", min_digit, "номера:", min_pos_end, "(с конца)", min_pos_start, "(с начала)")

# 6.47 (какая цифра левее: max или min)
num = int(input("Натуральное число с разными цифрами: "))
digits = [int(d) for d in str(num)]
max_digit = max(digits)
min_digit = min(digits)
max_index = digits.index(max_digit)
min_index = digits.index(min_digit)
if max_index < min_index:
    print("Максимальная цифра левее минимальной")
else:
    print("Минимальная цифра левее максимальной")

# 6.48 (максимальная нечётная цифра)
num = int(input("Натуральное число: "))
max_odd = -1
temp = num
while temp > 0:
    digit = temp % 10
    if digit % 2 != 0 and digit > max_odd:
        max_odd = digit
    temp //= 10
print("Максимальная нечётная цифра:", max_odd if max_odd != -1 else "нет")

# 6.49 (проверки числа)
num = int(input("Натуральное число: "))
digits = [int(d) for d in str(num)]
s = sum(digits)
p = 1
for d in digits:
    p *= d
print("Сумма цифр >10?", s > 10)
print("Произведение цифр <50?", p < 50)
print("Количество цифр чётное?", len(digits) % 2 == 0)
print("Число четырёхзначное?", 1000 <= num <= 9999)
print("Первая цифра ≤6?", digits[0] <= 6)
print("Начинается и заканчивается одной цифрой?", digits[0] == digits[-1])
print("Первая цифра больше последней?", digits[0] > digits[-1])

# 7.1 (сумма 10 чисел)
nums = [float(input(f"Число {i+1}: ")) for i in range(10)]
print("Сумма:", sum(nums))

# 7.2 (сумма n вещественных чисел)
n = int(input("n: "))
nums = [float(input(f"Число {i+1}: ")) for i in range(n)]
print("Сумма:", sum(nums))

# 7.3 (периметр 12-угольника)
sides = [float(input(f"Сторона {i+1}: ")) for i in range(12)]
print("Периметр:", sum(sides))

# 7.4 (общая масса груза)
n = int(input("Количество предметов: "))
masses = [float(input(f"Масса {i+1}: ")) for i in range(n)]
print("Общая масса:", sum(masses))

# 7.5 (зарплата сотрудников)
n = int(input("Количество сотрудников: "))
salaries = [float(input(f"Зарплата {i+1}: ")) for i in range(n)]
print("Общая сумма:", sum(salaries))

# 7.6 (последовательное сопротивление)
n = int(input("Количество элементов: "))
resistances = [float(input(f"Сопротивление {i+1}: ")) for i in range(n)]
print("Общее сопротивление:", sum(resistances))

# 7.7 (параллельное сопротивление)
n = int(input("Количество элементов: "))
resistances = [float(input(f"Сопротивление {i+1}: ")) for i in range(n)]
total = sum(1/r for r in resistances)
print("Общее сопротивление:", 1/total if total != 0 else "бесконечность")

# 7.8 (последовательность до 0)
total = 0
count = 0
while True:
    num = int(input("Введите число (0 для конца): "))
    if num == 0:
        break
    total += num
    count += 1
print("Сумма:", total)
print("Количество:", count)

# 7.9 (оценки двух учеников)
grades1 = [int(input(f"Оценка 1-го ученика по предмету {i+1}: ")) for i in range(4)]
grades2 = [int(input(f"Оценка 2-го ученика по предмету {i+1}: ")) for i in range(4)]
print("Сумма оценок 1-го:", sum(grades1))
print("Сумма оценок 2-го:", sum(grades2))

# 7.10 (результаты пятиборцев)
scores1 = [float(input(f"Результат 1-го спортсмена в виде {i+1}: ")) for i in range(5)]
scores2 = [float(input(f"Результат 2-го спортсмена в виде {i+1}: ")) for i in range(5)]
print("Сумма баллов 1-го:", sum(scores1))
print("Сумма баллов 2-го:", sum(scores2))

# 7.11 (произведение 5 чисел)
nums = [float(input(f"Число {i+1}: ")) for i in range(5)]
product = 1
for x in nums:
    product *= x
print("Произведение:", product)

# 7.12 (вывод a1, a2 попеременно)
sequence = []
while True:
    num = int(input("Введите число (0 для конца): "))
    sequence.append(num)
    if num == 0:
        break
for i in range(0, len(sequence), 2):
    if i < len(sequence):
        print(sequence[i])
    if i+1 < len(sequence):
        print(sequence[i+1])

# 7.13 (сумма квадратов 10 чисел)
nums = [float(input(f"Число {i+1}: ")) for i in range(10)]
print("Сумма квадратов:", sum(x**2 for x in nums))

# 7.14 (сумма квадратов n вещественных)
n = int(input("n: "))
nums = [float(input(f"Число {i+1}: ")) for i in range(n)]
print("Сумма квадратов:", sum(x**2 for x in nums))

# 7.15 (сумма > 100.78)
nums = [float(input(f"Число {i+1}: ")) for i in range(10)]
print("Сумма превышает 100.78?", sum(nums) > 100.78)

# 7.16 (сумма < p)
n = int(input("n: "))
p = int(input("p: "))
nums = [int(input(f"Число {i+1}: ")) for i in range(n)]
print("Сумма < p?", sum(nums) < p)

# 7.17 (чётность суммы 8 чисел)
nums = [int(input(f"Число {i+1}: ")) for i in range(8)]
print("Сумма чётная?", sum(nums) % 2 == 0)

# 7.18 (кратность суммы)
n = int(input("n: "))
b = int(input("b: "))
nums = [int(input(f"Число {i+1}: ")) for i in range(n)]
print(f"Сумма кратна {b}?", sum(nums) % b == 0)

# 7.19 (осадки в феврале)
days = 28
precip = [float(input(f"Осадки за {i+1} февраля: ")) for i in range(days)]
last_year = float(input("Осадки за прошлый февраль: "))
print("Превысило?", sum(precip) > last_year)

# 7.20 (грузоподъёмность)
capacity = float(input("Грузоподъёмность автомобиля: "))
n = int(input("Количество грузов: "))
masses = [float(input(f"Масса груза {i+1}: ")) for i in range(n)]
print("Превышение?", sum(masses) > capacity)

# 7.21 (лучший результат десятиборца)
n = 10
scores1 = [float(input(f"Результат 1-го в виде {i+1}: ")) for i in range(n)]
scores2 = [float(input(f"Результат 2-го в виде {i+1}: ")) for i in range(n)]
if sum(scores1) > sum(scores2):
    print("Лучший результат у 1-го спортсмена")
elif sum(scores2) > sum(scores1):
    print("Лучший результат у 2-го спортсмена")
else:
    print("Результаты равны")

# 7.22 (более дешёвый набор)
costs1 = [float(input(f"Стоимость предмета {i+1} из набора 1: ")) for i in range(8)]
costs2 = [float(input(f"Стоимость предмета {i+1} из набора 2: ")) for i in range(8)]
if sum(costs1) < sum(costs2):
    print("Набор 1 дешевле")
elif sum(costs2) < sum(costs1):
    print("Набор 2 дешевле")
else:
    print("Стоимость одинакова")

# 7.23 (произведение < 10000)
nums = [int(input(f"Число {i+1}: ")) for i in range(8)]
product = 1
for x in nums:
    product *= x
print("Произведение < 10000?", product < 10000)

# 7.24 (произведение > s)
n = int(input("n: "))
s = float(input("s: "))
nums = [float(input(f"Число {i+1}: ")) for i in range(n)]
product = 1
for x in nums:
    product *= x
print("Произведение > s?", product > s)

# 7.25 (среднее 10 чисел)
nums = [float(input(f"Число {i+1}: ")) for i in range(10)]
print("Среднее арифметическое:", sum(nums)/len(nums))

# 7.26 (среднее n чисел)
n = int(input("n: "))
nums = [float(input(f"Число {i+1}: ")) for i in range(n)]
print("Среднее арифметическое:", sum(nums)/n)

# 7.27 (средняя оценка по физике)
n = 20
grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(n)]
print("Средняя оценка:", sum(grades)/n)

# 7.28 (средняя оценка ученика)
n = 10
grades = [int(input(f"Оценка по предмету {i+1}: ")) for i in range(n)]
print("Средняя оценка:", sum(grades)/n)

# 7.29 (средняя оценка по алгебре в классе)
n = int(input("Количество учеников: "))
grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(n)]
print("Средняя оценка:", sum(grades)/n)

# 7.30 (средняя масса предметов)
n = int(input("Количество предметов: "))
masses = [float(input(f"Масса предмета {i+1}: ")) for i in range(n)]
print("Средняя масса:", sum(masses)/n)

# 7.31 (среднее до отрицательного числа)
total = 0
count = 0
while True:
    num = int(input("Введите неотрицательное число (отрицательное для конца): "))
    if num < 0:
        break
    total += num
    count += 1
if count > 0:
    print("Среднее арифметическое:", total/count)
else:
    print("Чисел не было")

# 7.32 (средний возраст двух классов)
def avg_age(class_name):
    print(f"Класс {class_name}:")
    ages = [float(input(f"Возраст ученика {i+1}: ")) for i in range(20)]
    return sum(ages)/20

avg1 = avg_age("A")
avg2 = avg_age("B")
print("Средний возраст в классе A:", avg1)
print("Средний возраст в классе B:", avg2)

# 7.33 (среднедневные осадки)
jan_days = 31
mar_days = 31
jan = [float(input(f"Осадки за {i+1} января: ")) for i in range(jan_days)]
mar = [float(input(f"Осадки за {i+1} марта: ")) for i in range(mar_days)]
print("Среднее за январь:", sum(jan)/jan_days)
print("Среднее за март:", sum(mar)/mar_days)

# 7.34 (средний рост двух классов)
def avg_height(class_name, n):
    print(f"Класс {class_name}:")
    heights = [float(input(f"Рост ученика {i+1}: ")) for i in range(n)]
    return sum(heights)/n

n = int(input("Количество учеников в каждом классе: "))
avg1 = avg_height("A", n)
avg2 = avg_height("B", n)
print("Средний рост в классе A:", avg1)
print("Средний рост в классе B:", avg2)

# 7.35 (средняя оценка по физике в двух классах)
def avg_physics(class_name, n):
    print(f"Класс {class_name}:")
    grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(n)]
    return sum(grades)/n

n = int(input("Количество учеников в каждом классе: "))
avg1 = avg_physics("A", n)
avg2 = avg_physics("B", n)
print("Средняя оценка в классе A:", avg1)
print("Средняя оценка в классе B:", avg2)

# 7.36 (урожайность по области)
n = 10
areas = [float(input(f"Площадь района {i+1}: ")) for i in range(n)]
yields = [float(input(f"Урожайность района {i+1}: ")) for i in range(n)]
total_wheat = sum(areas[i] * yields[i] for i in range(n))
total_area = sum(areas)
print("Общее количество пшеницы:", total_wheat)
print("Средняя урожайность по области:", total_wheat/total_area)

# 7.37 (средняя плотность населения)
n = 12
populations = [float(input(f"Население района {i+1} (тыс.): ")) for i in range(n)]
areas = [float(input(f"Площадь района {i+1} (км²): ")) for i in range(n)]
total_pop = sum(populations)
total_area = sum(areas)
print("Средняя плотность:", total_pop/total_area, "тыс. чел./км²")

# 7.38 (общая площадь области)
n = 12
populations = [float(input(f"Население района {i+1} (тыс.): ")) for i in range(n)]
densities = [float(input(f"Плотность района {i+1} (тыс./км²): ")) for i in range(n)]
total_area = sum(populations[i]/densities[i] for i in range(n))
print("Общая площадь области:", total_area, "км²")

# 7.39 (операции над массивом)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(n)]
# а) сумма модулей
print("Сумма модулей:", sum(abs(x) for x in arr))
# б) произведение модулей
product = 1
for x in arr:
    product *= abs(x)
print("Произведение модулей:", product)
# в) суммы соседей
print("Суммы соседних пар:", [arr[i]+arr[i+1] for i in range(n-1)])
# г) знакопеременная сумма
total = 0
sign = 1
for x in arr:
    total += sign * x
    sign *= -1
print("Знакопеременная сумма:", total)

# 7.40 (сумма > 10.75)
arr = [float(input(f"Число {i+1}: ")) for i in range(12)]
total = sum(x for x in arr if x > 10.75)
print("Сумма чисел > 10.75:", total)

# 7.41 (сумма > p)
n = int(input("n: "))
p = float(input("p: "))
arr = [float(input(f"Число {i+1}: ")) for i in range(n)]
total = sum(x for x in arr if x > p)
print("Сумма чисел > p:", total)

# 7.42 (сумма чётных)
arr = [int(input(f"Число {i+1}: ")) for i in range(10)]
total = sum(x for x in arr if x % 2 == 0)
print("Сумма чётных чисел:", total)

# 7.43 (сумма оканчивающихся на 0)
arr = [int(input(f"Число {i+1}: ")) for i in range(10)]
total = sum(x for x in arr if x % 10 == 0)
print("Сумма чисел, оканчивающихся на 0:", total)

# 7.44 (сумма элементов с чётными индексами 2,4,6...)
arr = [int(input(f"a[{i+1}]: ")) for i in range(20)]
total = sum(arr[i] for i in range(1, 20, 2))  # индексы 1,3,5...
print("Сумма a2 + a4 + ...:", total)

# 7.45 (сумма с отрицательным знаком для нечётных индексов)
arr = [float(input(f"c[{i+1}]: ")) for i in range(15)]
total = -sum(arr[i] for i in range(0, 15, 2))  # индексы 0,2,4...
print("-c1 - c3 - c5 - ...:", total)

# 7.46 (операции с первым и последним)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(n)]
print("a1 + an:", arr[0] + arr[-1])
print("a2 - a_{n-1}:", arr[1] - arr[-2])

# 7.47 (стоимость товаров дороже 1000)
total = 0
while True:
    price = float(input("Стоимость товара (0 для конца): "))
    if price == 0:
        break
    if price > 1000:
        total += price
print("Общая стоимость товаров дороже 1000 руб.:", total)

# 7.48 (страницы в журналах)
pages_gas = []
pages_jour = []
while True:
    pages = int(input("Количество страниц (0 для конца): "))
    if pages == 0:
        break
    if pages <= 16:
        pages_gas.append(pages)
    else:
        pages_jour.append(pages)
print("Общее число страниц в журналах:", sum(pages_jour))

# 7.49 (осадки в чётные дни месяца)
days = int(input("Количество дней в месяце: "))
precip = [float(input(f"Осадки за день {i+1}: ")) for i in range(days)]
total = sum(precip[i] for i in range(1, days, 2))  # дни 2,4,6...
print("Осадки в чётные дни:", total)

# 7.50 (ученики в нечётных классах)
classes = 11
students = [int(input(f"Учеников в {i}-х классах: ")) for i in range(1, classes+1)]
total = sum(students[i] for i in range(0, classes, 2))  # 1,3,5 классы
print("Учеников в нечётных классах:", total)

# 7.51 (сумма первых подряд идущих нечётных)
total = 0
while True:
    num = int(input("Введите число (первое должно быть нечётным): "))
    if num % 2 == 0:
        break
    total += num
print("Сумма первых нечётных чисел:", total)

# 7.52 (проверки суммы)
arr = [int(input(f"b[{i+1}]: ")) for i in range(14)]
sum_gt20 = sum(x for x in arr if x > 20)
sum_lt50 = sum(x for x in arr if x < 50)
print("Сумма >20 превышает 100?", sum_gt20 > 100)
print("Сумма <50 чётная?", sum_lt50 % 2 == 0)

# 7.53 (проверки с условиями)
n = int(input("n: "))
arr = [int(input(f"m[{i+1}]: ")) for i in range(n)]
sum_lt25 = sum(x for x in arr if x < 25)
sum_le20 = sum(x for x in arr if x <= 20)
print("Сумма <25 не превышает 50?", sum_lt25 <= 50)
print("Сумма ≤20 кратна 3?", sum_le20 % 3 == 0)

# 7.54 (сумма >20.5)
n = int(input("n: "))
p = float(input("p: "))
arr = [float(input(f"d[{i+1}]: ")) for i in range(n)]
sum_gt20 = sum(x for x in arr if x > 20)
print("Сумма >20 меньше p?", sum_gt20 < p)

# 7.55 (сумма чисел ≤ m)
n = int(input("n: "))
m = int(input("m: "))
q = int(input("q: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(n)]
sum_le_m = sum(x for x in arr if x <= m)
print("Сумма ≤ m превышает q?", sum_le_m > q)

# 7.56 (сумма чисел ≤ m кратна p)
n = int(input("n: "))
m = int(input("m: "))
p = int(input("p: "))
arr = [int(input(f"c[{i+1}]: ")) for i in range(n)]
sum_le_m = sum(x for x in arr if x <= m)
print("Сумма ≤ m кратна p?", sum_le_m % p == 0)

# 7.57 (осадки по чётным и нечётным дням февраля)
days = 28
precip = [float(input(f"Осадки за {i+1} февраля: ")) for i in range(days)]
even_sum = sum(precip[i] for i in range(1, days, 2))
odd_sum = sum(precip[i] for i in range(0, days, 2))
print("По чётным выпало больше?", even_sum > odd_sum)

# 7.58 (жители по сторонам улицы)
n = int(input("Количество домов: "))
residents = [int(input(f"Жителей в доме {i+1}: ")) for i in range(n)]
odd_sum = sum(residents[i] for i in range(0, n, 2))
even_sum = sum(residents[i] for i in range(1, n, 2))
if odd_sum > even_sum:
    print("Больше жителей на нечётной стороне")
elif even_sum > odd_sum:
    print("Больше жителей на чётной стороне")
else:
    print("Поровну")

# 7.59 (количество пятёрок по информатике)
n = int(input("Количество учеников: "))
grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(n)]
count5 = grades.count(5)
print("Пятёрок:", count5)

# 7.60 (дни с температурой <0°C)
days = int(input("Количество дней: "))
temps = [float(input(f"Температура дня {i+1}: ")) for i in range(days)]
count_below0 = sum(1 for t in temps if t < 0)
print("Дней с t<0°C:", count_below0)

# 7.61 (юноши ростом <165 см)
n = 12
heights = [float(input(f"Рост юноши {i+1}: ")) for i in range(n)]
count_lt165 = sum(1 for h in heights if h < 165)
print("Юношей ростом <165 см:", count_lt165)

# 7.62 (количество чисел по условиям)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(n)]
p = int(input("p: "))
k = int(input("k: "))
count_gt_p = sum(1 for x in arr if x > p)
count_ends5 = sum(1 for x in arr if x % 10 == 5)
count_mult_k = sum(1 for x in arr if x % k == 0)
print("> p:", count_gt_p)
print("Оканчиваются на 5:", count_ends5)
print("Кратных k:", count_mult_k)

# 7.63 (пятёрки и двойки по химии)
n = int(input("Количество учеников: "))
grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(n)]
count5 = grades.count(5)
count2 = grades.count(2)
print("Пятёрок:", count5)
print("Двоек:", count2)

# 7.64 (люди до 1990 и после 2000)
n = int(input("Количество людей: "))
years = [int(input(f"Год рождения человека {i+1}: ")) for i in range(n)]
before1990 = sum(1 for y in years if y < 1990)
after2000 = sum(1 for y in years if y > 2000)
print("До 1990:", before1990)
print("После 2000:", after2000)

# 7.65 (команды с победами > поражений)
n = int(input("Количество команд: "))
count = 0
for i in range(n):
    wins = int(input(f"Побед команды {i+1}: "))
    losses = int(input(f"Поражений команды {i+1}: "))
    if wins > losses:
        count += 1
print("Команд с победами > поражений:", count)

# 7.66 (отрицательные числа в начале последовательности)
n = int(input("n: "))
count = 0
for i in range(n):
    num = float(input(f"Число {i+1}: "))
    if num >= 0:
        break
    count += 1
print("Отрицательных чисел в начале:", count)

# 7.67 (числа перед первым нулём)
count = 0
while True:
    num = float(input("Введите число: "))
    if num == 0:
        break
    count += 1
print("Чисел перед первым нулём:", count)

# 7.68 (равные элементы в начале)
n = int(input("n: "))
first = float(input("Число 1: "))
count = 1
for i in range(2, n+1):
    num = float(input(f"Число {i}: "))
    if num != first:
        break
    count += 1
print("Равных элементов в начале:", count)

# 7.69 (ученики с оценкой 5)
# Случай 1: не все имеют 5
n = 20
grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(n)]
count5 = 0
for grade in grades:
    if grade != 5:
        break
    count5 += 1
print("Учеников с оценкой 5:", count5)

# Случай 2: все могут иметь 5
count5 = 0
for grade in grades:
    if grade == 5:
        count5 += 1
    else:
        break
print("Учеников с оценкой 5 (случай 2):", count5)

# 7.70 (дни без осадков с 1 мая)
days = 31
precip = [float(input(f"Осадки за {i} мая: ")) for i in range(1, days+1)]
count_no_precip = 0
for p in precip:
    if p > 0:
        break
    count_no_precip += 1
print("Дней без осадков с начала мая:", count_no_precip)

# 7.71 (студенты с двойкой)
n = int(input("Количество студентов: "))
count2 = 0
for i in range(n):
    grade1 = int(input(f"Оценка за экзамен 1 студента {i+1}: "))
    grade2 = int(input(f"Оценка за экзамен 2 студента {i+1}: "))
    if grade1 == 2 or grade2 == 2:
        count2 += 1
print("Студентов с двойкой:", count2)

# 7.72 (отрицательные и положительные числа)
n = int(input("n: "))
arr = [float(input(f"a[{i+1}]: ")) for i in range(n)]
neg = sum(1 for x in arr if x < 0)
pos = sum(1 for x in arr if x > 0)
print("Отрицательных:", neg)
print("Положительных:", pos)

# 7.73 (кратные 3 и 7)
m = int(input("m: "))
arr = [int(input(f"x[{i+1}]: ")) for i in range(m)]
count3 = sum(1 for x in arr if x % 3 == 0)
count7 = sum(1 for x in arr if x % 7 == 0)
print("Кратных 3:", count3)
print("Кратных 7:", count7)

# 7.74 (тройки для треугольника)
n = int(input("Количество троек: "))
count = 0
for i in range(n):
    a, b, c = map(int, input(f"Тройка {i+1} (a≤b≤c): ").split())
    if a + b > c:
        count += 1
print("Троек для треугольника:", count)

# 7.75 (попадание снарядов в цель)
import math
n = int(input("Количество выстрелов: "))
hits = 0
g = 9.8
R = float(input("Расстояние до цели R: "))
H = float(input("Высота цели H: "))
P = float(input("Высота цели P: "))
for i in range(n):
    alpha = float(input(f"Угол α выстрела {i+1}: "))
    v0 = float(input(f"Начальная скорость v0 выстрела {i+1}: "))
    t = R / (v0 * math.cos(alpha))
    y = v0 * t * math.sin(alpha) - g * t**2 / 2
    if H <= y <= H + P:
        hits += 1
print("Процент попаданий:", (hits / n) * 100, "%")

# 7.76 (удаления в хоккее)
team1_removals = 0
team1_time = 0
team2_removals = 0
team2_time = 0
for i in range(24):
    team = int(input(f"Номер команды удаления {i+1}: "))
    time = int(input("Время удаления (2,5,10): "))
    if team == 1:
        team1_removals += 1
        team1_time += time
    else:
        team2_removals += 1
        team2_time += time
print("Команда 1: удалений", team1_removals, "время", team1_time)
print("Команда 2: удалений", team2_removals, "время", team2_time)

# 7.77 (штрафное время до окончания игры)
team1_removals = 0
team1_time = 0
team2_removals = 0
team2_time = 0
while True:
    team = int(input("Номер команды (0 для конца): "))
    if team == 0:
        break
    time = int(input("Время удаления (2,5,10): "))
    if team == 1:
        team1_removals += 1
        team1_time += time
    else:
        team2_removals += 1
        team2_time += time
print("Команда 1: удалений", team1_removals, "время", team1_time)
print("Команда 2: удалений", team2_removals, "время", team2_time)

# 7.78 (оценки по физике)
n = int(input("Количество учеников: "))
grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(n)]
count2 = grades.count(2)
count3 = grades.count(3)
count4 = grades.count(4)
count5 = grades.count(5)
print("Двоек:", count2)
print("Троек:", count3)
print("Четвёрок:", count4)
print("Пятёрок:", count5)

# 7.79 (результаты футбольных игр)
n = int(input("Количество игр: "))
points = [int(input(f"Очки за игру {i+1}: ")) for i in range(n)]
wins = points.count(3)
draws = points.count(1)
losses = points.count(0)
print("Выигрышей:", wins)
print("Ничьих:", draws)
print("Проигрышей:", losses)

# 7.80 (футбольные игры)
games = 20
results = []
for i in range(games):
    scored = int(input(f"Забито в игре {i+1}: "))
    conceded = int(input(f"Пропущено в игре {i+1}: "))
    if scored > conceded:
        results.append("выигрыш")
    elif scored == conceded:
        results.append("ничья")
    else:
        results.append("проигрыш")
print("Результаты игр:", results)
print("Выигрышей:", results.count("выигрыш"))
print("Проигрышей:", results.count("проигрыш"))
print("Выигрышей и ничьих:", results.count("выигрыш") + results.count("ничья"))
print("Выигрышей, ничьих, проигрышей:", results.count("выигрыш"), results.count("ничья"), results.count("проигрыш"))

# 7.81 (игры в виде одного числа)
games = 20
for i in range(games):
    result = input(f"Результат игры {i+1} (например, 32): ")
    if len(result) == 1:
        scored = conceded = int(result)
    else:
        scored = int(result[0])
        conceded = int(result[1])
    if scored > conceded:
        print("выигрыш")
    elif scored == conceded:
        print("ничья")
    else:
        print("проигрыш")

# 7.82 (пары соседних чисел)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(n)]
count_equal = sum(1 for i in range(n-1) if arr[i] == arr[i+1])
count_zero = sum(1 for i in range(n-1) if arr[i] == 0 and arr[i+1] == 0)
count_even = sum(1 for i in range(n-1) if arr[i] % 2 == 0 and arr[i+1] % 2 == 0)
count_ends5 = sum(1 for i in range(n-1) if arr[i] % 10 == 5 and arr[i+1] % 10 == 5)
print("Равных пар:", count_equal)
print("Пар нулей:", count_zero)
print("Чётных пар:", count_even)
print("Пар, оканчивающихся на 5:", count_ends5)

# 7.83 (есть ли чётное число)
n = int(input("Количество чисел: "))
arr = [int(input(f"Число {i+1}: ")) for i in range(n)]
has_even = any(x % 2 == 0 for x in arr)
print("Есть чётное число?", has_even)

# 7.84 (количество положительных ≤5)
arr = [int(input(f"a[{i+1}]: ")) for i in range(10)]
pos_count = sum(1 for x in arr if x > 0)
print("Количество положительных ≤5?", pos_count <= 5)

# 7.85 (количество чисел ≤33.2 кратно 4)
arr = [float(input(f"x[{i+1}]: ")) for i in range(15)]
count_le33 = sum(1 for x in arr if x <= 33.2)
print("Количество ≤33.2 кратно 4?", count_le33 % 4 == 0)

# 7.86 (количество чисел <20 равно 5)
n = int(input("n: "))
arr = [int(input(f"c[{i+1}]: ")) for i in range(n)]
count_lt20 = sum(1 for x in arr if x < 20)
print("Количество <20 равно 5?", count_lt20 == 5)

# 7.87 (количество положительных кратно 3)
m = int(input("m: "))
arr = [int(input(f"d[{i+1}]: ")) for i in range(m)]
pos_count = sum(1 for x in arr if x > 0)
print("Количество положительных кратно 3?", pos_count % 3 == 0)

# 7.88 (количество отрицательных > x)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(n)]
x = int(input("x: "))
neg_count = sum(1 for x in arr if x < 0)
print("Количество отрицательных > x?", neg_count > x)

# 7.89 (количество > m кратно p)
m = int(input("m: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(m)]
p = int(input("p: "))
threshold = int(input("порог: "))
count_gt = sum(1 for x in arr if x > threshold)
print(f"Количество > {threshold} кратно {p}?", count_gt % p == 0)

# 7.90 (нет ли троек?)
grades = [int(input(f"Оценка по предмету {i+1}: ")) for i in range(12)]
has_3 = 3 in grades
print("Нет троек?", not has_3)

# 7.91 (10 дней без осадков?)
days = 31
precip = [float(input(f"Осадки за {i} марта: ")) for i in range(1, days+1)]
dry_days = sum(1 for p in precip if p == 0)
print("10 дней без осадков?", dry_days == 10)

# 7.92 (есть ли двойки?)
n = 28
grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(n)]
has_2 = 2 in grades
print("Есть двойки?", has_2)

# 7.93 (есть ли мощность >200 л.с.?)
n = 30
powers = [int(input(f"Мощность автомобиля {i+1}: ")) for i in range(n)]
has_gt200 = any(p > 200 for p in powers)
print("Есть мощность >200 л.с.?", has_gt200)

# 7.94 (строгие локальные максимумы)
n = int(input("n: "))
arr = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
count = 0
for i in range(1, n-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        count += 1
print("Строгих локальных максимумов:", count)

# 7.95 (смена знака)
n = int(input("n: "))
arr = [int(input(f"Элемент {i+1}: ")) for i in range(n)]
changes = 0
for i in range(1, n):
    if arr[i] * arr[i-1] < 0:
        changes += 1
print("Смен знака:", changes)

# 7.96 (первая пара одинаковых соседних чисел)
arr = [int(input(f"a[{i+1}]: ")) for i in range(15)]
found = False
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print(f"Первая пара: индексы {i} и {i+1}")
        found = True
        break
if not found:
    print("Таких пар нет")

# 7.97 (первая пара одинаковых соседних, конец -1)
arr = []
while True:
    num = int(input("Введите число (-1 для конца): "))
    if num == -1:
        break
    arr.append(num)
found = False
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print(f"Первая пара: индексы {i} и {i+1}")
        found = True
        break
if not found:
    print("Таких пар нет")

# 7.98 (первая пара соседних нечётных чисел)
arr = [int(input(f"d[{i+1}]: ")) for i in range(20)]
found = False
for i in range(len(arr)-1):
    if arr[i] % 2 != 0 and arr[i+1] % 2 != 0:
        print(f"Первая пара нечётных: индексы {i} и {i+1}")
        found = True
        break
if not found:
    print("Таких пар нет")

# 7.99 (первая пара соседних чётных чисел, конец 9999)
arr = []
while True:
    num = int(input("Введите число (9999 для конца): "))
    if num == 9999:
        break
    arr.append(num)
found = False
for i in range(len(arr)-1):
    if arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
        print(f"Первая пара чётных: индексы {i} и {i+1}")
        found = True
        break
if not found:
    print("Таких пар нет")

# 7.100 (упорядоченность по возрастанию)
arr = [float(input(f"x[{i+1}]: ")) for i in range(15)]
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print(f"Нарушение на индексе {i}")
        break
else:
    print("Последовательность упорядочена")

# 7.101 (упорядоченность, конец 10000)
arr = []
while True:
    num = float(input("Введите число (10000 для конца): "))
    if num == 10000:
        break
    arr.append(num)
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print(f"Нарушение на индексе {i}")
        break
else:
    print("Последовательность упорядочена")

# 7.102 (список учеников по убыванию роста)
n = int(input("Количество учеников: "))
heights = [float(input(f"Рост ученика {i+1}: ")) for i in range(n)]
is_descending = all(heights[i] >= heights[i+1] for i in range(n-1))
print("Список по убыванию роста?", is_descending)

# 7.103 (команды по убыванию очков)
n = int(input("Количество команд: "))
points = [int(input(f"Очки команды {i+1}: ")) for i in range(n)]
is_descending = all(points[i] >= points[i+1] for i in range(n-1))
print("Команды по убыванию очков?", is_descending)

# 7.104 (все ли элементы равны)
arr = [int(input(f"x[{i+1}]: ")) for i in range(12)]
all_equal = all(x == arr[0] for x in arr)
print("Все элементы равны?", all_equal)

# 7.105 (все ли элементы равны, конец отрицательным)
arr = []
while True:
    num = int(input("Введите число (отрицательное для конца): "))
    if num < 0:
        break
    arr.append(num)
if arr:
    all_equal = all(x == arr[0] for x in arr)
    print("Все элементы равны?", all_equal)
else:
    print("Последовательность пуста")

# 7.106 (среднее чисел >20)
arr = [float(input(f"c[{i+1}]: ")) for i in range(16)]
gt20 = [x for x in arr if x > 20]
if gt20:
    print("Среднее чисел >20:", sum(gt20)/len(gt20))
else:
    print("Таких чисел нет")

# 7.107 (среднее чисел >n)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(12)]
gt_n = [x for x in arr if x > n]
if gt_n:
    print("Среднее чисел > n:", sum(gt_n)/len(gt_n))
else:
    print("Таких чисел нет")

# 7.108 (среднее чисел, кратных n)
n = int(input("n: "))
m = int(input("m: "))
arr = [int(input(f"b[{i+1}]: ")) for i in range(m)]
mult_n = [x for x in arr if x % n == 0]
if mult_n:
    print("Среднее кратных n:", sum(mult_n)/len(mult_n))
else:
    print("Таких чисел нет")

# 7.109 (среднее чётных и нечётных)
arr = [int(input(f"Число {i+1}: ")) for i in range(12)]
even = [x for x in arr if x % 2 == 0]
odd = [x for x in arr if x % 2 != 0]
if even:
    print("Среднее чётных:", sum(even)/len(even))
else:
    print("Чётных нет")
if odd:
    print("Среднее нечётных:", sum(odd)/len(odd))
else:
    print("Нечётных нет")

# 7.110 (средняя масса полных и остальных)
n = int(input("Количество людей: "))
masses = [float(input(f"Масса человека {i+1}: ")) for i in range(n)]
full = [m for m in masses if m > 100]
others = [m for m in masses if m <= 100]
if full:
    print("Средняя масса полных:", sum(full)/len(full))
else:
    print("Полных нет")
if others:
    print("Средняя масса остальных:", sum(others)/len(others))
else:
    print("Все полные")

# 7.111 (средний рост мальчиков и девочек)
n = int(input("Количество учеников: "))
heights = [float(input(f"Рост ученика {i+1} (отрицательный для мальчиков): ")) for i in range(n)]
boys = [abs(h) for h in heights if h < 0]
girls = [h for h in heights if h > 0]
if boys:
    print("Средний рост мальчиков:", sum(boys)/len(boys))
else:
    print("Мальчиков нет")
if girls:
    print("Средний рост девочек:", sum(girls)/len(girls))
else:
    print("Девочек нет")

# 7.112 (среднее чисел >10, может не быть)
arr = [float(input(f"b[{i+1}]: ")) for i in range(15)]
gt10 = [x for x in arr if x > 10]
if gt10:
    print("Среднее чисел >10:", sum(gt10)/len(gt10))
else:
    print("Чисел >10 нет")

# 7.113 (среднее чисел >n, может не быть)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(12)]
gt_n = [x for x in arr if x > n]
if gt_n:
    print("Среднее чисел > n:", sum(gt_n)/len(gt_n))
else:
    print("Таких чисел нет")

# 7.114 (среднее чётных, может не быть)
arr = [int(input(f"d[{i+1}]: ")) for i in range(14)]
even = [x for x in arr if x % 2 == 0]
if even:
    print("Среднее чётных:", sum(even)/len(even))
else:
    print("Чётных нет")

# 7.115 (среднее кратных n, может не быть)
n = int(input("n: "))
m = int(input("m: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(m)]
mult_n = [x for x in arr if x % n == 0]
if mult_n:
    print("Среднее кратных n:", sum(mult_n)/len(mult_n))
else:
    print("Таких чисел нет")

# 7.116 (средняя стоимость автомобилей >3× средняя мотоциклов)
cars = []
bikes = []
while True:
    price = float(input("Стоимость транспортного средства (0 для конца): "))
    if price == 0:
        break
    if price > 5000:
        cars.append(price)
    else:
        bikes.append(price)
if cars and bikes:
    avg_cars = sum(cars)/len(cars)
    avg_bikes = sum(bikes)/len(bikes)
    print("Средняя стоимость автомобилей >3× средняя мотоциклов?", avg_cars > 3*avg_bikes)
else:
    print("Недостаточно данных")

# 7.117 (средний рост мальчиков > среднего роста девочек +10 см)
n = int(input("Количество учеников: "))
heights = [float(input(f"Рост ученика {i+1} (отрицательный для мальчиков): ")) for i in range(n)]
boys = [abs(h) for h in heights if h < 0]
girls = [h for h in heights if h > 0]
if boys and girls:
    avg_boys = sum(boys)/len(boys)
    avg_girls = sum(girls)/len(girls)
    print("Средний рост мальчиков > среднего роста девочек +10 см?", avg_boys > avg_girls + 10)
else:
    print("Недостаточно данных")

# 7.118 (номер первого и последнего числа 10)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(n)]
first = None
last = None
for i, x in enumerate(arr):
    if x == 10:
        if first is None:
            first = i+1
        last = i+1
if last is not None:
    print("Номер последнего 10:", last)
    print("Номер первого 10:", first if first is not None else "нет")
else:
    print("Чисел 10 нет")

# 7.119 (номер последнего числа >100)
n = int(input("n: "))
arr = [int(input(f"b[{i+1}]: ")) for i in range(n)]
last_index = None
for i, x in enumerate(arr):
    if x > 100:
        last_index = i+1
if last_index is not None:
    print("Номер последнего >100:", last_index)
else:
    print("Таких чисел нет")

# 7.120 (номер последнего числа 25)
n = int(input("n: "))
arr = [int(input(f"c[{i+1}]: ")) for i in range(n)]
last_index = None
for i, x in enumerate(arr):
    if x == 25:
        last_index = i+1
if last_index is not None:
    print("Номер последнего 25:", last_index)
else:
    print("Чисел 25 нет")

# 7.121 (номер последнего отрицательного)
k = int(input("k: "))
arr = [int(input(f"b[{i+1}]: ")) for i in range(k)]
last_index = None
for i, x in enumerate(arr):
    if x < 0:
        last_index = i+1
if last_index is not None:
    print("Номер последнего отрицательного:", last_index)
else:
    print("Отрицательных нет")

# 7.122 (номер последнего числа, оканчивающегося на 12)
m = int(input("m: "))
arr = [int(input(f"x[{i+1}]: ")) for i in range(m)]
last_index = None
for i, x in enumerate(arr):
    if x % 100 == 12:
        last_index = i+1
if last_index is not None:
    print("Номер последнего, оканчивающегося на 12:", last_index)
else:
    print("Таких чисел нет")

# 7.123 (место нового ученика по росту)
heights = sorted([int(input(f"Рост ученика {i+1}: ")) for i in range(15)], reverse=True)
new_height = int(input("Рост нового ученика: "))
position = 1
for h in heights:
    if new_height > h:
        break
    position += 1
print("Новый ученик займёт место:", position)

# 7.124 (место команды по очкам)
points = sorted([int(input(f"Очки команды {i+1}: ")) for i in range(20)], reverse=True)
N = int(input("Очки искомой команды: "))
place = points.index(N) + 1
print("Команда заняла место:", place)

# 7.125 (анализ упорядоченной последовательности)
arr = sorted([float(input(f"y[{i+1}]: ")) for i in range(15)])
n = float(input("n (не равное ни одному элементу): "))
# а) сумма чисел < n
sum_lt = sum(x for x in arr if x < n)
print("Сумма чисел < n:", sum_lt)
# б) два элемента, между которыми находится n
for i in range(len(arr)-1):
    if arr[i] < n < arr[i+1]:
        print(f"n между элементами {i+1} ({arr[i]}) и {i+2} ({arr[i+1]})")
        break

# 7.126 (первое отрицательное число)
arr = [float(input(f"a[{i+1}]: ")) for i in range(15)]
for i, x in enumerate(arr):
    if x < 0:
        print(f"Первое отрицательное на индексе {i}")
        break
else:
    print("Отрицательных нет")

# 7.127 (первое число 666)
arr = []
while True:
    num = int(input("Введите число (100 для конца): "))
    if num == 100:
        break
    arr.append(num)
for i, x in enumerate(arr):
    if x == 666:
        print(f"Первое 666 на индексе {i}")
        break
else:
    print("Чисел 666 нет")

# 7.128 (первое число, оканчивающееся на 7)
arr = [int(input(f"b[{i+1}]: ")) for i in range(12)]
for i, x in enumerate(arr):
    if x % 10 == 7:
        print(f"Первое число, оканчивающееся на 7, на индексе {i}")
        break
else:
    print("Таких чисел нет")

# 7.129 (первое число, кратное 7)
arr = []
while True:
    num = int(input("Введите число (-1 для конца): "))
    if num == -1:
        break
    arr.append(num)
for i, x in enumerate(arr):
    if x % 7 == 0:
        print(f"Первое кратное 7 на индексе {i}")
        break
else:
    print("Кратных 7 нет")

# 7.130 (количество повторений в неубывающей последовательности)
arr = sorted([int(input(f"Число {i+1}: ")) for i in range(20)])
repeats = 0
i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr) and arr[j] == arr[i]:
        j += 1
    if j - i > 1:
        repeats += j - i
    i = j
print("Количество повторений:", repeats)

# 7.131 (количество подряд идущих равных чисел)
arr = sorted([int(input(f"Число {i+1}: ")) for i in range(20)])
max_count = 0
i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr) and arr[j] == arr[i]:
        j += 1
    max_count = max(max_count, j - i)
    i = j
print("Максимальное количество подряд идущих равных:", max_count)

# 7.132 (количество различных чисел)
arr = sorted([int(input(f"Число {i+1}: ")) for i in range(30)])
different = 1
for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        different += 1
print("Количество различных чисел:", different)

# 7.133 (количество подряд идущих равных, конец 1000)
arr = []
while True:
    num = float(input("Введите число (1000 для конца): "))
    if num == 1000:
        break
    arr.append(num)
arr.sort()
max_count = 0
i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr) and arr[j] == arr[i]:
        j += 1
    max_count = max(max_count, j - i)
    i = j
print("Максимальное количество подряд идущих равных:", max_count)

# 7.134 (количество различных в невозрастающей последовательности)
arr = []
while True:
    num = float(input("Введите число (0 для конца): "))
    if num == 0:
        break
    arr.append(num)
# Проверяем, что последовательность невозрастающая
is_non_increasing = all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
if not is_non_increasing:
    print("Последовательность не является невозрастающей!")
else:
    different = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            different += 1
    print("Количество различных чисел:", different)

# 7.135 (максимальное и минимальное)
n = int(input("n: "))
arr = [float(input(f"x[{i+1}]: ")) for i in range(n)]
print("Максимум:", max(arr))
print("Минимум:", min(arr))
# в одном цикле
max_val = min_val = arr[0]
for x in arr[1:]:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x
print("Максимум (один цикл):", max_val)
print("Минимум (один цикл):", min_val)

# 7.136 (лучший результат лыжников)
best = float('inf')
while True:
    time = float(input("Время спортсмена (0 для конца): "))
    if time == 0:
        break
    if time < best:
        best = time
    print("Текущий лучший результат:", best)

# 7.137 (самый удалённый город от Москвы)
n = int(input("Количество городов: "))
max_dist = 0
for i in range(n):
    dist = float(input(f"Расстояние до города {i+1}: "))
    if dist > max_dist:
        max_dist = dist
print("Расстояние до самого удалённого города:", max_dist)

# 7.138 (максимальная температура месяца)
days = int(input("Количество дней: "))
temps = [float(input(f"Температура дня {i+1}: ")) for i in range(days)]
print("Максимальная температура:", max(temps))

# 7.139 (максимальная скорость автомобиля)
n = 20
speeds = [float(input(f"Максимальная скорость автомобиля {i+1}: ")) for i in range(n)]
print("Самая быстрая скорость:", max(speeds))

# 7.140 (радиус самого маленького круга)
import math
n = int(input("Количество кругов: "))
min_radius = float('inf')
for i in range(n):
    area = float(input(f"Площадь круга {i+1}: "))
    radius = math.sqrt(area / math.pi)
    if radius < min_radius:
        min_radius = radius
print("Радиус самого маленького круга:", min_radius)

# 7.141 (диагональ самого большого квадрата)
import math
n = int(input("Количество квадратов: "))
max_diag = 0
for i in range(n):
    area = float(input(f"Площадь квадрата {i+1}: "))
    side = math.sqrt(area)
    diag = side * math.sqrt(2)
    if diag > max_diag:
        max_diag = diag
print("Диагональ самого большого квадрата:", max_diag)

# 7.142 (максимальная плотность)
n = 20
max_density = 0
for i in range(n):
    mass = float(input(f"Масса тела {i+1} (кг): "))
    volume = float(input(f"Объём тела {i+1} (см³): ")) / 1e6  # в м³
    density = mass / volume
    if density > max_density:
        max_density = density
print("Максимальная плотность:", max_density, "кг/м³")

# 7.143 (минимальная плотность населения)
n = 16
min_density = float('inf')
for i in range(n):
    population = float(input(f"Население государства {i+1} (млн): "))
    area = float(input(f"Площадь государства {i+1} (тыс. км²): "))
    density = population / area
    if density < min_density:
        min_density = density
print("Минимальная плотность населения:", min_density, "млн/тыс. км²")

# 7.144 (максимальная сумма и минимальное произведение в парах)
n = int(input("n: "))
max_sum = -float('inf')
min_product = float('inf')
for i in range(n):
    a, b = map(float, input(f"Пара {i+1}: ").split())
    max_sum = max(max_sum, a + b)
    min_product = min(min_product, a * b)
print("Максимальная сумма в паре:", max_sum)
print("Минимальное произведение в паре:", min_product)

# 7.145 (оценка фигуриста)
n = int(input("Количество судей: "))
scores = [float(input(f"Оценка судьи {i+1}: ")) for i in range(n)]
scores.sort()
if n > 2:
    scores = scores[1:-1]  # удаляем мин и макс
print("Итоговая оценка:", sum(scores) / len(scores))

# 7.146 (разница между самым высоким и самым низким)
n = int(input("Количество людей: "))
heights = [float(input(f"Рост человека {i+1}: ")) for i in range(n)]
print("Разница:", max(heights) - min(heights))

# 7.147 (разница в количестве учеников)
n = 20
students = [int(input(f"Учеников в классе {i+1}: ")) for i in range(n)]
print("Разница:", max(students) - min(students))

# 7.148 (максимум превышает минимум не более чем на 25)
n = int(input("n: "))
arr = [int(input(f"a[{i+1}]: ")) for i in range(n)]
print("Максимум превышает минимум ≤25?", max(arr) - min(arr) <= 25)

# 7.149 (масса самого тяжелого >2× масса самого лёгкого)
n = int(input("Количество людей: "))
masses = [float(input(f"Масса человека {i+1}: ")) for i in range(n)]
print("Самый тяжёлый >2× самого лёгкого?", max(masses) > 2 * min(masses))

# 7.150 (наибольшая длина отрезка из чётных чисел)
n = int(input("n: "))
arr = [int(input(f"d[{i+1}]: ")) for i in range(n)]
max_len = 0
curr_len = 0
for x in arr:
    if x % 2 == 0:
        curr_len += 1
        max_len = max(max_len, curr_len)
    else:
        curr_len = 0
print("Наибольшая длина отрезка из чётных:", max_len)

# 8.1 (числа 1,4,9,... не превышающие n)
n = int(input("n: "))
i = 1
while i**2 <= n:
    print(i**2, end=' ')
    i += 1
print()

# 8.2 (первое число 1,4,9,... больше n)
n = int(input("n: "))
# Способ 1: с условием
i = 1
while i**2 <= n:
    i += 1
print("Первое число > n (способ 1):", i**2)
# Способ 2: без условия
for i in range(1, n+2):  # n+2 чтобы гарантированно найти
    if i**2 > n:
        print("Первое число > n (способ 2):", i**2)
        break

# 8.3 (числа 1, 1/2, 1/3,... не меньше a)
a = float(input("a (0<a≤1): "))
i = 1
while 1/i >= a:
    print(1/i, end=' ')
    i += 1
print()

# 8.4 (первое число 1, 1/2, 1/3,... меньше a)
a = float(input("a (0<a≤1): "))
i = 1
while 1/i >= a:
    i += 1
print("Первое число < a:", 1/i)

# 8.5 (числа 1+1/2, 1+1/3,... не меньше a)
a = float(input("a (1<a≤1.5): "))
i = 2
while 1 + 1/i >= a:
    print(1 + 1/i, end=' ')
    i += 1
print()

# 8.6 (то же, другой способ)
a = float(input("a (1<a≤1.5): "))
for i in range(2, 1000):
    val = 1 + 1/i
    if val >= a:
        print(val, end=' ')
    else:
        break
print()

# 8.7 (первое число 1+1/2, 1+1/3,... меньше a)
a = float(input("a (1<a≤1.5): "))
i = 2
while 1 + 1/i >= a:
    i += 1
print("Первое число < a:", 1 + 1/i)

# 8.8 (все n, при которых 1+1/n ≥ a)
a = float(input("a (1<a≤1.5): "))
for n in range(2, 1000):
    if 1 + 1/n >= a:
        print(n, end=' ')
    else:
        break
print()

# 8.9 (наименьшее n, при котором 1+1/n < a)
a = float(input("a (1<a≤1.5): "))
n = 2
while 1 + 1/n >= a:
    n += 1
print("Наименьшее n:", n)

# 8.10 (числа 1, 1+1/2, 1+1/3,... меньше a)
a = float(input("a: "))
i = 1
val = 1
while val < a:
    print(val, end=' ')
    i += 1
    val = 1 + 1/i
print()

# 8.11 (первое число 1, 1+1/2, 1+1/2+1/3,... больше n)
n = float(input("n: "))
total = 1
i = 1
while total <= n:
    i += 1
    total += 1/i
print("Первое число > n:", total)

# 8.12 (все n, при которых сумма 1+1/2+...+1/n > a)
a = float(input("a: "))
total = 0
i = 0
while total <= a:
    i += 1
    total += 1/i
    if total > a:
        print(i, end=' ')
print()

# 8.13 (наименьшее n, при котором сумма > a)
a = float(input("a: "))
total = 0
i = 0
while total <= a:
    i += 1
    total += 1/i
print("Наименьшее n:", i)

# 8.14 (первое число 1, 1/2, 1/3,... меньше a, разные способы)
a = float(input("a (0<a≤1): "))
# Способ 1
i = 1
while 1/i >= a:
    i += 1
print("Первое число < a (способ 1):", 1/i)
# Способ 2
for i in range(1, 1000):
    if 1/i < a:
        print("Первое число < a (способ 2):", 1/i)
        break

# 8.15 (последовательность y = (x^2+100)/(x+200))
m = float(input("m (0.52≤m≤33.7): "))
x = 1
while x <= 100:
    y = (x**2 + 100) / (x + 200)
    if y < m:
        print(y, end=' ')
    x += 1
print()

# 8.16 (последовательность 1/2, 2/3, 3/4,...)
m = float(input("m (0.5<m<1): "))
i = 1
while i/(i+1) < m:
    print(i/(i+1), end=' ')
    i += 1
print()

# 8.17 (последовательность дробей с суммированием числителей/знаменателей)
eps = 0.001
num1, num2 = 1, 2
den1, den2 = 1, 1
prev = num1/den1
curr = num2/den2
i = 2
while abs(curr - prev) > eps:
    i += 1
    num1, num2 = num2, num1 + num2
    den1, den2 = den2, den1 + den2
    prev, curr = curr, num2/den2
print(f"Первый член, отличающийся от предыдущего ≤ {eps}: {curr}")

# 8.18 (последовательность y_i)
import math
a = float(input("a>0: "))
x = float(input("x>0: "))
eps = float(input("ε>0: "))
y_prev = a
y_curr = 0.5 * (y_prev + x/(y_prev-1))
i = 1
while abs(y_curr**2 - y_prev**2) >= eps:
    y_prev, y_curr = y_curr, 0.5 * (y_curr + x/(y_curr-1))
    i += 1
print(f"Первый член y_{i} = {y_curr}")

# 8.19 (сумма чисел Фибоначчи ≤1000)
fib1, fib2 = 1, 1
total = 0
while fib1 <= 1000:
    total += fib1
    fib1, fib2 = fib2, fib1 + fib2
print("Сумма чисел Фибоначчи ≤1000:", total)

# 8.19б (первое число Фибоначчи > n)
n = int(input("n>1: "))
fib1, fib2 = 1, 1
while fib1 <= n:
    fib1, fib2 = fib2, fib1 + fib2
print("Первое число Фибоначчи > n:", fib1)

# 9.1а (таблица из 8)
for i in range(5):
    for j in range(3):
        print(8, end=' ')
    print()

# 9.1б (таблица чисел от 1 до 7)
for i in range(1, 8):
    for j in range(5):
        print(i, end=' ')
    print()

# 9.1в (таблица 10,20,...,80)
for i in range(1, 9):
    for j in range(4):
        print(i*10, end=' ')
    print()

# 9.1г (таблица 12,22,...,82)
for i in range(1, 9):
    for j in range(4):
        print(i*10+2, end=' ')
    print()

# 9.1д (таблица чисел 2..20 по строкам)
for i in range(5):
    for j in range(2, 21):
        print(j, end=' ')
    print()

# 9.1е (таблица чисел 15..3 по строкам)
for i in range(4):
    for j in range(15, 2, -1):
        print(j, end=' ')
    print()

# 9.1ж (треугольник из нулей)
for i in range(6, 0, -1):
    for j in range(i):
        print(0, end=' ')
    print()

# 9.1з (убывающие строки)
for i in range(8, 0, -1):
    for j in range(8, 8-i, -1):
        print(j, end=' ')
    print()

# 9.1и (треугольник чисел)
for i in range(2, 11):
    for j in range(i, 11):
        print(j, end=' ')
    print()

# 9.1й (треугольник 2, 2 3, 2 3 4,...)
for i in range(2, 11):
    for j in range(2, i+1):
        print(j, end=' ')
    print()

# 9.1к (треугольник из повторяющихся чисел)
for i in range(3, 7):
    for j in range(i):
        print(i, end=' ')
    print()

# 9.1л (треугольник 21, 22 22, ...)
for i in range(21, 26):
    for j in range(i-20):
        print(i, end=' ')
    print()

# 9.1м (убывающий треугольник)
for i in range(1, 6):
    for j in range(9-i):
        print(i, end=' ')
    print()

# 9.1н (треугольник из десятков)
for i in range(1, 6):
    for j in range(i):
        print(i*10, end=' ')
    print()

# 9.1о (треугольник 5..9)
for i in range(5, 10):
    for j in range(10-i):
        print(i, end=' ')
    print()

# 9.1п (таблица умножения 5,10,...,25)
for i in range(5, 30, 5):
    for j in range(5):
        print(i, end=' ')
    print()

# 9.1р (таблица чисел 101..165)
for i in range(101, 166, 10):
    for j in range(5):
        print(i+j, end=' ')
    print()

# 9.1с (таблица 51..58, 41..48,...)
for i in range(51, 20, -10):
    for j in range(8):
        print(i+j, end=' ')
    print()

# 9.2а (таблица сложения по строкам)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} + {j} = {i+j}", end='   ')
    print()

# 9.2б (таблица сложения по столбцам)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} + {i} = {i+j}", end='   ')
    print()

# 9.3а (таблица умножения по строкам)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end='   ')
    print()

# 9.3б (таблица умножения по столбцам)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j} * {i} = {i*j}", end='   ')
    print()

# 9.4 (ввод оценок 12 учеников по 3 предметам)
# Способ 1: по строкам
total = 0
for student in range(12):
    for subject in range(3):
        grade = int(input(f"Ученик {student+1}, предмет {subject+1}: "))
        total += grade
print("Сумма всех оценок (способ 1):", total)

# Способ 2: по столбцам
total = 0
for subject in range(3):
    for student in range(12):
        grade = int(input(f"Предмет {subject+1}, ученик {student+1}: "))
        total += grade
print("Сумма всех оценок (способ 2):", total)

# 9.5 (зарплата за квартал)
employees = 12
months = 3
salaries = [[0]*months for _ in range(employees)]

# Ввод данных
for emp in range(employees):
    for month in range(months):
        salaries[emp][month] = float(input(f"Зарплата работника {emp+1} за месяц {month+1}: "))

# а) общая сумма за квартал
total_all = sum(sum(row) for row in salaries)
print("Общая сумма за квартал:", total_all)

# б) зарплата каждого за квартал
for emp in range(employees):
    total_emp = sum(salaries[emp])
    print(f"Работник {emp+1}: {total_emp}")

# в) общая зарплата за каждый месяц
for month in range(months):
    total_month = sum(salaries[emp][month] for emp in range(employees))
    print(f"Месяц {month+1}: {total_month}")

# 9.6 (соревнования по фигурному катанию)
sportsmen = 15
programs = 3
scores = [[0]*programs for _ in range(sportsmen)]

# Ввод
for sp in range(sportsmen):
    for prog in range(programs):
        scores[sp][prog] = float(input(f"Спортсмен {sp+1}, программа {prog+1}: "))

# а) среднее каждого спортсмена
for sp in range(sportsmen):
    avg = sum(scores[sp]) / programs
    print(f"Спортсмен {sp+1}: {avg:.2f}")

# б) среднее по каждой программе
for prog in range(programs):
    avg = sum(scores[sp][prog] for sp in range(sportsmen)) / sportsmen
    print(f"Программа {prog+1}: {avg:.2f}")

# 9.7 (оценки 15 учеников по 3 предметам)
students = 15
subjects = 3
grades = [[0]*subjects for _ in range(students)]

# Ввод
for st in range(students):
    for sub in range(subjects):
        grades[st][sub] = int(input(f"Ученик {st+1}, предмет {sub+1}: "))

# а) общее количество пятёрок
count5 = sum(1 for row in grades for g in row if g == 5)
print("Пятёрок в таблице:", count5)

# б) количество троек у каждого ученика
for st in range(students):
    count3 = grades[st].count(3)
    print(f"Ученик {st+1}: троек {count3}")

# в) количество двоек по каждому предмету
for sub in range(subjects):
    count2 = sum(1 for st in range(students) if grades[st][sub] == 2)
    print(f"Предмет {sub+1}: двоек {count2}")

# 9.8 (оценки студентов)
students = 14
subjects = 3
grades = [[0]*subjects for _ in range(students)]

# Ввод
for st in range(students):
    for sub in range(subjects):
        grades[st][sub] = int(input(f"Студент {st+1}, предмет {sub+1}: "))

# а) студентов без двоек
count_no2 = sum(1 for st in range(students) if 2 not in grades[st])
print("Студентов без двоек:", count_no2)

# б) предметы только с 5 и 4
count_subjects = 0
for sub in range(subjects):
    all_4_5 = all(grades[st][sub] in (4,5) for st in range(students))
    if all_4_5:
        count_subjects += 1
print("Предметов только с 4 и 5:", count_subjects)

# в) количество двоек по каждому предмету
for sub in range(subjects):
    count2 = sum(1 for st in range(students) if grades[st][sub] == 2)
    print(f"Предмет {sub+1}: двоек {count2}")

# 9.9 (пятиборье)
sportsmen = 8
sports = 5
scores = [[0]*sports for _ in range(sportsmen)]

# Ввод
for sp in range(sportsmen):
    for sport in range(sports):
        scores[sp][sport] = int(input(f"Спортсмен {sp+1}, вид {sport+1}: "))

# а) максимальная оценка
max_score = max(max(row) for row in scores)
print("Максимальная оценка:", max_score)

# б) баллы победителя (сумма)
winner_score = max(sum(row) for row in scores)
print("Баллы победителя:", winner_score)

# 9.10 (зарплата за квартал, поиск максимумов)
employees = 12
months = 3
salaries = [[0]*months for _ in range(employees)]

# Ввод
for emp in range(employees):
    for month in range(months):
        salaries[emp][month] = float(input(f"Работник {emp+1}, месяц {month+1}: "))

# а) максимальная зарплата
max_salary = max(max(row) for row in salaries)
print("Максимальная зарплата:", max_salary)

# б) работник с наибольшей суммой
max_emp = max(range(employees), key=lambda i: sum(salaries[i]))
print(f"Работник с наибольшей суммой: {max_emp+1}")

# в) месяц с наибольшей общей суммой
month_totals = [sum(salaries[emp][month] for emp in range(employees)) for month in range(months)]
max_month = month_totals.index(max(month_totals))
print(f"Месяц с наибольшей общей суммой: {max_month+1}")

# 9.11 (для каждого работника и месяца максимум)
for emp in range(employees):
    max_month = max(range(months), key=lambda m: salaries[emp][m])
    print(f"Работник {emp+1}: наибольшая зарплата в месяце {max_month+1}")

for month in range(months):
    max_emp = max(range(employees), key=lambda e: salaries[e][month])
    print(f"Месяц {month+1}: наибольшая зарплата у работника {max_emp+1}")

# 9.12 (ученики в параллелях)
parallels = 11
classes = 4
students = [[0]*classes for _ in range(parallels)]

# Ввод (примерные данные, можно раскомментировать ввод)
# for p in range(parallels):
#     for c in range(classes):
#         students[p][c] = int(input(f"Параллель {p+1}, класс {chr(ord('A')+c)}: "))
# Заполним тестовыми данными
import random
for p in range(parallels):
    for c in range(classes):
        students[p][c] = random.randint(20, 30)

# а) самый малочисленный класс
min_class = min(min(row) for row in students)
print("Самый малочисленный класс:", min_class)

# б) минимальное количество учеников в параллели
min_parallel = min(sum(row) for row in students)
print("Минимальное количество в параллели:", min_parallel)

# в) минимальное количество учеников в классах A,Б,В,Г
for c in range(classes):
    total = sum(students[p][c] for p in range(parallels))
    print(f"Класс {chr(ord('A')+c)}: всего {total}")

# 9.13 (самый малочисленный класс в каждой параллели и в каждом буквенном классе)
# а) в каждой параллели
for p in range(parallels):
    min_in_parallel = min(students[p])
    print(f"Параллель {p+1}: самый малочисленный класс {min_in_parallel} чел.")

# б) среди классов с каждой буквой
for c in range(classes):
    min_in_class = min(students[p][c] for p in range(parallels))
    print(f"Класс {chr(ord('A')+c)}: самый малочисленный {min_in_class} чел.")

# 9.14 (доход магазинов)
shops = 3
days = 10
income = [[0]*days for _ in range(shops)]

# Ввод
for s in range(shops):
    for d in range(days):
        income[s][d] = float(input(f"Магазин {s+1}, день {d+1}: "))

# а) магазин с максимальным общим доходом
total_by_shop = [sum(income[s]) for s in range(shops)]
best_shop = total_by_shop.index(max(total_by_shop))
print(f"Магазин с максимальным доходом: {best_shop+1}")

# б) день с максимальным общим доходом
total_by_day = [sum(income[s][d] for s in range(shops)) for d in range(days)]
best_day = total_by_day.index(max(total_by_day))
print(f"День с максимальным доходом: {best_day+1}")

# в) магазин и день с максимальным дневным доходом
max_inc = max(max(row) for row in income)
for s in range(shops):
    for d in range(days):
        if income[s][d] == max_inc:
            print(f"Максимальный доход: магазин {s+1}, день {d+1}")
            break
    else:
        continue
    break

# 9.15 (для каждого магазина и дня максимум)
for s in range(shops):
    best_day = max(range(days), key=lambda d: income[s][d])
    print(f"Магазин {s+1}: лучший день {best_day+1}")

for d in range(days):
    best_shop = max(range(shops), key=lambda s: income[s][d])
    print(f"День {d+1}: лучший магазин {best_shop+1}")

# 9.16 (студенты по курсам и группам)
courses = 5
groups = 6
students = [[0]*groups for _ in range(courses)]

# Ввод
for c in range(courses):
    for g in range(groups):
        students[c][g] = int(input(f"Курс {c+1}, группа {g+1}: "))

# а) курс с наименьшим количеством студентов
total_by_course = [sum(students[c]) for c in range(courses)]
min_course = total_by_course.index(min(total_by_course))
print(f"Курс с наименьшим количеством студентов: {min_course+1}")

# б) самая малочисленная группа
min_students = min(min(row) for row in students)
for c in range(courses):
    for g in range(groups):
        if students[c][g] == min_students:
            print(f"Самая малочисленная группа: курс {c+1}, группа {g+1}")
            break
    else:
        continue
    break

# в) самая малочисленная группа на каждом курсе
for c in range(courses):
    min_in_course = min(students[c])
    group_index = students[c].index(min_in_course)
    print(f"Курс {c+1}: самая малочисленная группа {group_index+1}")

# 9.17 (доход от товаров)
goods = 5
days = 6
prices = [float(input(f"Цена товара {i+1}: ")) for i in range(goods)]
quantities = [[0]*days for _ in range(goods)]

# Ввод количества
for g in range(goods):
    for d in range(days):
        quantities[g][d] = int(input(f"Товар {g+1}, день {d+1}: "))

# а) общий доход от каждого вида товара
for g in range(goods):
    total = sum(quantities[g][d] * prices[g] for d in range(days))
    print(f"Товар {g+1}: доход {total}")

# б) общий доход за каждый день
for d in range(days):
    total = sum(quantities[g][d] * prices[g] for g in range(goods))
    print(f"День {d+1}: доход {total}")

# в) общий доход за 6 дней
total_all = sum(quantities[g][d] * prices[g] for g in range(goods) for d in range(days))
print("Общий доход за 6 дней:", total_all)

# г) товар с максимальным общим доходом
income_by_good = [sum(quantities[g][d] * prices[g] for d in range(days)) for g in range(goods)]
best_good = income_by_good.index(max(income_by_good))
print(f"Товар с максимальным доходом: {best_good+1}")

# д) день с максимальным общим доходом
income_by_day = [sum(quantities[g][d] * prices[g] for g in range(goods)) for d in range(days)]
best_day = income_by_day.index(max(income_by_day))
print(f"День с максимальным доходом: {best_day+1}")

# е) дни с доходом > a
a = float(input("Порог a: "))
count_days = sum(1 for income in income_by_day if income > a)
print(f"Дней с доходом > {a}: {count_days}")

# 9.18 (лучшая группа по среднему баллу)
groups = 3
students_per_group = 20
exams = 3

best_group = None
best_avg = 0

for g in range(groups):
    print(f"Группа {g+1}:")
    total_group = 0
    for s in range(students_per_group):
        total_student = sum(int(input(f"Студент {s+1}, экзамен {e+1}: ")) for e in range(exams))
        total_group += total_student
    avg_group = total_group / (students_per_group * exams)
    print(f"Средний балл группы {g+1}: {avg_group:.2f}")
    if avg_group > best_avg:
        best_avg = avg_group
        best_group = g+1

print(f"Лучшая группа: {best_group} со средним баллом {best_avg:.2f}")

# 9.19 (количество делителей чисел от 120 до 140)
for num in range(120, 141):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    print(f"{num}: {count} делителей")

# 9.20 (графическое изображение делимости)
n = int(input("n: "))
for num in range(1, n+1):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    print(f"{num} {'+' * count}")

# 9.21 (числа с ровно 5 делителями)
for num in range(1, 301):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    if count == 5:
        print(num, end=' ')
print()

# 9.22 (числа с ровно 6 делителями от 200 до 500)
for num in range(200, 501):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    if count == 6:
        print(num, end=' ')
print()

# 9.23 (числа с k делителями от a до b)
a = int(input("a: "))
b = int(input("b: "))
k = int(input("k: "))
for num in range(a, b+1):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    if count == k:
        print(num, end=' ')
print()

# 9.24 (число с максимальным количеством делителей)
a = int(input("a: "))
b = int(input("b: "))
max_div = 0
max_num = a
for num in range(a, b+1):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    if count > max_div:
        max_div = count
        max_num = num
print(f"Число с максимальным количеством делителей: {max_num} ({max_div} делителей)")

# 9.25 (трёхзначные простые числа)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for num in range(100, 1000):
    if is_prime(num):
        print(num, end=' ')
print()

# 9.26 (первые 100 простых чисел)
primes = []
num = 2
while len(primes) < 100:
    if is_prime(num):
        primes.append(num)
    num += 1
print("Первые 100 простых чисел:", primes)

# 9.27 (сумма делителей чисел от 50 до 70)
for num in range(50, 71):
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            total += i
    print(f"{num}: сумма делителей {total}")

# 9.28 (числа от 100 до 300 с суммой делителей 50)
for num in range(100, 301):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == 50:
        print(num, end=' ')
print()

# 9.29 (числа от 300 до 600 с суммой делителей кратной 10)
for num in range(300, 601):
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            total += i
    if total % 10 == 0:
        print(num, end=' ')
print()

# 9.30 (трёхзначное совершенное число)
for num in range(100, 1000):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        print("Трёхзначное совершенное число:", num)
        break

# 9.31 (все совершенные числа <100000)
for num in range(2, 100000):
    total = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            total += i
            if i != 1 and i != num // i:
                total += num // i
    if total == num:
        print(num, end=' ')
print()

# 9.32 (число с максимальной суммой делителей от a до b)
a = int(input("a: "))
b = int(input("b: "))
max_sum = 0
best_num = a
for num in range(a, b+1):
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            total += i
    if total > max_sum:
        max_sum = total
        best_num = num
print(f"Число с максимальной суммой делителей: {best_num} (сумма {max_sum})")

# 9.33 (дружественные числа <50000)
def sum_of_divisors(n):
    total = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            total += i
            if i != 1 and i != n // i:
                total += n // i
    return total

for a in range(1, 50000):
    b = sum_of_divisors(a)
    if b > a and sum_of_divisors(b) == a:
        print(f"Дружественная пара: {a} и {b}")

# 9.34 (способы выплаты n рублей)
n = int(input("n (<100): "))
count = 0
# a) количество способов
for r10 in range(n//10 + 1):
    for r5 in range((n - r10*10)//5 + 1):
        remaining = n - r10*10 - r5*5
        if remaining >= 0:
            # оставшиеся можно выплатить монетами 1 и 2 рубля
            for r2 in range(remaining//2 + 1):
                r1 = remaining - r2*2
                if r1 >= 0:
                    count += 1
print("Количество способов выплаты:", count)

# б) все способы
print("Все способы (10р 5р 2р 1р):")
for r10 in range(n//10 + 1):
    for r5 in range((n - r10*10)//5 + 1):
        remaining = n - r10*10 - r5*5
        if remaining >= 0:
            for r2 in range(remaining//2 + 1):
                r1 = remaining - r2*2
                if r1 >= 0:
                    print(f"10р:{r10} 5р:{r5} 2р:{r2} 1р:{r1}")

# 9.35 (выплата сумм n..n+10 минимальным количеством купюр)
denominations = [64, 32, 16, 8, 4, 2, 1]
for amount in range(n, n+11):
    print(f"\nСумма {amount}:")
    temp = amount
    for d in denominations:
        count = temp // d
        if count > 0:
            print(f"  {d}: {count}")
            temp -= count * d

# 9.36 (прямоугольники с площадью s)
s = int(input("s: "))
print("Прямоугольники с площадью", s)
# а) разные
for a in range(1, s+1):
    if s % a == 0:
        b = s // a
        print(f"{a} x {b}")
# б) совпадающие (только a ≤ b)
for a in range(1, int(s**0.5)+1):
    if s % a == 0:
        b = s // a
        if a <= b:
            print(f"{a} x {b}")

# 9.37 (параллелепипеды с объёмом v)
v = int(input("v: "))
print("Параллелепипеды с объёмом", v)
# а) разные
for a in range(1, v+1):
    if v % a == 0:
        v_rest = v // a
        for b in range(1, v_rest+1):
            if v_rest % b == 0:
                c = v_rest // b
                print(f"{a} x {b} x {c}")
# б) совпадающие (a ≤ b ≤ c)
for a in range(1, int(v**(1/3))+1):
    if v % a == 0:
        v_rest = v // a
        for b in range(a, int(v_rest**0.5)+1):
            if v_rest % b == 0:
                c = v_rest // b
                if b <= c:
                    print(f"{a} x {b} x {c}")

# 9.38 (натуральные решения x² + y² = k²)
for x in range(1, 31):
    for y in range(x, 31):  # чтобы избежать перестановок
        k2 = x**2 + y**2
        k = int(k2**0.5)
        if k <= 30 and k**2 == k2:
            print(f"{x}² + {y}² = {k}²")

# 9.39 (сумма 1^n + 2^n + ... + m^n)
m = int(input("m: "))
n = int(input("n: "))
total = sum(i**n for i in range(1, m+1))
print(f"1^{n} + 2^{n} + ... + {m}^{n} = {total}")

# 9.40 (сумма 1^1 + 2^2 + ... + n^n)
n = int(input("n: "))
total = sum(i**i for i in range(1, n+1))
print(f"1^1 + 2^2 + ... + {n}^{n} = {total}")

# 9.41 (трёхзначные числа с суммой цифр = n)
n = int(input("n (≤27): "))
for num in range(100, 1000):
    # без операций деления
    digits = [int(d) for d in str(num)]
    if sum(digits) == n:
        print(num, end=' ')
print()

# 9.42 (трёхзначные числа без одинаковых цифр)
for num in range(100, 1000):
    digits = str(num)
    if len(set(digits)) == 3:
        print(num, end=' ')
print()

# 9.43 (НОД нескольких чисел)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input("Количество чисел: "))
nums = [int(input(f"Число {i+1}: ")) for i in range(n)]
result = nums[0]
for num in nums[1:]:
    result = gcd(result, num)
print("НОД всех чисел:", result)

# 9.44 (способы составить вес v грамм гирями)
weights = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
v = int(input("v: "))
count = 0
# Перебор всех подмножеств (2^10 = 1024 вариантов)
for mask in range(1 << len(weights)):
    total = 0
    for i in range(len(weights)):
        if mask & (1 << i):
            total += weights[i]
    if total == v:
        count += 1
print(f"Способов составить вес {v} г: {count}")

# 9.45 (числа, квадрат суммы цифр которых равен m)
m = int(input("m: "))
n = int(input("n: "))
for num in range(1, n):
    s = sum(int(d) for d in str(num))
    if s**2 == m:
        print(num, end=' ')
print()

# 9.46 (цифровой корень)
num = int(input("Число: "))
while num >= 10:
    num = sum(int(d) for d in str(num))
print("Цифровой корень:", num)

# 9.47 (старинная задача: быки, коровы, телята)
print("Решение: быки - 10 руб, коровы - 5 руб, телята - 0.5 руб, всего 100 голов на 100 руб")
for bulls in range(1, 11):  # максимум 10 быков
    for cows in range(1, 20):  # максимум 19 коров
        calves = 100 - bulls - cows
        if calves > 0:
            if bulls*10 + cows*5 + calves*0.5 == 100:
                print(f"Быков: {bulls}, коров: {cows}, телят: {calves}")

# 9.48 (разложение на простые множители)
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

n = int(input("n: "))
factors = prime_factors(n)
# 1) каждый множитель один раз
unique = list(set(factors))
print("Уникальные простые множители:", unique)
# 2) с учётом кратности
print("Разложение с кратностью:", factors)

# 9.49 (все простые делители числа)
n = int(input("n: "))
divisors = []
for i in range(2, n+1):
    if n % i == 0 and is_prime(i):
        divisors.append(i)
print("Простые делители:", divisors)

# 9.50 (числа, взаимно простые с n)
n = int(input("n: "))
for i in range(1, n):
    if gcd(i, n) == 1:
        print(i, end=' ')
print()

# 9.51 (числа, взаимно простые с p)
p = int(input("p: "))
for i in range(1, n):
    if gcd(i, p) == 1:
        print(i, end=' ')
print()

# 9.52 (делители q, взаимно простые с p)
q = int(input("q: "))
p = int(input("p: "))
for i in range(1, q+1):
    if q % i == 0 and gcd(i, p) == 1:
        print(i, end=' ')
print()

# 9.53 (наименьшее число, представимое двумя способами как сумма кубов)
found = False
num = 1
while not found:
    ways = []
    for a in range(1, int(num**(1/3))+1):
        for b in range(a, int(num**(1/3))+1):
            if a**3 + b**3 == num:
                ways.append((a, b))
    if len(ways) >= 2:
        print(f"Наименьшее число: {num}")
        for a, b in ways:
            print(f"  {a}³ + {b}³")
        found = True
    num += 1

# 9.54 (простые несократимые дроби между 0 и 1, знаменатель ≤7)
print("Простые дроби между 0 и 1, знаменатель ≤7:")
for den in range(2, 8):
    for num in range(1, den):
        if gcd(num, den) == 1:
            print(f"{num}/{den}", end=' ')
print()

import random
import math

# 10.1 (случайные вещественные числа)
# а) 8 чисел от 0 до 1
print("10.1а:", [random.random() for _ in range(8)])
# б) k чисел от 0 до 1
k = int(input("k: "))
print("10.1б:", [random.random() for _ in range(k)])
# в) 15 чисел от 25 до 26
print("10.1в:", [25 + random.random() for _ in range(15)])
# г) 20 чисел от 0 до 15
print("10.1г:", [random.random()*15 for _ in range(20)])
# д) случайное k ≤ a, и k чисел от 0 до b
a = int(input("a: "))
b = float(input("b: "))
k = random.randint(1, a)
print(f"10.1д: k={k}, числа:", [random.random()*b for _ in range(k)])
# е) 10 чисел от -40 до 40
print("10.1е:", [random.uniform(-40, 40) for _ in range(10)])
# ж) случайное k ≤ m, и k чисел от a до b
m = int(input("m: "))
a = float(input("a: "))
b = float(input("b (>a): "))
k = random.randint(1, m)
print(f"10.1ж: k={k}, числа:", [random.uniform(a, b) for _ in range(k)])

# 10.2 (случайные целые числа)
# а) 10 чисел от 0 до 10
print("10.2а:", [random.randint(0, 10) for _ in range(10)])
# б) k чисел от 0 до a
k = int(input("k: "))
a = int(input("a: "))
print("10.2б:", [random.randint(0, a) for _ in range(k)])
# в) 20 чисел от 10 до 20
print("10.2в:", [random.randint(10, 20) for _ in range(20)])
# г) k чисел от -10 до a
k = int(input("k: "))
a = int(input("a: "))
print("10.2г:", [random.randint(-10, a) for _ in range(k)])
# д) случайное k ≤15, и k чисел от a до b
a = int(input("a: "))
b = int(input("b (>a): "))
k = random.randint(1, 15)
print(f"10.2д: k={k}, числа:", [random.randint(a, b) for _ in range(k)])

# 10.3 (разные случайные числа)
a = int(input("a: "))
b = int(input("b: "))
m = random.randint(1, 20)
n = random.randint(1, 20)
print(f"m={m}, n={n}")
print("Целые от a до b:", [random.randint(a, b) for _ in range(n)])
print("Вещественные ≤ n:", [random.random()*n for _ in range(m)])

# 10.4 (50 чисел 0-5, выводим только 0 и 1)
nums = [random.randint(0, 5) for _ in range(50)]
print("Только 0 и 1:", [x for x in nums if x in (0, 1)])

# 10.5 (30 чисел 0-5, выводим только нечётные)
nums = [random.randint(0, 5) for _ in range(30)]
print("Нечётные:", [x for x in nums if x % 2 != 0])

# 10.6 (50 чисел 0 или 1, подсчёт)
nums = [random.randint(0, 1) for _ in range(50)]
print("Единиц:", nums.count(1))
print("Нулей:", nums.count(0))

# 10.7 (разные наборы случайных чисел)
# а) a in [0,1], b in [0,1,2], разные
a = random.randint(0, 1)
b = random.choice([x for x in range(3) if x != a])
print("10.7а: a=", a, "b=", b)
# б) a in [1,2], b in [0,1,2], c in [1,2,3], все разные
a = random.randint(1, 2)
b = random.choice([x for x in range(3) if x != a])
c = random.choice([x for x in range(1, 4) if x not in (a, b)])
print("10.7б: a=", a, "b=", b, "c=", c)
# в) 15 чисел: 7 двоек и 8 троек
nums = [2]*7 + [3]*8
random.shuffle(nums)
print("10.7в:", nums)

# 10.8 (подбрасывание монеты)
coin = random.randint(0, 1)
print("Монета:", "решка" if coin == 0 else "орел")

# 10.9 (относительная частота)
N = 100
results = [random.randint(0, 1) for _ in range(N)]
print("Частота 0 при 100 бросках:", results.count(0)/N)
print("Частота 1 при 100 бросках:", results.count(1)/N)

N = 1000
results = [random.randint(0, 1) for _ in range(N)]
print("Частота 0 при 1000 бросках:", results.count(0)/N)
print("Частота 1 при 1000 бросках:", results.count(1)/N)

# 10.10 (игра "Чет или нечет")
# а) один раз
print("Чет (2) или нечет (1)?")
guess = int(input("Ваш выбор: "))
comp = random.choice([1, 2])
print("Компьютер выбрал:", "чет" if comp == 2 else "нечет")
print("Вы угадали!" if guess == comp else "Вы не угадали.")

# б) n раз
n = int(input("Сколько раз играем? "))
score_user = 0
score_comp = 0
for _ in range(n):
    guess = int(input("Чет (2) или нечет (1)? "))
    comp = random.choice([1, 2])
    if guess == comp:
        score_user += 1
    else:
        score_comp += 1
if score_user > score_comp:
    print(f"Счет {score_user}:{score_comp} в вашу пользу. Вы выиграли!")
elif score_comp > score_user:
    print(f"Счет {score_user}:{score_comp} в пользу компьютера. Вы проиграли!")
else:
    print("Ничья!")

# в) до команды "Нет"
score_user = 0
score_comp = 0
while True:
    guess = int(input("Чет (2) или нечет (1)? (0 для выхода) "))
    if guess == 0:
        break
    comp = random.choice([1, 2])
    if guess == comp:
        score_user += 1
        print("Угадал!")
    else:
        score_comp += 1
        print("Не угадал!")
print(f"Верных ответов: {score_user}, неверных: {score_comp}")

# 10.11 (бросание кубика)
dice = random.randint(1, 6)
print("Выпало на кубике:", dice)

# 10.12 (два игрока)
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(f"Игрок 1: {dice1}, игрок 2: {dice2}")
if dice1 > dice2:
    print("Победил игрок 1")
elif dice2 > dice1:
    print("Победил игрок 2")
else:
    print("Ничья")

# 10.13 (игра с несколькими бросками)
# 1) каждый бросает два раза
dice1 = [random.randint(1, 6) for _ in range(2)]
dice2 = [random.randint(1, 6) for _ in range(2)]
print(f"Игрок 1: {dice1}, сумма {sum(dice1)}")
print(f"Игрок 2: {dice2}, сумма {sum(dice2)}")
if sum(dice1) > sum(dice2):
    print("Победил игрок 1")
elif sum(dice2) > sum(dice1):
    print("Победил игрок 2")
else:
    print("Ничья")

# 2) несколько раундов
rounds = int(input("Сколько раундов? "))
wins1 = 0
wins2 = 0
draws = 0
for _ in range(rounds):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 > dice2:
        wins1 += 1
    elif dice2 > dice1:
        wins2 += 1
    else:
        draws += 1
print(f"Игрок 1: {wins1} побед, Игрок 2: {wins2} побед, ничьих: {draws}")

# 10.14 (три игрока, K кубиков)
K = int(input("Сколько кубиков бросает каждый? "))
players = []
for i in range(3):
    dice = [random.randint(1, 6) for _ in range(K)]
    total = sum(dice)
    players.append((total, i+1))
    print(f"Игрок {i+1}: {dice}, сумма {total}")
winner = max(players)
print(f"Победил игрок {winner[1]} с суммой {winner[0]}")

# 10.15 (относительная частота чисел на кубике)
N = 100
results = [random.randint(1, 6) for _ in range(N)]
print("Частоты при 100 бросках:")
for i in range(1, 7):
    print(f"{i}: {results.count(i)/N:.3f}")

N = 1000
results = [random.randint(1, 6) for _ in range(N)]
print("Частоты при 1000 бросках:")
for i in range(1, 7):
    print(f"{i}: {results.count(i)/N:.3f}")

# 10.16 (случайная кость домино)
a = random.randint(0, 6)
b = random.randint(0, 6)
print(f"Выбрана кость {a}-{b}")

# 10.17 (две случайные кости домино, можно ли приставить)
a1, b1 = random.randint(0, 6), random.randint(0, 6)
a2, b2 = random.randint(0, 6), random.randint(0, 6)
print(f"Кость 1: {a1}-{b1}")
print(f"Кость 2: {a2}-{b2}")
if a1 == a2 or a1 == b2 or b1 == a2 or b1 == b2:
    print("Кости можно приставить")
else:
    print("Кости нельзя приставить")

# 10.18 (проверка таблицы умножения)
# а) один вопрос
a = random.randint(2, 9)
b = random.randint(2, 9)
answer = int(input(f"{a} × {b} = ? "))
if answer == a*b:
    print("Правильно!")
else:
    print(f"Неправильно. Правильный ответ: {a*b}")

# б) 20 вопросов
correct = 0
for _ in range(20):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = int(input(f"{a} × {b} = ? "))
    if answer == a*b:
        correct += 1
print(f"Правильных ответов: {correct}, неправильных: {20-correct}")

# в) до ввода 0
while True:
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = int(input(f"{a} × {b} = ? (0 для выхода) "))
    if answer == 0:
        break
    if answer == a*b:
        print("Правильно!")
    else:
        print(f"Неправильно. Правильный ответ: {a*b}")

# 10.19 (случайная карта одной масти)
ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
card = random.choice(ranks)
print("Выбрана карта:", card)

# 10.20 (случайная карта из полной колоды)
suits = ["пик", "треф", "бубен", "червей"]
ranks = ["шестерка", "семерка", "восьмерка", "девятка", "десятка", "валет", "дама", "король", "туз"]
suit = random.choice(suits)
rank = random.choice(ranks)
print(f"Выбрана {rank} {suit}")

# 10.21 (две карты, определение старшей)
suit1 = random.choice(suits)
rank1 = random.choice(ranks)
suit2 = random.choice(suits)
rank2 = random.choice(ranks)
print(f"Игрок 1: {rank1} {suit1}")
print(f"Игрок 2: {rank2} {suit2}")
# Сравниваем: сначала масти, потом достоинства
if suits.index(suit1) > suits.index(suit2):
    print("Старше карта игрока 1")
elif suits.index(suit2) > suits.index(suit1):
    print("Старше карта игрока 2")
else:
    if ranks.index(rank1) > ranks.index(rank2):
        print("Старше карта игрока 1")
    elif ranks.index(rank2) > ranks.index(rank1):
        print("Старше карта игрока 2")
    else:
        print("Карты одинаковы")

# 10.22 (несколько раундов)
rounds = int(input("Сколько раундов? "))
score1 = 0
score2 = 0
for r in range(rounds):
    suit1 = random.choice(suits)
    rank1 = random.choice(ranks)
    suit2 = random.choice(suits)
    rank2 = random.choice(ranks)
    if suits.index(suit1) > suits.index(suit2):
        score1 += 1
    elif suits.index(suit2) > suits.index(suit1):
        score2 += 1
    else:
        if ranks.index(rank1) > ranks.index(rank2):
            score1 += 1
        elif ranks.index(rank2) > ranks.index(rank1):
            score2 += 1
print(f"Счет: {score1}:{score2}")

# 10.23 (с козырной мастью)
trump = random.choice(suits)
print(f"Козырная масть: {trump}")
suit1 = random.choice(suits)
rank1 = random.choice(ranks)
print(f"Выбрана карта: {rank1} {suit1}")
if suit1 == trump:
    print("Карта козырная")

# 10.24 (случайные координаты на шахматной доске)
# а) ладья не угрожает полю
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if not (a == c or b == d):  # ладья угрожает, если совпадает строка или столбец
        break
print(f"Ладья на ({a},{b}) не угрожает полю ({c},{d})")

# б) слон не угрожает
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if abs(a - c) != abs(b - d):
        break
print(f"Слон на ({a},{b}) не угрожает полю ({c},{d})")

# в) король может попасть за один ход
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if max(abs(a - c), abs(b - d)) == 1:  # король ходит на одну клетку в любом направлении
        break
print(f"Король на ({a},{b}) может попасть на ({c},{d}) за один ход")

# г) ферзь не угрожает
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if not (a == c or b == d or abs(a - c) == abs(b - d)):
        break
print(f"Ферзь на ({a},{b}) не угрожает полю ({c},{d})")

# 10.25 (пешки и конь)
# а) белая пешка может сделать обычный ход
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if b == 2 and d == b + 2 and a == c:  # с начальной позиции на две клетки
        break
print(f"Белая пешка на ({a},{b}) может пойти на ({c},{d}) обычным ходом")

# б) белая пешка может бить
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if d == b + 1 and abs(a - c) == 1:
        break
print(f"Белая пешка на ({a},{b}) может бить на ({c},{d})")

# в) чёрная пешка может сделать обычный ход
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if b == 7 and d == b - 2 and a == c:
        break
print(f"Чёрная пешка на ({a},{b}) может пойти на ({c},{d}) обычным ходом")

# г) чёрная пешка может бить
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if d == b - 1 and abs(a - c) == 1:
        break
print(f"Чёрная пешка на ({a},{b}) может бить на ({c},{d})")

# д) конь угрожает полю
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    if (abs(a - c), abs(b - d)) in [(1,2), (2,1)]:
        break
print(f"Конь на ({a},{b}) угрожает полю ({c},{d})")

# 10.26 (белая фигура и чёрная фигура)
# Рассмотрим один вариант: ладья и ладья
while True:
    a, b = random.randint(1, 8), random.randint(1, 8)
    c, d = random.randint(1, 8), random.randint(1, 8)
    e, f = random.randint(1, 8), random.randint(1, 8)
    # Белая ладья на (a,b), черная ладья на (c,d), белая хочет пойти на (e,f)
    # Проверяем, что (e,f) не под боем черной ладьи
    if not (c == e or d == f):
        break
print(f"Белая ладья на ({a},{b}) может пойти на ({e,f}) не под боем черной ладьи на ({c},{d})")

# 10.27 (метод Монте-Карло)
# а) площадь половины синусоиды от 0 до π
N = 100000
count = 0
for _ in range(N):
    x = random.random() * math.pi
    y = random.random()  # максимум sin(x) = 1
    if y <= math.sin(x):
        count += 1
area = (math.pi * 1) * (count / N)
print(f"Площадь половины синусоиды ≈ {area}")

# б) площадь под параболой y=x² от 0 до 3
count = 0
for _ in range(N):
    x = random.random() * 3
    y = random.random() * 9  # максимум y=9 при x=3
    if y <= x**2:
        count += 1
area = (3 * 9) * (count / N)
print(f"Площадь под параболой y=x² от 0 до 3 ≈ {area}")

# 10.28 (число π методом Монте-Карло)
# Площадь круга радиуса 1 = π, вписанного в квадрат 2×2
count = 0
N = 0
target_error = 0.0001
current_pi = 0
while True:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        count += 1
    N += 1
    new_pi = 4 * count / N
    if N > 100 and abs(new_pi - current_pi) < target_error:
        break
    current_pi = new_pi
print(f"π ≈ {current_pi} (выполнено {N} испытаний)")

# 11.42 (операции с массивом)
arr = [random.randint(1, 20) for _ in range(10)]
print("Массив:", arr)
print("Сумма всех элементов:", sum(arr))
product = 1
for x in arr:
    product *= x
print("Произведение всех элементов:", product)
print("Сумма квадратов:", sum(x**2 for x in arr))
print("Сумма первых шести элементов:", sum(arr[:6]))
k1 = int(input("k1: "))
k2 = int(input("k2 (>k1): "))
print(f"Сумма с {k1}-го по {k2}-й:", sum(arr[k1-1:k2]))
print("Среднее арифметическое всех элементов:", sum(arr)/len(arr))
s1 = int(input("s1: "))
s2 = int(input("s2 (>s1): "))
print(f"Среднее с {s1}-го по {s2}-й:", sum(arr[s1-1:s2])/(s2-s1+1))

# 11.43 (знакопеременная сумма)
arr = [random.randint(1, 10) for _ in range(10)]
print("Массив:", arr)
total = 0
sign = 1
for x in arr:
    total += sign * x
    sign *= -1
print("Знакопеременная сумма a[1]-a[2]+a[3]-...:", total)

# 11.44 (осадки за январь)
days = 31
precip = [random.randint(0, 10) for _ in range(days)]
print("Осадки за январь:", precip)
print("Общее количество осадков:", sum(precip))

# 11.45 (стоимость 12 предметов)
prices = [random.uniform(100, 1000) for _ in range(12)]
print("Стоимости:", [round(p,2) for p in prices])
print("Общая стоимость:", round(sum(prices),2))

# 11.46 (последовательное сопротивление)
resistances = [random.uniform(10, 100) for _ in range(20)]
print("Сопротивления:", [round(r,2) for r in resistances])
print("Общее последовательное сопротивление:", round(sum(resistances),2))

# 11.47 (параллельное сопротивление)
total = sum(1/r for r in resistances)
print("Общее параллельное сопротивление:", round(1/total,2) if total != 0 else "бесконечность")

# 11.48 (осадки за декады июня)
days = 30
precip = [random.randint(0, 20) for _ in range(days)]
print("Осадки за июнь:", precip)
print("За первую декаду:", sum(precip[:10]))
print("За вторую декаду:", sum(precip[10:20]))
print("За третью декаду:", sum(precip[20:]))

# 11.49 (среднедневные осадки февраля)
days = 28
precip = [random.randint(0, 15) for _ in range(days)]
print("Среднедневные осадки февраля:", sum(precip)/days)

# 11.50 (среднее за декады сентября)
days = 30
precip = [random.randint(0, 25) for _ in range(days)]
print("Среднее за 1-ю декаду:", sum(precip[:10])/10)
print("Среднее за 2-ю декаду:", sum(precip[10:20])/10)
print("Среднее за 3-ю декаду:", sum(precip[20:])/10)

# 11.51 (сумма неотрицательна?)
arr = [random.randint(-10, 10) for _ in range(10)]
print("Массив:", arr)
print("Сумма неотрицательна?", sum(arr) >= 0)

# 11.52 (чётность суммы, пятизначность суммы квадратов)
arr = [random.randint(1, 50) for _ in range(10)]
print("Массив:", arr)
print("Сумма чётная?", sum(arr) % 2 == 0)
squares_sum = sum(x**2 for x in arr)
print("Сумма квадратов пятизначная?", 10000 <= squares_sum <= 99999)

# 11.53 (общее число учеников четырёхзначно?)
classes = 42
students = [random.randint(20, 30) for _ in range(classes)]
total = sum(students)
print("Общее число учеников:", total)
print("Четырёхзначное?", 1000 <= total <= 9999)

# 11.54 (общее число книг шестизначно?)
sections = 35
books = [random.randint(1000, 5000) for _ in range(sections)]
total = sum(books)
print("Общее число книг:", total)
print("Шестизначное?", 100000 <= total <= 999999)

# 11.55 (грузоподъёмность)
capacity = 1000
items = 30
masses = [random.uniform(10, 50) for _ in range(items)]
total_mass = sum(masses)
print("Общая масса:", round(total_mass,2))
print("Превышает грузоподъёмность?", total_mass > capacity)

# 11.56 (выход в следующий этап)
threshold = 8000
scores = [random.randint(600, 1200) for _ in range(10)]
total = sum(scores)
print("Баллы спортсмена:", scores)
print("Общая сумма:", total)
print("Вышел в следующий этап?", total > threshold)

# 11.57 (сравнение осадков в июне)
days = 30
precip = [random.randint(0, 20) for _ in range(days)]
first_half = sum(precip[:15])
second_half = sum(precip[15:])
print("Осадки в первой половине:", first_half)
print("Осадки во второй половине:", second_half)
print("Больше в первой половине?", first_half > second_half)
# по декадам
dec1 = sum(precip[:10])
dec2 = sum(precip[10:20])
dec3 = sum(precip[20:])
max_dec = max(dec1, dec2, dec3)
print("Самая дождливая декада:", ["первая","вторая","третья"][[dec1,dec2,dec3].index(max_dec)])

# 11.58 (фигурное катание)
scores = [random.uniform(4, 6) for _ in range(18)]
obligatory = scores[:6]
free = scores[6:]
avg_obl = sum(obligatory)/6
avg_free = sum(free)/12
print("Средний балл обязательной программы:", avg_obl)
print("Средний балл произвольной программы:", avg_free)
print("Лучший результат в", "обязательной" if avg_obl > avg_free else "произвольной", "программе")

# 11.59 (сумма элементов по условиям)
arr = [random.randint(1, 30) for _ in range(10)]
print("Массив:", arr)
print("Сумма ≤20:", sum(x for x in arr if x <= 20))
a = int(input("a: "))
print(f"Сумма >{a}:", sum(x for x in arr if x > a))

# 11.60 (суммы по свойствам)
arr = [random.randint(1, 50) for _ in range(10)]
print("Массив:", arr)
print("Сумма нечётных:", sum(x for x in arr if x % 2 != 0))
k = int(input("Кратность: "))
print(f"Сумма кратных {k}:", sum(x for x in arr if x % k == 0))
a = int(input("a: "))
b = int(input("b: "))
print(f"Сумма кратных {a} или {b}:", sum(x for x in arr if x % a == 0 or x % b == 0))

# 11.61 (сумма элементов с чётными индексами 2,4,6...)
arr = [random.randint(1, 20) for _ in range(10)]
print("Массив:", arr)
total = sum(arr[i] for i in range(1, len(arr), 2))  # индексы 1,3,5...
print("Сумма элементов на чётных позициях (2,4,6...):", total)

# 11.62 (осадки по чётным числам февраля)
days = 28
precip = [random.randint(0, 10) for _ in range(days)]
total = sum(precip[i] for i in range(1, days, 2))  # дни 2,4,6...
print("Осадки по чётным числам февраля:", total)

# 11.63 (осадки в марте, июне, сентябре, декабре)
months = 12
precip = [random.randint(20, 100) for _ in range(months)]
print("Осадки по месяцам:", precip)
total = precip[2] + precip[5] + precip[8] + precip[11]  # месяцы 3,6,9,12
print("Осадки в марте, июне, сентябре, декабре:", total)

# 11.64 (частное суммы положительных на модуль суммы отрицательных)
arr = [random.randint(-10, 10) for _ in range(10)]
print("Массив:", arr)
pos_sum = sum(x for x in arr if x > 0)
neg_sum = sum(x for x in arr if x < 0)
if neg_sum != 0:
    print("Частное:", pos_sum / abs(neg_sum))
else:
    print("Отрицательных нет, деление невозможно")

# 11.65 (проверки сумм)
arr = [random.randint(1, 60) for _ in range(10)]
print("Массив:", arr)
sum_gt20 = sum(x for x in arr if x > 20)
sum_lt50 = sum(x for x in arr if x < 50)
print("Сумма >20 превышает 100?", sum_gt20 > 100)
print("Сумма <50 чётная?", sum_lt50 % 2 == 0)

# 11.66 (осадки по чётным vs нечётным дням февраля)
days = 28
precip = [random.randint(0, 15) for _ in range(days)]
even_sum = sum(precip[i] for i in range(1, days, 2))
odd_sum = sum(precip[i] for i in range(0, days, 2))
print("По чётным больше?", even_sum > odd_sum)

# 11.67 (жители по сторонам улицы)
houses = 20
residents = [random.randint(1, 10) for _ in range(houses)]
odd_sum = sum(residents[i] for i in range(0, houses, 2))
even_sum = sum(residents[i] for i in range(1, houses, 2))
print("На нечётной стороне больше?", odd_sum > even_sum)

# 11.68 (количество неотрицательных)
arr = [random.randint(-5, 5) for _ in range(10)]
print("Массив:", arr)
count = sum(1 for x in arr if x >= 0)
print("Неотрицательных элементов:", count)

# 11.69 (количество элементов, отличных от последнего, кратных a)
arr = [random.randint(1, 20) for _ in range(10)]
print("Массив:", arr)
last = arr[-1]
count_diff = sum(1 for x in arr if x != last)
print("Отличных от последнего:", count_diff)
a = int(input("a: "))
count_mult = sum(1 for x in arr if x % a == 0)
print(f"Кратных {a}:", count_mult)

# 11.70 (дни без осадков в феврале)
days = 28
precip = [random.randint(0, 10) for _ in range(days)]
count_dry = precip.count(0)
print("Дней без осадков:", count_dry)

# 11.71 (неуспевающие по химии)
students = 25
grades = [random.randint(2, 5) for _ in range(students)]
count_fail = grades.count(2)
print("Неуспевающих:", count_fail)

# 11.72 (дни с продажами > s)
days = 31
sales = [random.uniform(5000, 20000) for _ in range(days)]
s = float(input("Порог s: "))
count = sum(1 for x in sales if x > s)
print(f"Дней с продажами > {s}:", count)

# 11.73 (ученики ростом ≤ r)
students = 22
heights = [random.randint(150, 190) for _ in range(students)]
r = int(input("r: "))
count = sum(1 for h in heights if h <= r)
print(f"Учеников ростом ≤ {r}:", count)

# 11.74 (элементы в промежутке [a,b])
arr = [random.randint(1, 100) for _ in range(10)]
print("Массив:", arr)
a = int(input("a: "))
b = int(input("b (>a): "))
count = sum(1 for x in arr if a <= x <= b)
print(f"Элементов в [{a},{b}]:", count)

# 11.75 (выигрыши и ничьи футбольной команды)
games = 20
results = [random.choice([0,1,3]) for _ in range(games)]
print("Результаты игр (0-поражение,1-ничья,3-победа):", results)
wins = results.count(3)
draws = results.count(1)
print("Выигрышей:", wins)
print("Ничьих:", draws)

# 11.76 (четвёрки и пятёрки)
grades = [random.randint(2, 5) for _ in range(10)]
print("Оценки:", grades)
count4 = grades.count(4)
count5 = grades.count(5)
print("Четвёрок:", count4)
print("Пятёрок:", count5)

# 11.77 (положительные и отрицательные)
arr = [random.randint(-10, 10) for _ in range(10)]
print("Массив:", arr)
pos = sum(1 for x in arr if x > 0)
neg = sum(1 for x in arr if x < 0)
print("Положительных:", pos)
print("Отрицательных:", neg)

# 11.78 (чётные и оканчивающиеся на 5)
arr = [random.randint(1, 100) for _ in range(10)]
print("Массив:", arr)
even = sum(1 for x in arr if x % 2 == 0)
ends5 = sum(1 for x in arr if x % 10 == 5)
print("Чётных:", even)
print("Оканчивающихся на 5:", ends5)

# 11.79 (выигрыши, ничьи, проигрыши)
results = [random.choice([0,1,3]) for _ in range(20)]
print("Результаты:", results)
wins = results.count(3)
draws = results.count(1)
losses = results.count(0)
print("Выигрышей:", wins)
print("Ничьих:", draws)
print("Проигрышей:", losses)

# 11.80 (оценки по иностранному языку)
students = 22
grades = [random.randint(2, 5) for _ in range(students)]
print("Оценки:", grades)
count5 = grades.count(5)
count4 = grades.count(4)
count3 = grades.count(3)
count2 = grades.count(2)
print("Пятёрок:", count5)
print("Четвёрок:", count4)
print("Троек:", count3)
print("Двоек:", count2)

# 11.81 (пары соседних чётных чисел)
arr = [random.randint(1, 20) for _ in range(10)]
print("Массив:", arr)
count = 0
for i in range(len(arr)-1):
    if arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
        count += 1
print("Пар соседних чётных чисел:", count)

# 11.82 (пары соседних чисел, оканчивающихся на 0)
arr = [random.randint(1, 100) for _ in range(10)]
print("Массив:", arr)
count = 0
for i in range(len(arr)-1):
    if arr[i] % 10 == 0 and arr[i+1] % 10 == 0:
        count += 1
print("Пар соседних чисел, оканчивающихся на 0:", count)

# 11.83 (элементы больше соседей)
arr = [random.randint(1, 20) for _ in range(10)]
print("Массив:", arr)
count = 0
for i in range(1, len(arr)-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        count += 1
print("Элементов, больших своих соседей:", count)

# 11.84 (проверки количества)
arr = [random.uniform(0, 100) for _ in range(10)]
print("Массив:", [round(x,2) for x in arr])
pos_count = sum(1 for x in arr if x > 0)
print("Количество положительных ≤5?", pos_count <= 5)
count_le50 = sum(1 for x in arr if x <= 50.55)
print(f"Количество ≤50.55 кратно 4?", count_le50 % 4 == 0)

# 11.85 (баскетбольная команда)
heights = [random.randint(160, 200) for _ in range(30)]
count_gt170 = sum(1 for h in heights if h > 170)
print("Росты:", heights)
print("Человек ростом >170 см:", count_gt170)
print("Можно сформировать команду (≥5 чел.)?", count_gt170 >= 5)

# 11.86 (10 дней без осадков в марте)
days = 31
precip = [random.randint(0, 10) for _ in range(days)]
dry_days = precip.count(0)
print("Дней без осадков:", dry_days)
print("Ровно 10 дней без осадков?", dry_days == 10)

# 11.87 (среднее элементов >10)
arr = [random.randint(1, 30) for _ in range(10)]
print("Массив:", arr)
gt10 = [x for x in arr if x > 10]
if gt10:
    print("Среднее элементов >10:", sum(gt10)/len(gt10))
else:
    print("Элементов >10 нет")

# 11.88 (среднее элементов < m)
m = int(input("m: "))
lt_m = [x for x in arr if x < m]
if lt_m:
    print(f"Среднее элементов < {m}:", sum(lt_m)/len(lt_m))
else:
    print(f"Элементов < {m} нет")

# 11.89 (среднее осадков в дождливые дни)
days = 31
precip = [random.randint(0, 20) for _ in range(days)]
rainy = [p for p in precip if p > 0]
if rainy:
    print("Среднее осадков в дождливые дни:", sum(rainy)/len(rainy))
else:
    print("Дождливых дней не было")

# 11.90 (средние положительных и отрицательных)
arr = [random.randint(-10, 10) for _ in range(10)]
print("Массив:", arr)
pos = [x for x in arr if x > 0]
neg = [x for x in arr if x < 0]
if pos:
    print("Среднее положительных:", sum(pos)/len(pos))
else:
    print("Положительных нет")
if neg:
    print("Среднее отрицательных:", sum(neg)/len(neg))
else:
    print("Отрицательных нет")

# 11.91 (средняя масса полных и остальных)
people = 25
masses = [random.uniform(50, 120) for _ in range(people)]
full = [m for m in masses if m > 100]
others = [m for m in masses if m <= 100]
if full:
    print("Средняя масса полных (>100 кг):", sum(full)/len(full))
else:
    print("Полных нет")
if others:
    print("Средняя масса остальных:", sum(others)/len(others))
else:
    print("Все полные")

# 11.92 (средний рост мальчиков и девочек)
students = 22
heights = []
for _ in range(students):
    if random.choice([True, False]):  # мальчик
        heights.append(-random.randint(160, 180))
    else:  # девочка
        heights.append(random.randint(150, 170))
boys = [abs(h) for h in heights if h < 0]
girls = [h for h in heights if h > 0]
if boys:
    print("Средний рост мальчиков:", sum(boys)/len(boys))
else:
    print("Мальчиков нет")
if girls:
    print("Средний рост девочек:", sum(girls)/len(girls))
else:
    print("Девочек нет")

# 11.93 (сравнение средней стоимости автомобилей и мотоциклов)
cars = [random.uniform(5000, 30000) for _ in range(10)]
bikes = [random.uniform(1000, 5000) for _ in range(10)]
avg_cars = sum(cars)/len(cars)
avg_bikes = sum(bikes)/len(bikes)
print("Средняя стоимость автомобилей:", round(avg_cars,2))
print("Средняя стоимость мотоциклов:", round(avg_bikes,2))
print("Средняя автомобилей >3× средняя мотоциклов?", avg_cars > 3*avg_bikes)

# 11.94 (сравнение среднего роста мальчиков и девочек)
if boys and girls:
    avg_boys = sum(boys)/len(boys)
    avg_girls = sum(girls)/len(girls)
    print("Средний рост мальчиков:", avg_boys)
    print("Средний рост девочек:", avg_girls)
    print("Мальчики выше девочек более чем на 10 см?", avg_boys > avg_girls + 10)
else:
    print("Недостаточно данных")

# 11.95 (элементы больше суммы всех элементов)
arr = [random.randint(1, 20) for _ in range(10)]
print("Массив:", arr)
total = sum(arr)
indices = [i for i, x in enumerate(arr) if x > total]
print("Сумма всех элементов:", total)
print("Индексы элементов > суммы:", indices)

# 11.96 (элементы больше среднего min и max)
arr = [random.randint(1, 30) for _ in range(10)]
print("Массив:", arr)
avg_min_max = (min(arr) + max(arr)) / 2
indices = [i for i, x in enumerate(arr) if x > avg_min_max]
print("Среднее min и max:", avg_min_max)
print("Индексы элементов > среднего min и max:", indices)

# 11.97 (ученики ростом больше среднего)
heights = [random.randint(150, 190) for _ in range(25)]
avg_height = sum(heights)/len(heights)
count = sum(1 for h in heights if h > avg_height)
print("Средний рост:", avg_height)
print("Учеников ростом больше среднего:", count)

# 11.98 (товары дешевле средней стоимости)
prices = [random.uniform(100, 1000) for _ in range(20)]
avg_price = sum(prices)/len(prices)
count = sum(1 for p in prices if p < avg_price)
print("Средняя стоимость:", round(avg_price,2))
print("Товаров дешевле средней стоимости:", count)

# 11.99 (дни с осадками больше среднего за январь)
days = 31
precip = [random.randint(0, 20) for _ in range(days)]
avg_precip = sum(precip)/days
rainy_days = [i+1 for i, p in enumerate(precip) if p > avg_precip]
print("Среднее количество осадков:", avg_precip)
print("Дни с осадками больше среднего:", rainy_days)

# 11.100 (ученики с оценкой ниже средней)
grades = [random.randint(2, 5) for _ in range(22)]
avg_grade = sum(grades)/len(grades)
indices = [i for i, g in enumerate(grades) if g < avg_grade]
print("Оценки:", grades)
print("Средняя оценка:", avg_grade)
print("Индексы учеников с оценкой ниже средней:", indices)

