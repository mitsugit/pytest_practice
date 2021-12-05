import simple_calc

def test_add_func():
    assert simple_calc.add_func(1,2) == 3

def test_subtract_func():
    assert simple_calc.subtract_func(3,2) == 1

def test_multiple_func():
    assert simple_calc.multiple_func(3,2) == 6

def test_add_string():
    assert simple_calc.add_string("田中","太郎") == "苗字は田中です。名前は太郎です。"
