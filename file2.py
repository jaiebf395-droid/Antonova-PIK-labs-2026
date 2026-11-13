import sys
import math


class BiquadraticEquation:
    #a*x^4 + b*x^2 + c = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _solve_quadratic(self):
        #корни квадр ур a*t^2 + b*t + c = 0
        a, b, c = self.a, self.b, self.c
        roots = []
        if a == 0:
            if b != 0:
                roots.append(-c / b)
            return roots
        D = b * b - 4 * a * c
        if D == 0:
            roots.append(-b / (2 * a))
        elif D > 0:
            sq = math.sqrt(D)
            roots.append((-b + sq) / (2 * a))
            roots.append((-b - sq) / (2 * a))
        return roots

    def solve(self):
        #действительные корни биквадратного ур
        result = []
        for t in self._solve_quadratic():
            if t < 0:
                continue
            if t == 0:
                result.append(0.0)
            else:
                s = math.sqrt(t)
                result.extend([s, -s])

        uniq = []
        for x in result:
            if not any(abs(x - u) < 1e-12 for u in uniq):
                uniq.append(x)
        return sorted(uniq)


class CoefficientReader:
    #чтение коэф из argv

    def __init__(self, argv):
        self.argv = argv

    def read(self, index, prompt):
        while True:
            if index < len(self.argv):
                raw = self.argv[index]
            else:
                print(prompt)
                raw = input()
            try:
                return float(raw)
            except ValueError:
                print("Ошибка: введите действительное число")
                self.argv = self.argv[:index]  # дальше — с клавиатуры


def main():
    reader = CoefficientReader(sys.argv)
    a = reader.read(1, 'Введите коэффициент А:')
    b = reader.read(2, 'Введите коэффициент B:')
    c = reader.read(3, 'Введите коэффициент C:')

    eq = BiquadraticEquation(a, b, c)
    roots = eq.solve()

    if not roots:
        print('Нет действительных корней')
    elif len(roots) == 1:
        print('Один корень: {:.6g}'.format(roots[0]))
    elif len(roots) == 2:
        print('Два корня: {:.6g} и {:.6g}'.format(*roots))
    else:
        print('Корни: ' + ', '.join('{:.6g}'.format(r) for r in roots))


if __name__ == "__main__":
    main()
