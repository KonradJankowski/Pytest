

const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) +32
    return fah

# print(cent_to_fah())

def test_type():
    assert type(const) == float

def test_type_another_type():
    assert cent_to_fah() == 32

