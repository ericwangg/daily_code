def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(pair):
    def pair(a,b):
        return a
    return f(pair)

def cdr(pair):
    def pair(a,b):
        return b
    return f(pair)

if __name__ == '__main__':
    car(cons(3,4))
    cdr(cons(3,4))
    car(cons(6, 5, 4))
    cdr(cons(4, 5, 6))
