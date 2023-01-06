import pytest


def test_case_exeption():
    with pytest.raises(ZeroDivisionError):
    # with pytest.raises(Exception): # możemy od razu wpisać jaki Exeption oczekujemy
        assert (1/0)