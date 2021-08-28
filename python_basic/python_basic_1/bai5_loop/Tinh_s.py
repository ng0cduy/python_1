print ('calculate the result of the polynominal (x^2+1)^n')
n = int(input('input a power integer n:\n'))
x = float(input('input a number x:\n'))
S=1
while (n>0):
    S *=(x**2 + 1)
    n-=1
if (S%1==0):
    print ('the result is S = %d'%S)
else:
    print ('the result is S = %.3f' %S)