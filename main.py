"""

nom: Mani
prenom: Khaled
TP1
group: G1.1


"""
def suit_fibonacci(n):
    a, b = 1, 1 
    for _ in range (n):
        yield a
        a, b =b, a+b 