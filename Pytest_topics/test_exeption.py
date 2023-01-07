import pytest


def test_case_exeption():
    with pytest.raises(ZeroDivisionError):
    # with pytest.raises(Exception): # możemy od razu wpisać jaki Exeption oczekujemy
        assert (1/0)

    with pytest.raises(AssertionError):
        assert 3 > 3

def test_case_exeption_print():
    with pytest.raises(Exception) as excinfo:
        assert  (1,2,3) == (1,2,4)
    print(excinfo)

def func1():
    raise ValueError("IndexError func1 raised")

def test_case_exeption_2():
    with pytest.raises(Exception) as execinfo:
        func1()
    print(str(execinfo))
    assert (str(execinfo.value)) == 'Exception func1 raised'
