def ex_5_1(a,b):
    print("--Exercise 5.1")
    a,b = b,a
    print("a =",a)
    print("b =",b)

def ex_5_2():
    print("\n--Exercise 5.2")
    x = [1,2,3]
    y = [4,5,6]
    # ghep lai
    ghep = list(zip(x, y))
    print(ghep)
    #tach ra
    x, y = zip(*ghep) 
    x = list(x)
    y = list(y)
    print(x)
    print(y)

def ex_5_3_L1(x,y):
    print("\n--Exercise 5.3.L1")
    # tổng các độ chênh lệch tuyệt đối
    s = 0
    for xi,yi in zip(x,y):
        s += abs(xi - yi)
    print(s)

def ex_5_3_L2(x,y):
    print("\n--Exercise 5.3.L2")
    # khoảng cách đường thẳng
    s = 0
    for xi,yi in zip(x,y):
        s += (xi - yi)**2
    print(s**0.5)

if __name__ == "__main__":
    ex_5_1(3,7)
    ex_5_2()
    x = [1,4,6,8,5,9]
    y = [2,5,3,1,2,4]
    ex_5_3_L1(x,y)
    ex_5_3_L2(x,y)
