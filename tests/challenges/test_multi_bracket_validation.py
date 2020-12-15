from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation_1():
    actual= multi_bracket_validation('(ahmad)')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_2():
    actual= multi_bracket_validation(f'{{}}')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_3():
    actual= multi_bracket_validation(f'{{}}(){{}}')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_4():
    actual= multi_bracket_validation('()[[Extra Characters]]')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_5():
    actual= multi_bracket_validation(f'(){{}}[[]]')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_6():
    actual= multi_bracket_validation(f'{{}}{{Code}}[Fellows](())')
    expected= True
    assert actual==expected

def test_multi_bracket_validation_7():
    actual= multi_bracket_validation(f'[({{}}]')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_8():
    actual= multi_bracket_validation('(](')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_9():
    actual= multi_bracket_validation('{(})')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_10():
    actual= multi_bracket_validation('{([(asd[)]]})')
    expected= False
    assert actual==expected

def test_multi_bracket_validation_11():
    actual= multi_bracket_validation(f'({{]}})')
    expected= False
    assert actual==expected
