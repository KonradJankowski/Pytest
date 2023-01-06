import pytest


def test_case_exeption():
    with pytest.raises(Exception): # bez tego byłoby wyjątek !! ZeroDivisionError
        assert (1/0)