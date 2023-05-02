
"""
Bayes é a probabilidade algo acontecer caso algo ja tenha acontecido ou seja
P(A/B) = P(B/A) * P(A) / P(B)
Probabilidade
de A acontecer      =   Probabilidade           Probabilidade de       /  Probabilidade de
caso B tenha            de B acontecer caso  X         A              /         B
acontecido              A tenha acontecido                           /


Extenendo fica

P(A/B) = P(B/A) * P(A)/ P(B/A)*P(A) + P(B/Ã)*P(Ã)
"""

def bayes(pba,pa,pb):
    pab=(pba*pa)/pb
    print(pab)

