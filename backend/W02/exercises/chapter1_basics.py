def ex_1_1_and_1_2():
    print("--Exercise 1.1 & 1.2")
    print("3 + 1 =",3+1) # in ra phép cộng
    print("3 * 3 =",3*3) # in ra phép nhân
    print("2 ** 3 =",2**3) # in ra lũy thừa
    print("Hello, world!") ## in ra chuỗi

def ex_1_3():
    print("\n--Exercise 1.3")
    # phép cộng chuỗi
    print("'py' + 'thon' =",'py'+'thon')

    # nhân bản py 3 lần sau đó cộng chuỗi
    print("'py' * 3 + 'thon' =",'py'*3+'thon')

    # python không hỗ trợ phép - cho string
    #print("'py' - 'py' =",'py'-'y') # dòng này lỗi, nên comment lại

    # python không cho phép cộng khác kiểu dữ liệu
    #print("'3' + '3' =",'3'+3) # dòng này lỗi, nên comment lại

    # nhân bản 3 lần chuỗi 3 
    print("3 * '3' =",3*'3')        

    # lỗi a chưa được định nghĩa
    #print(a) # dòng này lỗi, nên comment lại

    # gắn giá trị 3 cho biến a
    a = 3

    # in ra a = 3
    print("a =",a)

def ex_1_4():
    print("\n--Exercise 1.4")
    # True vì 1=1
    print("1 == 1 :",1==1) 

    # Vì kiểu bool là một dạng con của int,True là 1 False là 0
    print("1 == True :",1==True) # True 
    print("0 == True :",0==True) # False 

    # True vì 3 = 1*3
    print("3 == 1 * 3 :",3==1*3)  

    # 0 vì False = 0, *3 cũng = 0
    print("(3 == 1) * 3 :",(3 == 1) * 3) 

    # False vì True = 1, *4+3 = 7
    print("(3 == 3) * 4 + 3 == 1 :",(3 == 3) * 4 + 3 == 1) 

    # False vì 15 < 16
    print("3**5 >= 4**4 :",3**5 >= 4**4) 

def ex_1_5():
    print("\n--Exercise 1.5")

    # toán tử / luôn thực hiện phép chia thực
    print("5 / 3 =",5 / 3)

    # toán tử % chia lấy dư
    print("5 % 3 =",5 % 3) 

    # toán tử / luôn thực hiện phép chia thực
    print("5.0 / 3 =",5.0 / 3)

    # toán tử / luôn thực hiện phép chia thực
    print("5 / 3.0 =",5 / 3.0)

    # toán tử % chia lấy dư
    # nhưng toán tử % sau khi chia lấy phần nguyên
    # 5.2/3 ≈gần = 1.72 -> lấy 1 
    # 5.2 - (1*3) = 2.2
    print("5.2 % 3 =",5.2 % 3) # in ra 2.2

    #toán tử lũy thừa
    print("2001 ** 200 =",2001 ** 200)

def ex_1_6():
    print("\n--Exercise 1.6")
    # Kết quả sẽ quá lớn OverflowError
    #print("2000.3 ** 200 =",2000.3 ** 200) # dòng này lỗi, nên comment lại
    
    # số nhỏ float ra kết quả chính xác
    print("1.0 + 1.0 -1.0 =",1.0 + 1.0 -1.0)  

    # 1.0e20 là số cực lớn, 1.0 quá nhỏ
    # float chỉ lưu đc khoảng 15-16 chữ số
    # nên 1.0 có thể bị mất do làm tròn
    print("1.0 + 1.0e20 -1.0e20 =",1.0 + 1.0e20 -1.0e20)  

def ex_1_7():
    print("\n--Exercise 1.7") 
    name = "Hung"
    print("Hello, "+name+"!") 

def ex_1_8():
    print("\n--Exercise 1.8:")

    # chuyển số nguyên 123 sang số thực 123.0
    print("float(123) ->",float(123))

    # chuỗi số nguyên '123' sang số thực 123.0
    print("float('123') ->",float('123'))

    # chuỗi số thực '123.23' sang số thực 123.23
    print("float('123.23') ->",float('123.23')) 

    # chuyển số thực 123.23 sang số nguyên 123
    print("int(123.23) ->",int(123.23)) 

    # ValueError int không chấp nhận ép chuỗi số thập phân
    #print("int('123.23') ->",int('123.23')) # dòng này lỗi nên comment lại

    # chuỗi số thực '123.23' sang số thực 123.23
    # sau đó, chuyển số thực 123.23 sang số nguyên 123
    print("int(float('123.23')) ->",int(float('123.23')))

    # chuyển số nguyên thành chuỗi
    print("str(12) ->", str(12)) 

    # chuyển số thực thành chuỗi
    print("str(12.2) ->",str(12.2))

    # True, chuỗi ko rỗng
    print("bool('a') ->",bool('a'))    

    # False, vì số 0 coi là False
    print("bool(0) ->",bool(0))  

    # True, vì khác 0 coi là True           
    print("bool(0.1) ->",bool(0.1))        

if __name__ == "__main__":
    ex_1_1_and_1_2()
    ex_1_3()
    ex_1_4()
    ex_1_5()
    ex_1_6()
    ex_1_7()
    ex_1_8()