def ex_3_1_a():
    print("--Exercise 3.1.a")
    print("Hello, world!")
    return "Hello, world!"

def ex_3_1_b(name):
    print("\n--Exercise 3.1.b")
    print("Hello",name)    
    return "Hello "+ name

def ex_3_1_c(name):
    print("\n--Exercise 3.1.c")
    # print in ra màn hình nhưng không trả giá trị cho hàm
    # còn return thì ngược lại
    # nếu thay print thành return thì khi được gọi không có kết quả in ra
    return "Hello "+name

def ex_3_2(x):
    print("\n--Exercise 3.2")
    print("Tinh da thuc 3x^2 - x  + 2")
    result = 3*(x**2)-x +2
    print("3 *",x,"^2 -",x,"+ 2 =",result)
    return result

def ex_3_3_a(a,b):
    print("\n--Exercise 3.3.a")
    print("tim max cua a va b bang if else")
    if a>b:
        print("max cua %d va %d la"%(a,b),a)
        return a
    else:
        print("max cua %d va %d la"%(a,b),b)  
        return b     

def ex_3_3_b(a,b):
    print("\n--Exercise 3.3.b")
    print("tim max cua a va b bang if")
    if a>=b:
        print("max cua %d va %d la"%(a,b),a)
        return a
    if a<b:
        print("max cua %d va %d la"%(a,b),b)    
        return b

def ex_3_4_a(n):
    print("\n--Exercise 3.4.a")
    print("kiem tra so",n,"co phai so nguyen to")
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True 

def ex_3_4_b(n):
    print("\n--Exercise 3.4.b")
    print("kiem tra so",n,"co phai so nguyen to")
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5,n,6):
        if n % i == 0 or n % (i + 2) == 0: #6k-1 va 6k+1
            return False
    return True

def ex_3_4_c(n):
    print("\n--Exercise 3.4.c")
    print("ham tra ve tat ca so nguyen to den",n)
    ans = []    
    for i in range(2,n+1):
        count = 0 
        for j in range(2,i):
            if i%j==0:
                count +=1
        if count == 0:
            ans.append(i)
    return ans

def ex_3_4_d(n):
    print("\n--Exercise 3.4.d")
    print("ham tra ve",n,"so nguyen to dau tien")
    ans = []    
    i = 2
    while len(ans)<n:
        count = 0
        for j in range(2,i):
            if i%j==0:
                count +=1
        if count == 0:
            ans.append(i) 
        i+=1
    return ans

if __name__ == "__main__":
    ex_3_1_a()
    ex_3_1_b('vnext')
    print(ex_3_1_c('vnext'))
    ex_3_2(5)
    ex_3_3_a(4,7)
    ex_3_3_b(3,5)
    print(ex_3_4_a(6))
    print(ex_3_4_b(11))
    print(ex_3_4_c(10))
    print(ex_3_4_d(10))