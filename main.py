count = 0
n = 452022

while count < 5:
    divisors = []

    # Ищем делители от 2 до sqrt(n)
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divisors.append(d)
            if d != n // d and n // d != n:
                divisors.append(n // d)

    if divisors:
        min_d = min(divisors)
        max_d = max(divisors)
        M = min_d + max_d
    else:
        M = 0

    if M % 7 == 3:
        print(n, M)
        count += 1

    n += 1