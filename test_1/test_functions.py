import pytest

import Functions_1 as Numericals

def test_add():
    result = Numericals.add(number_one:1) + (number_two:2)
    assert result == 3


def test_add_strings():
    result = Numericals.add (number_one:"Grain crops" ) + (number_two:"and vegitable ")
    assert result == "Grain crops and vegitables"
