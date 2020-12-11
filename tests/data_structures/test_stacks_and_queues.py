from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import (Stack,Queue)

import pytest

# Can successfully push onto a stack
def test_push(fixed_stack):
    assert fixed_stack.top.value == 5
    fixed_stack.push(3)
    assert fixed_stack.top.value == 3
# Can successfully push multiple values onto a stack
def test_push_multi(fixed_stack):
    fixed_stack.push(3)
    fixed_stack.push(1)
    assert fixed_stack.top.value == 1
    assert fixed_stack.top.next.value == 3
# Can successfully pop off the stack
def test_pop(fixed_stack):
    assert fixed_stack.top.value == 5
    assert fixed_stack.pop() == 5
    assert fixed_stack.top.value == 7
# Can successfully empty a stack after multiple pops
def test_pop_all(fixed_stack):
    fixed_stack.pop()
    fixed_stack.pop()
    fixed_stack.pop()
    assert fixed_stack.top == None
# Can successfully peek the next item on the stack
def test_peek(fixed_stack):
    assert fixed_stack.peek() == 5
# Can successfully instantiate an empty stack
def test_is_empty(fixed_stack):
    assert fixed_stack.isEmpty() == False
# Calling pop or peek on empty stack raises exception
def test_call_empty(fixed_stack):
    fixed_stack.pop()
    fixed_stack.pop()
    fixed_stack.pop()
    assert fixed_stack.pop() == 'Empty Stack'
    assert fixed_stack.peek() == 'Empty Stack'


# Can successfully enqueue into a queue
def test_enqueue(fixed_Queue):
    assert fixed_Queue.rear.value == 5
    fixed_Queue.enqueue(3)
    assert fixed_Queue.rear.value == 3
# Can successfully enqueue multiple values into a queue
def test_enqueue_multi(fixed_Queue):
    fixed_Queue.enqueue(3)
    fixed_Queue.enqueue(1)
    assert fixed_Queue.rear.value == 1
# Can successfully dequeue out of a queue the expected value
def test_dequeue(fixed_Queue):
    assert fixed_Queue.dequeue() == 9
    assert fixed_Queue.front.value == 7
# Can successfully peek into a queue, seeing the expected value
def test_peek_Q(fixed_Queue):
    assert fixed_Queue.peek() == 9
    assert fixed_Queue.front.value == 9
# Can successfully empty a queue after multiple dequeues
def test_emptying(fixed_Queue):
    fixed_Queue.dequeue()
    fixed_Queue.dequeue()
    fixed_Queue.dequeue()
    assert fixed_Queue.isEmpty() == True
# Can successfully instantiate an empty queue
def test_is_empty_Q(fixed_Queue):
    assert fixed_Queue.isEmpty() == False
# Calling dequeue or peek on empty queue raises exception
def test_emptying_exception(fixed_Queue):
    fixed_Queue.dequeue()
    fixed_Queue.dequeue()
    fixed_Queue.dequeue()
    assert fixed_Queue.peek() == 'Empty Queue'
    assert fixed_Queue.dequeue() == 'Empty Queue'


@pytest.fixture
def fixed_stack():
        s_stack=Stack()
        s_stack.push(9)
        s_stack.push(7)
        s_stack.push(5)
        return s_stack

@pytest.fixture
def fixed_Queue():
        q_queue=Queue()
        q_queue.enqueue(9)
        q_queue.enqueue(7)
        q_queue.enqueue(5)
        return q_queue