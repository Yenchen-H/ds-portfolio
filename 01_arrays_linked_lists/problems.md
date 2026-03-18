# Array & Linked List — Problem Set

Problems are grouped by the core technique exercised.
Difficulty: 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## Array

| # | Title | Difficulty | Key Technique |
|---|-------|-----------|---------------|
| 1 | Two Sum | 🟢 | Hash map complement |
| 15 | 3Sum | 🟡 | Sort + two pointers |
| 11 | Container With Most Water | 🟡 | Two pointers, greedy |
| 42 | Trapping Rain Water | 🔴 | Prefix max arrays / two pointers |
| 53 | Maximum Subarray | 🟡 | Kadane's algorithm (DP on array) |
| 56 | Merge Intervals | 🟡 | Sort + linear scan |
| 84 | Largest Rectangle in Histogram | 🔴 | Monotonic stack |
| 238 | Product of Array Except Self | 🟡 | Prefix / suffix products, O(1) extra |

### Study note — #42 Trapping Rain Water

Two-pointer solution achieves O(n) time, O(1) space.

```python
def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```

**Why it works**: at each step, the water at position `left` is determined
by `left_max` when `height[left] < height[right]`, because the right wall
is guaranteed to be at least `height[right] ≥ left_max`.

---

## Linked List

| # | Title | Difficulty | Key Technique |
|---|-------|-----------|---------------|
| 206 | Reverse Linked List | 🟢 | Three-pointer iteration |
| 21 | Merge Two Sorted Lists | 🟢 | Merge with dummy head |
| 141 | Linked List Cycle | 🟢 | Floyd's algorithm |
| 142 | Linked List Cycle II | 🟡 | Floyd's — find cycle entry |
| 19 | Remove Nth Node From End | 🟡 | Two pointers, n-gap |
| 23 | Merge k Sorted Lists | 🔴 | Min-heap or divide & conquer |
| 25 | Reverse Nodes in k-Group | 🔴 | Iterative group reversal |
| 146 | LRU Cache | 🟡 | DoublyLinkedList + HashMap |

### Study note — #146 LRU Cache

Classic combination of DoublyLinkedList + dict. O(1) for both get and put.

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: dict = {}          # key -> node
        # Sentinel nodes
        self.head = _DLLNode(0, 0)    # MRU side
        self.tail = _DLLNode(0, 0)    # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = _DLLNode(key, value)
        self.cache[key] = node
        self._insert_front(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

**Complexity**: O(1) get and put. Space: O(capacity).

---

## Challenge problems (beyond LeetCode)

These require combining multiple ideas and are closer to interview / research exercises:

1. **Implement a memory allocator** using a free-list (linked list of free blocks).  
   Analyse internal vs. external fragmentation.

2. **Persistent array**: support `set(i, v, version)` and `get(i, version)` in O(log n)
   time using a persistent segment tree (preview of L4 topic).

3. **Skip list with finger search**: prove that searching from the last accessed
   position takes O(log d) expected time where d is the distance to the target.
