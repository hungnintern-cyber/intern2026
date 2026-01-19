import pytest
from chapter3_functions import (
    ex_3_1_a, ex_3_1_b, ex_3_1_c, 
    ex_3_2, ex_3_4_a, ex_3_4_b, ex_3_4_c, ex_3_4_d
)

def test_ex_3_1_a():
    assert ex_3_1_a() == "Hello, world!"

def test_ex_3_1_b():
    assert ex_3_1_b("Vnext") == "Hello Vnext"

def test_ex_3_1_c():
    assert ex_3_1_c("Python") == "Hello Python"

def test_ex_3_2():
    # 3*(2^2) - 2 + 2 = 12
    assert ex_3_2(2) == 12

def test_ex_3_4_a():
    # kiểm tra số nguyên tố
    assert ex_3_4_a(5) is True
    assert ex_3_4_a(4) is False

def test_ex_3_4_b():    
    assert ex_3_4_b(11) is True
    assert ex_3_4_b(8) is False

def test_ex_3_4_c():
    # tat ca so nguyen to den n
    assert ex_3_4_c(5) == [2, 3, 5] 

def test_ex_3_4_d():
    # n số nguyên tố đầu tiên
    assert ex_3_4_d(3) == [2, 3, 5] 