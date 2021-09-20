import numpy as np


def main():
    m = np.arange(2,10).reshape(4,2)
    print(m)


    m = np.zeros((8,8))
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
    
    

main()