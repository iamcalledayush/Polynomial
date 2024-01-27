class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)

# class Mul:
#     def __init__(self, p1, p2):
#         self.p1 = p1
#         self.p2 = p2

#     def __repr__(self):
#         if isinstance(self.p1, Add):
#             if isinstance(self.p2, Add):
#                  return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
#             return "( " + repr(self.p1) + " ) * " + repr(self.p2)
#         if isinstance(self.p2, Add):
#             return repr(self.p1) + " * ( " + repr(self.p2) + " )"
#         return repr(self.p1) + " * " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        def needs_parentheses(term):
            return isinstance(term, (Add, Sub, Div))

        left = f"( {repr(self.p1)} )" if needs_parentheses(self.p1) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if needs_parentheses(self.p2) else repr(self.p2)
        return f"{left} * {right}"
    
    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        left = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Mul)) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Mul)) else repr(self.p2)
        return f"{left} / {right}"
    
    def evaluate(self, value):
        return self.p1.evaluate(value) / self.p2.evaluate(value)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        left = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub)) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub)) else repr(self.p2)
        return f"{left} - {right}"
    
    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)



poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1)) # ouptut is 8, because: 4+3+(-1)+1*(-1*-1 + 1) = 4+3-1+2 = 8