
class Polynomial:

    def __init__(self,coeffs):
        if not isinstance(coeffs,list):
            raise TypeError("Wrong type")
        else:
            if len(coeffs) == 0:
                raise TypeError("Wrong type")
            for i in coeffs:
                if not isinstance(i,(int,float)):
                    raise TypeError("Wrong type")
        self.coeffs = coeffs[:]
        c = self.coeffs
        if c:
            i = 0
            if c[i] == 0 and len(c) > 1:
                i += 1
                while i < len(c) - 1 and c[i] == 0:
                    i += 1
                del c[:i]

    @property
    def degree(self):
        return len(self.coeffs) - 1

    def __str__(self):
        result = ''
        i = self.degree
        k = 0
        while i >= 0:
            if self.coeffs[k] < 0:
                result += '-'
            elif self.coeffs[k] != 0 and self.degree != i:
                result += '+'
            if i != 0 and self.coeffs[k] != 0:
                if i != 1:
                    if abs(self.coeffs[k]) == 1:
                        result += 'x^' + str(i)
                    else:
                        result += str(abs(self.coeffs[k])) + 'x^' + str(i)
                else:
                    if abs(self.coeffs[k]) == 1:
                        result += 'x'
                    else:
                        result += str(abs(self.coeffs[k])) + 'x'
            elif i == 0 and self.coeffs[k] != 0:
                result += str(abs(self.coeffs[k]))
            k += 1
            i -= 1
        return result

    def __add__(self, other):
        poly = []
        if isinstance(other, Polynomial):
            if self.degree > other.degree:
                c = self.degree - other.degree
                k = 0
                poly = self.coeffs
                for i in range(c, len(poly)):
                    poly[i] += other.coeffs[k]
                    k += 1
            elif self.degree < other.degree:
                c = other.degree - self.degree
                k = 0
                poly = other.coeffs
                for i in range(c, len(poly)):
                    poly[i] += self.coeffs[k]
                    k += 1
            else:
                poly = self.coeffs
                for i in range(0,len(poly)):
                    poly[i] += other.coeffs[i]
        elif isinstance(other,(int,float)):
            poly = self.coeffs[:]
            poly[-1] += other
        else:
            raise TypeError("Wrong type")
        return Polynomial(poly)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self.__add__(-other)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        elif isinstance(other, (int, float)):
            return self.coeffs[-1] == other
        else:
            raise TypeError("Wrong type")

    def __mul__(self, other):
        poly = []
        if isinstance(other,Polynomial):
            coeffs1 = self.coeffs
            coeffs2 = other.coeffs
            poly = [0] * (len(coeffs1) + len(coeffs2) - 1)
            for pow1, coef1 in enumerate(coeffs1):
                for pow2, coef2 in enumerate(coeffs2):
                    poly[pow1 + pow2] += coef1 * coef2
        elif isinstance(other,(int,float)):
            for item in self.coeffs:
                poly.append(other*item)
        else:
            raise TypeError("Wrong Type")
        return Polynomial(poly)


    def __rmul__(self, other):
        return self * other
