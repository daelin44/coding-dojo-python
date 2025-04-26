# TODO: + пустой input
# TODO: + 1 значение в input
# TODO: + n значений в input
# TODO: + добавление разделителя \n
# TODO: + поддержка разных разделителей
# TODO: поддержка отрицательных чисел

import string_adder
def test_string_adder_returns_zero_null_input():
    assert string_adder.add() == 0

def test_string_adder_returns_single_value_in_input():
    assert string_adder.add("1") == 1

def test_string_adder_returns_two_values_in_input():
    assert string_adder.add("1,2") == 3

def test_string_adder_returns_n_delimiter_in_input():
    assert string_adder.add("1,2\n3") == 6

def test_string_adder_returns_custom_delimiter_in_input():
    assert string_adder.add("//;\n1;2") == 3

def test_string_adder_returns_error_for_negative_in_input():
    assert string_adder.add("-1,2") == "error: negative numbers not allowed"
