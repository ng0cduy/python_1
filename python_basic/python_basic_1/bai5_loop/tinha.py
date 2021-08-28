print ('calculate the result of the polynominal (x^2+x+1)^n + (x^2-x+1)^n')
n = int(input('input a power integer n:\n'))
x = float(input('input a number x:\n'))
A = 0
S1=1
S2=1
while (n>0):
    S1 *= (x**2 + x + 1)
    S2 *= (x**2 - x + 1)
    A=S1+S2
    n-=1
if (A%1==0):
    print ('the result is A = %d' %A)
else:
    print ('the result is S = %.3f' %A)
