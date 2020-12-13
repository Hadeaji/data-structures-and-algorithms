from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue
import pytest


def test_enqueue_and_dequeue(fixed_pseudoQueue):
    fixed_pseudoQueue.enqueue(4)
    assert fixed_pseudoQueue.dequeue() == 1
    assert fixed_pseudoQueue.dequeue() == 2
    assert fixed_pseudoQueue.dequeue() == 3
    assert fixed_pseudoQueue.dequeue() == 4
    assert fixed_pseudoQueue.dequeue() == "Can't dequeue from empty queue!"


@pytest.fixture
def fixed_pseudoQueue():
        pq=PseudoQueue()
        pq.enqueue(1)
        pq.enqueue(2)
        pq.enqueue(3)
        return pq