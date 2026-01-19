import pytest
from chapter4_lists import (
    ex_4_1_a, ex_4_1_b, ex_4_1_c, 
    ex_4_2_set_first_elem_to_zero, ex_4_4
)

def test_ex_4_1_a():
    data = [1, 2, 3]
    # trả về chính nó
    assert ex_4_1_a(data) == [1, 2, 3]

def test_ex_4_1_b(): 
    data = [1, 2, 3]   
    # đảo ngược
    assert ex_4_1_b(data) == [3, 2, 1]

def test_ex_4_1_c():  
    data = [1, 2, 3]  
    # độ dài
    assert ex_4_1_c(data) == 3

def test_ex_4_2_set_first_elem_to_zero():
    data = [10, 20, 30]
    result = ex_4_2_set_first_elem_to_zero(data)
    assert result[0] == 0
    assert result == [0, 20, 30]

def test_ex_4_4():
    data1 = [5, 5, 5]
    # đổi giá trị vị trí index
    # trường hợp hợp lệ
    assert ex_4_4(data1, 1) == [5, 0, 5]
    
    data2 = [5, 5, 5]
    # trường hợp index sai
    # sẽ in ra "nam ngoai pham vi" và trả về list cũ
    assert ex_4_4(data2, 99) == [5, 5, 5]