# Inheritance
#1 MultiLevel_Inheritance

class A:
    __skill = "Python"

class B(A):
    kjkbfd= "dsd"
class C(B):
    ffs = "fs"
    data = A.__skill
class D:
    dat = A.__skill
o = D()
print(o.data)
o = C()
# Access specifier "_" used as private will be acced by child
# but


# Multiple Inheritance

class P:
    pwe = "Parve"
class Q:
    abc = "Mukund"
    print("sdfsf")
class R (P,Q):
    Dss = "Hello"
