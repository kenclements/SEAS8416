import funct3

a = 1
b = 2

for i in range(2):
    a = i

def funct2():
    k = 23
    funct3.funct3()
    return

def funct1():
    for i in range(3):
        global c
        a = i
        c = 3
        d = 6
        funct2()
    return

funct1()