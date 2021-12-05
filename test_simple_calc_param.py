import simple_calc
import pytest

dataset_for_add_func = [
    (3, 5, 8),
    (4, 6, 10),
    (10, 10, 20)
]

dataset_for_subtract_func = [
    (5, 2, 3),
    (10, 6, 4),
    (20, 10, 10)
]

dataset_for_multiple_func = [
    (5, 2, 1),
    (10, 6, 60),
    (20, 10, 200)
]

dataset_for_add_string = [
    ("田中", "よしこ", "苗字は田中です。名前はよしこです。"),
    ("吉田", "よしこ", "苗字は吉田です。名前はよしこです。"),
    ("佐藤", "よしこ", "苗字は佐藤です。名前はよしこです。"),
]


@pytest.mark.parametrize('param1,param2,result',dataset_for_add_func)
def test_add_func(param1, param2, result):
    assert simple_calc.add_func(param1, param2) == result

@pytest.mark.parametrize('param1,param2,result',dataset_for_subtract_func)
def test_subtract_func(param1,param2,result):
    assert simple_calc.subtract_func(param1,param2) == result

@pytest.mark.parametrize('param1,param2,result',dataset_for_multiple_func)
def test_multiple_func(param1,param2,result):
    assert simple_calc.multiple_func(param1,param2) == result

@pytest.mark.parametrize('param1,param2,result',dataset_for_add_string)
def test_add_string(param1,param2,result):
    assert simple_calc.add_string(param1,param2) == result
