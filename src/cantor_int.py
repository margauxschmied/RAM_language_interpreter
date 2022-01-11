class Int(int):
    """
    This class aims to represent an int with the propreties 
    seen in our class, the four common operations (+, x, -, /) have been redefined to follow some important rules. \n
    For exemple,                          \n
        a - b gives 0 if b > a            \n
        a / b  gives the floor division   \n
    This class provides other important methods such as: \n
        left (resp. right) : giving the left (resp. right) part of an int
    """

    def __sub__(self, x: int): return Int(max(int(self) - x, 0))

    def __truediv__(self, x: int): return Int(int(self) // x)

    def __add__(self, x: int): return Int(int(self) + x)

    def __mul__(self, x: int): return Int(int(self) * x)

    def aux(self):
        """ Aux. function to calculate left and right part """

        def diff(val): return Int(self - val * (val + 1) // 2)
        def mean(m, M): return Int(m + (M-m)//2)
        m, M = 0, self
        if self == 0:
            raise Exception("Can't decode 0")
        while True:
            if M < 3:
                return M
            meanV = mean(m, M)
            diffV, diffD = diff(meanV), diff(meanV-1)
            if diffV <= 0 and diffD > 0:
                return meanV
            m, M = (m, meanV) if diffV <= 0 else (meanV, M)

    def right(self):
        """ Give the right part of a Int, from Cantor formula """
        tmp = self.aux()
        return self - ((tmp - 1) * tmp / 2 + 1)

    def left(self):
        """ Give the left part of a Int, from Cantor formula """
        return self.aux() - self.right() - 1

    def cantor_inv(self):
        tmp = self.aux()
        r = self - ((tmp - 1) * tmp / 2 + 1)
        l = tmp - r - 1
        return l, r

    def cantor(x, y):
        """ The standard Cantor's function """
        return (x+y+1)*(x+y)//2+y+1

    def int_to_couple(s):
        """ The couple (a1, (a2, ... (an, 0))) from an Int """
        res = Int(s).cantor_inv()
        return res if res[1] == 0 else (res[0], Int(res[1]).int_to_couple())

    def couple_to_int(s):
        return Int.cantor(s[0], Int.couple_to_int(s[1])) if not isinstance(s[1], int) else Int.cantor(*s)

    def int_to_str(self) -> str:
        """ 
        Gives a str repr of the couple of Cantor in the form we've seen in class : \n
        (a1, (a2, ... (an, 0))) → <a1, <a2, ... <an, 0>>>
        """
        def aux(x, s='', e=''):
            if x[1] == 0:
                return f"{s}, <{x[0]}, 0>{e}"
            return aux(x[1], f"{s + ', ' if s != '' else ''}<{x[0]}", e + '>')
        return aux(self.int_to_couple())


if __name__ == '__main__':
    for i in range(1, 20):
        I = Int(i)
        l, r = I.left(), I.right()
        # Test that the f(f_inv(X)) == X
        assert(I == Int.cantor(*Int.cantor_inv(I)))
        print(i, l, r, l.cantor(r))

    print(Int(32).int_to_str())

    assert(35 == Int.couple_to_int(Int.int_to_couple(Int(35))))
    c = (2, (5, (4, (0, (0, 0)))))
    assert(c == Int.int_to_couple(Int.couple_to_int(c)))
