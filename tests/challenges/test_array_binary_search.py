from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch


# Happy Path
def test_BinarySearch_1():
    actual= BinarySearch([2,4,6,8,9,12,15,16,18,20],16)
    expected= 7
    assert actual==expected

def test_BinarySearch_2():
    actual= BinarySearch([4,8,15,23,42,55,64,69],8)
    expected= 1
    assert actual==expected


# Expected failure

def test_BinarySearch_3():
    actual= BinarySearch([4,8,15,23,42,55,64,69],3)
    expected= 'Sorry Invailed Input'
    assert actual==expected

# # Edge Cases

def test_BinarySearch_4():
    actual= BinarySearch('error', 4)
    expected= 'Please Insert An Array'
    assert actual==expected


def test_BinarySearch_5():
    actual= BinarySearch([4,8,15,23,42,55,64,69], 'not number')
    expected= 'Please Insert A Number'
    assert actual==expected
