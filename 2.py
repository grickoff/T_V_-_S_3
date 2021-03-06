# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?

from math import factorial
def f(n, k):
    return int(factorial(n)/(factorial(k)*factorial(n - k)))

AA = ((f(5, 3)/f(12, 4))*(f(3, 2)/f(8, 2))) # все три белых меча из второго ящика (0.0010822510822510823)
Aa = ((f(5, 2)/f(12, 4))*(f(5,1)/f(8, 2))) # 2 из второго и 1 из первого (0.003607503607503608)
aa = ((f(5,1)/f(12, 4))*(f(5,2)/f(8,2))) # 1 из второго и 2 из первого()

print(AA+Aa+aa)

#Какова вероятность того, что 3 мяча белые? (0.00937950937950938)