
def test_a1():
    assert 4 < 5

def test_a2():
    assert 1

def test_a3():
    assert "abcd" == 'abcd'

def test_a4():
    assert ((3-1)*4/2) == 4.0  #4.0 bo jest dzielenie i przeszło na floata, bez głównyh nawiasów będzie 1.0 !!!

def test_a5():
    assert 1 in divmod(9,5)  # wynikiem tego jest tupla (1,4) i tak 1 się w tym zawiera, jest to wynik i reszta jak przy / a potem %

def test_a6():
    assert 'py' in 'this is pytest'

def test_a7():
    assert 'put' not in 'this is pytest'

def test_a8():
    assert [1,2] in [1,2,3]
