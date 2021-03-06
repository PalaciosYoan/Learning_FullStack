import numpy as np
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