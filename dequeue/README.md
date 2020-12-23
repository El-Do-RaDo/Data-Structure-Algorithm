# Dequeue
A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front and a rear, and the items remain positioned in the collection. What makes a deque different is the unrestrictive nature of adding and removing items. New items can be added at either the front or the rear. Likewise, existing items can be removed from either end. In a sense, this hybrid linear structure provides all the capabilities of stacks and queues in a single data structure. Figure 3.16 shows a deque of Python data objects. It is important to note that even though the deque can assume many of the characteristics of stacks and queues, it does not require the LIFO and FIFO orderings that are enforced by those data structures. It is up to you to make consistent use of the addition and removal operations.

## Dequeue abstract data types
The deque abstract data type is defined by the following structure and operations. A deque is structured, as described above, as an ordered collection of items where items are added and removed from either end, either front or rear. The deque operations are given below.
• Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
• add_front(item) adds a new item to the front of the deque. It needs the item and returns nothing.
• add_rear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
• remove_front() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
• remove_rear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
• is_empty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
• size() returns the number of items in the deque. It needs no parameters and returns an integer.

## Implementation of dequeue using Python
As we have done in previous sections, we will create a new class for the implementation of the abstract data type deque. Again, the Python list will provide a very nice set of methods upon which to build the details of the deque. Our implementation will assume that the rear of the deque is at position 0 in the list. you can refer to dequeue.py for the refrence.
