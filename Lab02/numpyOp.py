import numpy as np


def part1():
    print("Creating 4x2 matrix values 2-10")
    m = np.arange(2,10).reshape(4,2)
    print(m)

    print("\n\nChecker board of 0s and 1s")
    m = np.zeros((8,8), dtype=int)
    m[1::2, ::2] = 1
    m[::2, 1::2] = 1
    print(m)
    
    print("\n\nGetting unique values of a list")
    List = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
    print(np.unique(List))
    
    print("\n\nGetting values bigger than 37")
    List = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
    arrayList = np.array(List)
    print(arrayList[arrayList>37])
    
    print("\n\nConverting Centrigrade into Fahrenheit")
    List = [0, 12, 45.21 ,34, 99.91]
    List = np.array(List)
    print(List*((9/5))+32)

def part2():
    A = np.random.randint(100, size=(3,3))
    B = np.random.randint(100, size=(3,3))
    print("----Printing A------")
    print(A)
    print("\n\n----Printing B------")
    print(B)
    print("\n\n-----A + B-----")
    print(np.add(A,B))
    print("printing A +B")
    print(A+B)
    print("\n\n------A X B-----")
    print(np.multiply(A, B))
    print("printing A @ B")
    print(A * B)
    print("\n\n----Determinate of A------")
    print(np.linalg.det(A))
    print("\n\n-----Inverse of B--------")
    print(np.linalg.inv(B))
    print("\n\n------EigenValues of A-------")
    print(np.linalg.eig(A)[0])


part2()