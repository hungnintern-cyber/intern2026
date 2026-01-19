def ex_2_1():
    print("--Exercise 2.1")

    # range(5) trả về range(0, 5)
    # for i in range(5) là lặp 5 lần từ 0 -> 4
    print("range(5):",range(5))

    # kiểu dữ liệu range
    print("type(range(5)):",type(range(5)))

def ex_2_2():
    print("\n--Exercise 2.2:")

    # in từ 0 - 100
    # end=" " để in ngang hàng
    for i in range(101): 
        print(i, end=" ") 
    print()

    # in các số chia hết cho 7 từ 0 - 100
    for i in range(101):
        if i%7==0:
            print(i, end=" ")
    print()    

    # in các số chia hết cho 5 nhưng không chia hết cho 3 từ 0 - 100
    for i in range(101):
        if i%5==0 and i%3!=0:
            print(i, end=" ")
    print() 

    # in ra các ước của từng số từ 2 - 20
    # nhưng bỏ đi 1 và chính nó
    for i in range(2,21):
        print("uoc cua", i, "(bo 1 va", i, ") la:", end=" ")
        for j in range(2,i):
            if i%j==0:
                print(j, end=" ")
        print()        

def ex_2_3():
    print("\n--Exercise 2.3:")

    # in từ 0 - 100
    # end=" " để in ngang hàng
    i = 0
    while i<=100:
        print(i, end=" ") 
        i+=1
    print()

    # in các số chia hết cho 7 từ 0 - 100
    i = 0
    while i<=100:
        if i%7==0:
            print(i, end=" ") 
        i+=1
    print()

def ex_2_5():
    print("\n--Exercise 2.5:")

    x = 11
    count = 0
    print("20 so dau tien chia het cho 5, 7, 11 la")
    while count <20:
        if x%(5*7*11)==0:
            print(x, end=" ")
            count+=1
        x+=1
    print()

def ex_2_6():
    print("\n--Exercise 2.6:")

    x = 10
    while True:
        if all(x%n == 0 for n in range(1,11)):
            print("so nho nhat chia het cho tat ca cac so tu 1-10 la",x)
            break
        x+=10

def ex_2_7():
    print("\n--Exercise 2.7:")
    x = 103
    while x != 1:
        print(x, end=" ")
        if x % 2 == 0:      # nếu chẵn
            x = x // 2 # dùng // để lấy kiểu int
        else:               # nếu lẻ
            x = 3*x + 1
    print(1)

if __name__ == "__main__":
    ex_2_1()
    ex_2_2()
    ex_2_3()
    ex_2_5()
    ex_2_6()
    ex_2_7()