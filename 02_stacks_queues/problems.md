# Stack & Queue — Problem Set

Difficulty: 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## Stack

| # | Title | Difficulty | Key Technique |
|---|-------|-----------|---------------|
| 20 | Valid Parentheses | 🟢 | Matching brackets |
| 155 | Min Stack | 🟢 | Auxiliary min-stack |
| 150 | Evaluate Reverse Polish Notation | 🟡 | Operand/operator stack |
| 739 | Daily Temperatures | 🟡 | Monotonic stack |
| 84 | Largest Rectangle in Histogram | 🔴 | Monotonic stack |
| 85 | Maximal Rectangle | 🔴 | Histogram per row |
| 394 | Decode String | 🟡 | Two stacks (count + string) |
| 856 | Score of Parentheses | 🟡 | Stack simulation |

### Study note — #20 Valid Parentheses

```python
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack
```

**Pattern**: push open brackets, pop and match on close brackets.
Time O(n), Space O(n).

### Study note — #739 Daily Temperatures (Monotonic Stack)

```python
def dailyTemperatures(temps: list[int]) -> list[int]:
    n = len(temps)
    result = [0] * n
    stack = []   # stores indices, maintains decreasing temperatures

    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result
```

**Why O(n)?** Each index is pushed and popped at most once → total ops ≤ 2n.

---

## Queue

| # | Title | Difficulty | Key Technique |
|---|-------|-----------|---------------|
| 232 | Implement Queue using Stacks | 🟢 | Two-stack queue |
| 225 | Implement Stack using Queues | 🟢 | Queue rotation |
| 239 | Sliding Window Maximum | 🔴 | Monotonic deque |
| 346 | Moving Average from Data Stream | 🟢 | Circular buffer |
| 362 | Design Hit Counter | 🟡 | Queue + time window |
| 933 | Number of Recent Calls | 🟢 | Queue trim by threshold |

### Study note — #232 Implement Queue using Stacks

Two-stack approach: `s1` for enqueue, `s2` for dequeue.

```python
class MyQueue:
    def __init__(self):
        self.s1 = []   # enqueue here
        self.s2 = []   # dequeue here

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self._move()
        return self.s2.pop()

    def peek(self):
        self._move()
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2

    def _move(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
```

**Amortised analysis**: each element moves from s1 → s2 exactly once.
Total cost over n ops = O(n) → **O(1) amortised per operation**.

### Study note — #239 Sliding Window Maximum (Monotonic Deque)

```python
from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    dq = deque()   # stores indices; front = max of current window
    result = []

    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Maintain decreasing deque
        while dq and nums[i] > nums[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

**Complexity**: O(n) time — each index enters and leaves deque at most once.
**Space**: O(k) for the deque.

This is a canonical example of monotonic deque for range-max queries
on a sliding window — a building block for many time-series problems.

---

## Challenge problems

1. **Stack-sortable permutations**: given a sequence, determine if it can be sorted
   using a single stack (push/pop only). What is the forbidden pattern?
   *(Answer: 231-pattern — if i < j < k and a[k] < a[i] < a[j])*

2. **Implement a queue with O(1) worst-case** enqueue and dequeue
   using a more sophisticated data structure (hint: look up "real-time queue" in
   Okasaki's *Purely Functional Data Structures*).

3. **Maximum of all subarrays of size k** using only O(1) extra space.
   Is this possible? Why or why not?
