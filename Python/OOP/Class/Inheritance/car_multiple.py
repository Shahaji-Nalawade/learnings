class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welvome to class C"


c1 = C()
print(c1.varA, c1.varB, c1.varC)