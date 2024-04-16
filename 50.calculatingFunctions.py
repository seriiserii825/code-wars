def zero(p=None): return 0 if p is None else p(0)
def one(p=None): return 1 if p is None else p(1)
def two(p=None): return 2 if p is None else p(2)
def three(p=None): return 3 if p is None else p(3)
def four(p=None): return 4 if p is None else p(4)
def five(p=None): return 5 if p is None else p(5)
def six(p=None): return 6 if p is None else p(6)
def seven(p=None): return 7 if p is None else p(7)
def eight(p=None): return 8 if p is None else p(8)
def nine(p=None): return 9 if p is None else p(9)
def plus(x): return lambda y: y + x
def minus(x): return lambda y: y - x
def times(x): return lambda y: y * x
def divided_by(x): return lambda y: y // x

