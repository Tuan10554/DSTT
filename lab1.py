danhsach1=[1.,3.]
danhsach2=[5.,7.]
danhsach=danhsach1+danhsach2
print(danhsach)
danhsach_gapdoi=2*danhsach
print(danhsach_gapdoi)
mon_hoc=["ToanCC","DSTT","ToanRR","LaptrinhCB"]
thu_tu=[2,3,4,1]
diem_so=[10,9,8,7]
anh_xa = list(zip(thu_tu, mon_hoc, diem_so))
print(anh_xa)
tap_hop = set(anh_xa)
print(tap_hop)
lay_TT, lay_monhoc, lay_diem = zip(*anh_xa)
print(lay_monhoc)
import itertools
tap_sinh=list(itertools.chain(range(4),range(5,10),range(15,20)))
print(tap_sinh)
print(list(zip(range(4),range(7,12),reversed(range(11)))))
mylist=[100,200,300]
a,b,c=mylist
print( a,b ,c)
a=b=c=0
mylist=[]
#exec('c:/lab1.py')

def tao_danhsach():
    danhsach=[100,200,300]
    return danhsach
from lab1 import tao_danhsach
mylist= tao_danhsach()
a,b,c = mylist
print( a, b,c)
from sympy import Symbol
x= Symbol('x')
f= x+x+x+2
print(f)
a= Symbol("Noi")
b=Symbol('Chim')
print(3*b+7*a)
print(a.name)
print(b.name)
x= Symbol('x')
y=Symbol('y')
z=Symbol('z')
from sympy import symbols
a,b,c = symbols ('a,b,c')
from sympy import Symbol
x= Symbol('x')
y=Symbol('y')
s=x*y+y*x
print(s)
p= x*(x+2*x)
print(p)
p= (x+2)*(y+3)
print(p.expand())

from sympy import factor
bieuthuc=x**3 - y**3
factor(bieuthuc)

from sympy import expand
bieuthuc1=(x-y)*(x**2+x*y+y**2)
print(expand(bieuthuc1))

from sympy import pprint
bieuthuc2=x*x - 2*x*y + y**2
pprint(bieuthuc2)

from sympy import pprint
from sympy import init_printing
init_printing(order='rev-lex')
bieuthuc3=x*x-2*x*y + y**2
pprint(bieuthuc3)
bieuthuc4=factor(bieuthuc3)
pprint(bieuthuc4)

from sympy import Symbol
x=Symbol('x')
y=Symbol('y')
bieuthuc5=x*x-x*y+y*y
print(bieuthuc5)

giatri=bieuthuc.subs({x:3,y:2})
print(giatri)

giatri1=bieuthuc.subs({x:3,y:x})
print(giatri1)

giatri2=bieuthuc.subs({x:y,y:3})
print(giatri2)
giatri3=bieuthuc.subs({y:x}).subs({x:3})
print(giatri3)

from sympy import Symbol
x=Symbol('x')
y=Symbol('y')
bieuthuc6=x*x-x*y+y*y
print(bieuthuc6)
bieuthuc_moi=bieuthuc.subs({x:1-y})
print(bieuthuc_moi)

from sympy import simplify
dongian=simplify(bieuthuc_moi)
print(dongian)

from sympy import Symbol
from sympy import sin,cos
x= Symbol('x')
y=Symbol('y')
bt=sin(x)*cos(y)+cos(x)*sin(y)
bt_moi=simplify(bt)
print(bt_moi)

import numpy as np
vec1=np.array([1.,3.,5.])
print(vec1*2)
print(vec1*vec1)
print(vec1/2)
print(vec1+vec1)
vec2= np.array([2.,4.])
print(vec1+vec2)
vec3=np.array([2.,4.,6.])
print(vec1+vec3)
print(vec1/vec3)
print(vec1*vec3)
print(5*vec1 + 5*vec3)
print(vec3[[2]])
vec4=np.linspace(0,20,5)
print(vec4)
print(vec5=np.zeros(5))
print(vec6=np.ones(5))
print(vec7=np.empty(5))
print(np.rand(5))

v=np.array([1.,3.,5.])
print(np.sum(v))
print(v.shape)
print(v.transpose())
v1=v[:2]
print(v1)
v[0]=5
print(v)
v1[:2]=[1.,2.,3.]
v1[:2]=[1.,2]
print(v)
v3= 2*v[:2]+v1*3
print(v3)
v1=[4,6]
print(v+10.0)
print(np.sqrt(v))
print(cos(v))
print(sin(v))

np.dot(v1,v3)
v1.dot(v3)
v3.dot(v1)

