"""

nom: Mani
prenom: Khaled
TP4
group: G1.1


"""

#exercice n° 01

class Fib:
 def suit_fibonacci (self, n):
    a, b = 1, 1 
    for _ in range (n):
        yield a
        a, b =b, a+b 
        #exemple

       # for num in fib.suite_fibonacci(10)
    
 def super_impair(k):
    chiffres_pairs = [chiffre for chiffre in str(k) if chiffre in '02468']
    return len(chiffres_pairs) == 0
"""# exemp
n = 10
super_impair = list(super_impairs(n))
print(super_impair)"""

#exercice n° 02

class Octant:
    def __init__(self, n, d=0):
        self.n = n
        self.cone = [[d] * (n - i) for i in range(n)]

    def check(self, x, y):
        if not (0 <= y <= x < self.n):
            raise IndexError("Les coordonnées x, y ne satisfont pas 0 ≤ y ≤ x < n")

    def get(self, x, y):
        self.check(x, y)
        return self.cone[x][y]

    def set(self, x, y, d):
        self.check(x, y)
        self.cone[x][y] = d
    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.cone)
