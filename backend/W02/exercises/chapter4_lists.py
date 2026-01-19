def ex_4_1_a(x):
    print("--Exercise 4.1.a")
    for i in x:
        print(i, end=" ") 
    print()    
    return x

def ex_4_1_b(x):
    print("\n--Exercise 4.1.b")
    list_dao_nguoc = x[::-1]
    for i in list_dao_nguoc:
        print(i, end=" ")     
    print()     
    return list_dao_nguoc

def ex_4_1_c(x):
    print("\n--Exercise 4.1.c")
    length = len(x)
    print("so luong phan tu la",len(x))  
    return length   

def ex_4_2():
    print("\n--Exercise 4.2")
    a = [1,3,2,5]     
    b = a  
    b[1] = 20
    # a bị thay đổi vì cả a và b cùng trỏ đến 1 nơi
    print(a)
    #a lúc này = [1,20,2,5] 
    c = a[:]
    c[2] = 10
    # a không thay đổi vì c đang copy thành list mới
    print(a)

def ex_4_2_set_first_elem_to_zero(x):
    print("\n--Exercise 4.2.set_first_elem_to_zero")
    x[0] = 0
    return x

def ex_4_3():
    print("\n--Exercise 4.3")
    # tạo 1 list rồi tham chiếu 3 lần
    a = [[]] * 3
    a[0].append(1)
    # kết quả [[1], [1], [1]] , cả 3 phần tử cùng trỏ đến 1 chỗ
    print(a)

    # tạo 3 list khác nhau
    b = [[] for _ in range(3)]     
    b[0].append(1)
    # kết quả [[1], [], []] , chỉ phần tử đầu thay đổi
    print(b) 

def ex_4_4(x,index):
    print("\n--Exercise 4.4")
    if 0 <= index < len(x): # kiem tra pham vi dau vao
        x[index] = 0
    else:
        print("nam ngoai pham vi")
    return x

if __name__ == "__main__":
    x = [1,3,5,7,8,6,4,7,9,0,10]
    ex_4_1_a(x)
    ex_4_1_b(x)
    ex_4_1_c(x)
    ex_4_2()
    print(ex_4_2_set_first_elem_to_zero(x))
    ex_4_3()
    y = [1,3,5,7,8,6,4,7,9,0,10]
    print(ex_4_4(y,2))