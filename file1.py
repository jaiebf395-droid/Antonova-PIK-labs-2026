import sys
import math


def get_coef(index, prompt):
    #чит коэф из командной строки
    while True:
        try:
            coef_str = sys.argv[index]
        except IndexError:
            print(prompt)
            coef_str = input()
        try:
            return float(coef_str)
        except ValueError:
            print("Ошибка: коэффициент должен быть действительным числом. Повторите ввод.")
            if index < len(sys.argv):
                #чтобы не зациклиться на плохом argv
                sys.argv = sys.argv[:index]


def solve_quadratic(a, b, c):
    #решение квадратного ур a*y^2 + b*y + c = 0
    #возвращает список действительных корней y
    result = []
    if a == 0:
        #линейное: b*y + c = 0
        if b == 0:
            return result
        result.append(-c / b)
        return result

    D = b * b - 4 * a * c
    if D == 0.0:
        result.append(-b / (2.0 * a))
    elif D > 0.0:
        sqD = math.sqrt(D)
        result.append((-b + sqD) / (2.0 * a))
        result.append((-b - sqD) / (2.0 * a))
    return result


def get_roots(a, b, c):
    #биквадрат ур: a*x^4 + b*x^2 + c = 0
    #возвращает список действительных корней x
    #замена t = x^2 -> a*t^2 + b*t + c = 0
    t_roots = solve_quadratic(a, b, c)

    x_roots = []
    for t in t_roots:
        if t < 0:
            continue          #нет действительных x
        if t == 0:
            x_roots.append(0.0)
        else:
            sqrt_t = math.sqrt(t)
            x_roots.append(sqrt_t)
            x_roots.append(-sqrt_t)

    #убир дубл
    unique = []
    for x in x_roots:
        if not any(abs(x - u) < 1e-12 for u in unique):
            unique.append(x)
    unique.sort()
    return unique


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)

    n = len(roots)
    if n == 0:
        print('Нет действительных корней')
    elif n == 1:
        print('Один корень: {:.6g}'.format(roots[0]))
    elif n == 2:
        print('Два корня: {:.6g} и {:.6g}'.format(roots[0], roots[1]))
    elif n == 3:
        print('Три корня: {:.6g}, {:.6g} и {:.6g}'.format(*roots))
    elif n == 4:
        print('Четыре корня: {:.6g}, {:.6g}, {:.6g} и {:.6g}'.format(*roots))


if __name__ == "__main__":
    main()
