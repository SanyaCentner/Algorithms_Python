"""Start and check operation"""


from sortings import sortings
from data_structure import simple_structure


if __name__ == '__main__':
    stack = simple_structure.Stack(3)
    print(stack.lst)
    stack.push(2)
    stack.push(3)
    print(stack.lst)
    print(stack.pop(), stack.lst)
    stack.push(2)
    stack.push(4)
    print(stack.lst)
    stack.push(2)
    print(stack.pop(), stack.lst)
    stack.push(3)
    print(stack.pop(), stack.lst)
    print(stack.pop(), stack.lst)
    print(stack.pop(), stack.lst)
    print(stack.pop(), stack.lst)
    print(stack.pop(), stack.lst)
    print('Queue')
    queue = simple_structure.Queue(3)
    print(queue.lst)
    queue.push(2)
    queue.push(3)
    print(queue.lst)
    print(queue.pop(), queue.lst)
    queue.push(2)
    queue.push(4)
    print(queue.lst)
    queue.push(2)
    print(queue.pop(), queue.lst)
    queue.push(3)
    print(queue.pop(), queue.lst)
    print(queue.pop(), queue.lst)
    print(queue.pop(), queue.lst)
    print(queue.pop(), queue.lst)
    print(queue.pop(), queue.lst)

