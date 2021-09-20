import numpy as np


def part1():
    m = np.arange(2,10).reshape(4,2)
    print(m)


    m = np.zeros((8,8))
    i = 0
    for r in m:
        r[i::2] = 1
        if i == 0:
            i = 1
        else:
            i = 0
    print(m)
    
    List = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
    List = set(List)
    print(List)
    
    List = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
    List = [x for x in List if x > 37]
    print(List)
    
    List = [0, 12, 45.21 ,34, 99.91]
    List = [c*9/5+32 for c in List]
    print(List)

def part2():
    A = np.random.randint(100, size=(3,3))
    B = np.random.randint(100, size=(3,3))
    print("----Printing A------")
    print(A)
    print("\n\n----Printing B------")
    print(B)
    print("\n\n-----A + B-----")
    print(A+B)
    print("\n\n------A X B-----")
    print(A@B)
    print("\n\n----Determinate of A------")
    print(np.linalg.det(A))
    print("\n\n-----Inverse of B--------")
    print(np.linalg.inv(B))
    print("\n\n------EigenValues of A-------")
    print(np.linalg.eig(A)[0])


part1()