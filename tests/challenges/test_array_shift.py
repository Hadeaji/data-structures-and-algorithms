from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray


# Happy Path
def test_arrayShift_1():
    actual= insertShiftArray([2,4,6,8],5)
    expected= [2,4,5,6,8]
    assert actual==expected

def test_arrayShift_2():
    actual= insertShiftArray([4,8,15,23,42], 16)
    expected= [4,8,15,16,23,42]
    assert actual==expected


# Expected failure
# It suppose to accept all numrical values

def test_arrayShift_3():
    actual= insertShiftArray([], -10)
    expected= [-10]
    assert actual==expected

# Edge Cases

def test_arrayShift_4():
    actual= insertShiftArray('error', 4)
    expected= 'Please Insert An Array'
    assert actual==expected

def test_arrayShift_5():
    actual= insertShiftArray([2,5], 'not number')
    expected= 'Please Insert A Number'
    assert actual==expected
