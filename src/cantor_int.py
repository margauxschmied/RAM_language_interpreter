
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
        res, diff = Int(0), self
        while diff != 0:
            diff = self - (res * (res := res + 1) / 2)
        return res - 1

    def right(self):
        """ Give the right part of a Int, from Cantor formula """
        tmp = self.aux()
        return self - ((tmp - 1) * tmp / 2 + 1)

    def left(self):
        """ Give the left part of a Int, from Cantor formula """
        return self.aux() - self.right() - 1

    def cantor_inv(self):
        return self.left(), self.right()

    def cantor(x, y):
        """ The standard Cantor's function """
        return (x+y+1)*(x+y)/2+y+1

    def int_to_couple(s):
        """ The couple (a1, (a2, ... (an, (0, 0)))) from an Int"""
        res = s.left(), s.right()
        return res if res == (0, 0) else (res[0], res[1].int_to_couple())

    def int_to_str(self) -> str:
        """ 
        Gives a str repr of the couple of Cantor in the form we've seen in class : \n
        (a1, (a2, ... (an, (0, 0)))) → <a1, <a2, ... <an, <0, 0>>>>
        """
        def aux(x, s='', e=''):
            if x == (0, 0):
                return f"{s}, <0, 0>{e}"
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
