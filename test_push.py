# TODO: + пустой input
# TODO: 1 значение в input

import string_adder
def test_string_adder_returns_zero_null_input():
    assert string_adder.add() == 0

def test_string_adder_returns_single_value_in_input():
    assert string_adder.add("1") == 1


