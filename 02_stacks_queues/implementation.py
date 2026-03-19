"""
Stack & Queue — From-Scratch Implementation
============================================
Implements:
  - ArrayStack       : stack backed by dynamic array
  - LinkedStack      : stack backed by linked list
  - CircularQueue    : queue backed by circular buffer (fixed capacity)
  - LinkedQueue      : queue backed by linked list
  - Deque            : double-ended queue

No collections.deque or queue.Queue used.
"""

from __future__ import annotations
from typing import Any, Optional


# ──────────────────────────────────────────────
# Stack — Array-backed
# ──────────────────────────────────────────────

class ArrayStack:
    """
    LIFO stack using a Python list as the underlying array.

    All core operations are O(1) amortised (push) or O(1) worst-case.
    Python list.append / list.pop(-1) are already amortised O(1),
    but we implement our own to make the mechanics explicit.
    """

    def __init__(self) -> None:
        self._data: list = []

    def push(self, val: Any) -> None:
        """O(1) amortised."""
        self._data.append(val)

    def pop(self) -> Any:
        """O(1). Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any:
        """O(1). View top without removing."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"ArrayStack(top → {self._data[::-1]})"


# ──────────────────────────────────────────────
# Stack — Linked-list-backed
# ──────────────────────────────────────────────

class _Node:
    __slots__ = ("val", "next")
    def __init__(self, val: Any, next: Optional[_Node] = None):
        self.val = val
        self.next = next


class LinkedStack:
    """
    LIFO stack using a singly linked list.
    Push and pop operate on the head — both O(1) worst-case.
    No amortisation needed; no resizing.
    """

    def __init__(self) -> None:
        self._head: Optional[_Node] = None
        self._size: int = 0

    def push(self, val: Any) -> None:
        """O(1)."""
        self._head = _Node(val, self._head)
        self._size += 1

    def pop(self) -> Any:
        """O(1)."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        val = self._head.val
        self._head = self._head.next
        self._size -= 1
        return val

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._head.val

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        vals, cur = [], self._head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return "top → " + " → ".join(map(str, vals))


# ──────────────────────────────────────────────
# Queue — Circular Buffer
# ──────────────────────────────────────────────

class CircularQueue:
    """
    FIFO queue backed by a fixed-size circular buffer.

    Uses two pointers (head, tail) and a count to distinguish
    full from empty — avoids the classic off-by-one confusion.

    All operations O(1) worst-case.
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._data: list = [None] * capacity
        self._head = 0          # index of front element
        self._tail = 0          # index where next enqueue goes
        self._count = 0

    def enqueue(self, val: Any) -> None:
        """O(1). Raises if full."""
        if self._count == self._capacity:
            raise OverflowError("queue is full")
        self._data[self._tail] = val
        self._tail = (self._tail + 1) % self._capacity
        self._count += 1

    def dequeue(self) -> Any:
        """O(1). Raises if empty."""
        if self._count == 0:
            raise IndexError("dequeue from empty queue")
        val = self._data[self._head]
        self._data[self._head] = None   # release reference
        self._head = (self._head + 1) % self._capacity
        self._count -= 1
        return val

    def front(self) -> Any:
        if self._count == 0:
            raise IndexError("front of empty queue")
        return self._data[self._head]

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == self._capacity

    def __len__(self) -> int:
        return self._count

    def __repr__(self) -> str:
        items = [self._data[(self._head + i) % self._capacity]
                 for i in range(self._count)]
        return f"CircularQueue(front → {items})"


# ──────────────────────────────────────────────
# Queue — Linked List
# ──────────────────────────────────────────────

class LinkedQueue:
    """
    FIFO queue using a singly linked list with head + tail pointers.
    Enqueue at tail O(1), dequeue at head O(1).
    """

    def __init__(self) -> None:
        self._head: Optional[_Node] = None
        self._tail: Optional[_Node] = None
        self._size: int = 0

    def enqueue(self, val: Any) -> None:
        """O(1)."""
        node = _Node(val)
        if self._tail:
            self._tail.next = node
        self._tail = node
        if self._head is None:
            self._head = node
        self._size += 1

    def dequeue(self) -> Any:
        """O(1)."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        val = self._head.val
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return val

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._head.val

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        vals, cur = [], self._head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return "front → " + " → ".join(map(str, vals))


# ──────────────────────────────────────────────
# Deque — Double-ended Queue
# ──────────────────────────────────────────────

class Deque:
    """
    Double-ended queue: O(1) push/pop at both front and back.
    Backed by a doubly linked list (sentinel nodes).

    Common use: sliding window maximum (monotonic deque).
    """

    class _DNode:
        __slots__ = ("val", "prev", "next")
        def __init__(self, val):
            self.val = val
            self.prev = self.next = None

    def __init__(self) -> None:
        self._head = self._DNode(None)
        self._tail = self._DNode(None)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def _insert_after(self, node, val):
        new = self._DNode(val)
        new.prev, new.next = node, node.next
        node.next.prev = new
        node.next = new
        self._size += 1

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node.val

    def push_front(self, val: Any) -> None:
        self._insert_after(self._head, val)

    def push_back(self, val: Any) -> None:
        self._insert_after(self._tail.prev, val)

    def pop_front(self) -> Any:
        if self.is_empty():
            raise IndexError("pop_front from empty deque")
        return self._remove(self._head.next)

    def pop_back(self) -> Any:
        if self.is_empty():
            raise IndexError("pop_back from empty deque")
        return self._remove(self._tail.prev)

    def peek_front(self) -> Any:
        return self._head.next.val

    def peek_back(self) -> Any:
        return self._tail.prev.val

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size


# ──────────────────────────────────────────────
# Classic application: monotonic stack
# ──────────────────────────────────────────────

def next_greater_element(nums: list[int]) -> list[int]:
    """
    For each element, find the next element that is greater.
    Returns -1 if none exists.

    Monotonic stack pattern — O(n) time, O(n) space.

    Example: [2, 1, 2, 4, 3] → [4, 2, 4, -1, -1]
    """
    n = len(nums)
    result = [-1] * n
    stack = ArrayStack()   # stores indices

    for i in range(n):
        while not stack.is_empty() and nums[i] > nums[stack.peek()]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.push(i)

    return result


# ──────────────────────────────────────────────
# Smoke test
# ──────────────────────────────────────────────

if __name__ == "__main__":
    print("── ArrayStack ──")
    s = ArrayStack()
    for v in [1, 2, 3]:
        s.push(v)
    print(s)
    print("pop:", s.pop())
    print(s)

    print("\n── CircularQueue ──")
    q = CircularQueue(4)
    for v in [10, 20, 30]:
        q.enqueue(v)
    print(q)
    print("dequeue:", q.dequeue())
    q.enqueue(40)
    print(q)

    print("\n── LinkedQueue ──")
    lq = LinkedQueue()
    for v in ['a', 'b', 'c']:
        lq.enqueue(v)
    print(lq)
    print("dequeue:", lq.dequeue())

    print("\n── Deque ──")
    dq = Deque()
    dq.push_back(1)
    dq.push_back(2)
    dq.push_front(0)
    print("front:", dq.peek_front(), "back:", dq.peek_back())

    print("\n── Monotonic Stack ──")
    print(next_greater_element([2, 1, 2, 4, 3]))  # [4, 2, 4, -1, -1]
