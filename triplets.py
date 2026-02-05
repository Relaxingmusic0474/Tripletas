# Definiré una clase Tripleta en base a las propiedades y operaciones que tiene una
class Triplet:
    # Se inicializan los atributos aplicando encapsulamiento
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    # Getters
    def a(self):
        return self.__a
    def b(self):
        return self.__b
    def c(self):
        return self.__c
    
    # Setters
    def set_a(self, new_value):
        self.__a = new_value
    def set_b(self, new_value):
        self.__b = new_value
    def set_c(self, new_value):
        self.__c = new_value

    # Suma
    def __add__(self, T:"Triplet"):
        return Triplet(self.a() + T.a(),
                       self.b() + T.b(),
                       self.c() + T.c())
    
    # Resta rara
    def __sub__(self, T:"Triplet"):
        return Triplet(self.a() + T.c(),
                       self.b() - T.b(),
                       self.c() + T.a())
    
    # Multiplicación rara
    def __mul__(self, T:"Triplet"):
        ab = self.a()*self.b()
        cf = self.c()*T.c()
        be = self.b()*T.b()
        return Triplet(min(ab, cf), be, max(ab, cf))
    
    # Multiplicación por un real
    def __rmul__(self, r:float):
        if r > 0:
            return Triplet(r*self.a(), 
                           r*self.b(), 
                           r*self.c())
        
        elif r == 0:
            return Triplet(0, 0, 0)
        
        else:
            return Triplet(r*self.c(),
                           r*self.b(),
                           r*self.a())
    
    # Orden estricto
    def __lt__(self, T: "Triplet"):
        if self.b() != T.b():
            return self.b() < T.b()
        if self.a() != T.a():
            return self.a() < T.a()
        return self.c() < T.c()
    
    # Orden no estricto
    def __le__(self, T: "Triplet"):
        if self.b() != T.b():
            return self.b() < T.b()
        if self.a() != T.a():
            return self.a() < T.a()
        return self.c() <= T.c()
        
    # Para imprimir una tripleta
    def __repr__(self):
        return f"({self.a()}, {self.b()}, {self.c()})"
    

def distance(T1: "Triplet", T2: "Triplet") -> float:
    candidates = [abs(T1.a() - T2.a()), abs(T1.b() - T2.b()), abs(T1.c() - T2.c())]
    d = min(candidates)
    return d

def minor_triplet(T1: "Triplet", T2: "Triplet") -> Triplet:
    if T1.b() < T2.b():
        return T1
    if T1.b() == T2.b() and T1.a() < T2.a():
        return T1
    if T1.b() == T2.b() and T1.a() == T2.a() and T1.c() < T2.c():
        return T1
    return T2

def major_triplet(T1: "Triplet", T2: "Triplet") -> Triplet:
    if minor_triplet(T1, T2) is T1:
        return T2
    else:
        return T1