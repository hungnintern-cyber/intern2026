def ex_6_1():
    print("--Exercise 6.1")
    dic = {'V':'Next','VietNam':'Japan'}
    print(dic)

def ex_6_2():
    print("\n--Exercise 6.2")
    lst = [1,2,42,2,6,7,9,1]
    dic = {}
    for i in lst:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1    
    print(dic)

def ex_6_3():
    print("\n--Exercise 6.3")
    lst = [1,2,42,2,6,7,9,1]
    dic = {}
    for i in lst:
        # dùng get kiểm tra có i trong dic không
        # nếu không thì thì trả ra value default là 0 -> 0 + 1
        # nếu đã có thì trả ra value hiện tại -> value(>0) +1 
        dic[i] = dic.get(i, 0) + 1
    print(dic)    

if __name__ == "__main__":
    ex_6_1()
    ex_6_2()
    ex_6_3()