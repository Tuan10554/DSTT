from sympy import Symbol,solve
x= Symbol('x')
bthuc=x+3 -5
print(solve(bthuc))
bthuc1=x**2 +3 -5
nghiemx=solve(bthuc1)
print(nghiemx)
print(nghiemx[0])
print(nghiemx[[1]])