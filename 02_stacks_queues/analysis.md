# Stack & Queue — Complexity Analysis

## 1. Stack

### Operations

| Operation | ArrayStack | LinkedStack | Notes |
|-----------|-----------|-------------|-------|
| push | O(1) amortised | O(1) worst | Array doubles; linked prepends |
| pop | O(1) amortised | O(1) worst | Array shrinks at 1/4 load |
| peek | O(1) | O(1) | |
| is_empty | O(1) | O(1) | |
| Space | O(n) | O(n) + pointer overhead | |

### Amortised analysis of multi-pop (aggregate method)

Consider a sequence of n push and pop operations starting from empty.

Each element is pushed at most once and popped at most once.
Total number of pops ≤ total number of pushes ≤ n.

Therefore: total cost of all operations ≤ 2n = **O(n)** → **O(1) amortised per op**.

This is the key insight behind amortised analysis of stack-based algorithms
(e.g. maintaining a monotonic stack over n elements costs O(n) total).

---

## 2. Queue

### Circular Buffer

| Operation | Time | Notes |
|-----------|------|-------|
| enqueue | O(1) | Advance tail pointer mod capacity |
| dequeue | O(1) | Advance head pointer mod capacity |
| front | O(1) | |
| Space | O(capacity) | Fixed allocation |

**Why circular?** Naive array queue shifts elements on dequeue — O(n).
Circular buffer avoids shifting: head and tail wrap around using modulo.

```
Initial:   [_, _, _, _]   head=0, tail=0, count=0
Enqueue A: [A, _, _, _]   head=0, tail=1, count=1
Enqueue B: [A, B, _, _]   head=0, tail=2, count=2
Dequeue:   [_, B, _, _]   head=1, tail=2, count=1  ← no shifting!
Enqueue C: [_, B, C, _]   head=1, tail=3, count=2
Enqueue D: [_, B, C, D]   head=1, tail=0, count=3  ← wraps around
```

**Full vs Empty disambiguation**: use a separate `_count` field.
(Alternative: waste one slot; flag with `head == tail` = empty, `(tail+1)%cap == head` = full.)

### Linked Queue

| Operation | Time | Notes |
|-----------|------|-------|
| enqueue | O(1) | Insert at tail pointer |
| dequeue | O(1) | Remove at head pointer |
| Space | O(n) | 1 pointer per node overhead |

The critical invariant: maintain both `_head` and `_tail` pointers.
Without `_tail`, enqueue degrades to O(n).

---

## 3. Deque (Double-ended Queue)

| Operation | Time |
|-----------|------|
| push_front / push_back | O(1) |
| pop_front / pop_back | O(1) |
| peek_front / peek_back | O(1) |

Implementation uses a doubly linked list with sentinel nodes —
same technique as the DoublyLinkedList in module 01.

---

## 4. Monotonic Stack — Key Pattern

A monotonic stack maintains elements in sorted order (increasing or decreasing).
When a new element breaks the order, we pop until the invariant is restored.

**Claim**: processing n elements with a monotonic stack costs **O(n) total**.

**Proof**: each element is pushed exactly once and popped at most once.
Total operations ≤ 2n → O(n). ∎

### Applications

| Problem | Stack type | What's popped |
|---------|-----------|---------------|
| Next Greater Element | Decreasing | When current > top |
| Largest Rectangle in Histogram | Increasing | When current < top |
| Trapping Rain Water | Decreasing | When current > top |
| Daily Temperatures | Decreasing | When current > top |

---

## 5. Lower Bound

Any algorithm that implements a FIFO queue using only a LIFO stack must use
at least **two stacks** and incurs Ω(1) amortised cost per operation.

*Proof sketch*: a single stack cannot produce FIFO order without reversing,
which requires O(n) extra storage or O(n) time per dequeue.
The two-stack queue (enqueue to stack1; on dequeue, reverse into stack2 when empty)
achieves O(1) amortised — this is tight. ∎

The two-stack queue is itself an elegant amortised analysis example:
each element crosses from stack1 to stack2 exactly once → O(1) amortised dequeue.

---

## References

- CLRS §10.1 (Stacks and Queues), §17.1 (Aggregate Method)
- Sedgewick & Wayne, *Algorithms* §1.3
