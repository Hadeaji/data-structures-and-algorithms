from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter,Cat,Dog
import pytest

def test_Animal_Shelter(fixed_shelter):
    fixed_shelter.enqueue(Dog('JOJO'))
    assert str(fixed_shelter) == f'{{Tom}}->{{Spike}}->{{Mdhat}}->{{JOJO}}->NULL'

    assert fixed_shelter.dequeue('Dog') == 'Spike'
    assert str(fixed_shelter) == f'{{Tom}}->{{Mdhat}}->{{JOJO}}->NULL'

    assert fixed_shelter.dequeue('Bird') == 'NULL'
    assert str(fixed_shelter) == f'{{Tom}}->{{Mdhat}}->{{JOJO}}->NULL'

    assert fixed_shelter.dequeue('Cat') == 'Tom'
    assert str(fixed_shelter) == f'{{Mdhat}}->{{JOJO}}->NULL'

    assert fixed_shelter.dequeue() == 'Mdhat'
    assert str(fixed_shelter) == f'{{JOJO}}->NULL'



@pytest.fixture
def fixed_shelter():
    shelter =AnimalShelter()
    shelter.enqueue(Cat('Tom'))
    shelter.enqueue(Dog('Spike'))
    shelter.enqueue(Cat('Mdhat'))
    
    return shelter