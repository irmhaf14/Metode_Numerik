import math
def f(x) :
    return math.exp(x) - 5*x**2


a = 2
b = 9
e = 0.00021
N = 50
iterasi = 0

print('======================')
print('C                 f(c)')
print('======================')
while True :
    iterasi += 1
    c = (a + b)/2
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
    print('{:7.5f} \t {:15.10f}' .format(c, f(c)))
    if abs(f(c)) < e or iterasi >= N:
        break
    print('============')