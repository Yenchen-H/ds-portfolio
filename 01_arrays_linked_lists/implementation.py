"""
Hash Table — From-Scratch Implementation
=========================================
Implements:
  - SeparateChainingHashMap  : chaining with linked lists
  - OpenAddressingHashMap    : linear probing with lazy deletion

All keys must be hashable. Load factor threshold: 0.75 (resize up),
0.25 (resize down, minimum capacity 8).
"""

from __future__ import annotations
from typing import Any, Iterator, Optional


_DELETED = object()   # sentinel for lazy deletion


# ──────────────────────────────────────────────
# Separate Chaining
# ──────────────────────────────────────────────

class SeparateChainingHashMap:
    """
    Expected O(1) get / put / delete under uniform hashing assumption.
    Worst-case O(n) if all keys collide (adversarial input or poor hash).

    Load factor α = n / m  (n items, m buckets).
    Expected chain length = α.  Resize keeps α ∈ (0.25, 0.75].
    """

    def __init__(self, initial_capacity: int = 8) -> None:
        self._capacity = initial_capacity
        self._size = 0
        self._buckets: list[list] = [[] for _ in range(self._capacity)]

    def _hash(self, key: Any) -> int:
        return hash(key) % self._capacity

    def put(self, key: Any, value: Any) -> None:
        idx = self._hash(key)
        for pair in self._buckets[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self._buckets[idx].append([key, value])
        self._size += 1
        if self._size / self._capacity > 0.75:
            self._resize(self._capacity * 2)

    def get(self, key: Any, default: Any = None) -> Any:
        idx = self._hash(key)
        for pair in self._buckets[idx]:
            if pair[0] == key:
                return pair[1]
        return default

    def delete(self, key: Any) -> bool:
        idx = self._hash(key)
        for i, pair in enumerate(self._buckets[idx]):
            if pair[0] == key:
                self._buckets[idx].pop(i)
                self._size -= 1
                if self._capacity > 8 and self._size / self._capacity < 0.25:
                    self._resize(self._capacity // 2)
                return True
        return False

    def _resize(self, new_capacity: int) -> None:
        old_buckets = self._buckets
        self._capacity = new_capacity
        self._size = 0
        self._buckets = [[] for _ in range(new_capacity)]
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key: Any) -> bool:
        return self.get(key) is not None


# ──────────────────────────────────────────────
# Open Addressing (Linear Probing)
# ──────────────────────────────────────────────

class OpenAddressingHashMap:
    """
    Linear probing with lazy deletion.

    Primary clustering is a known weakness of linear probing.
    Quadratic probing or double hashing reduce cluster formation.
    Expected O(1) operations at load factor < 0.5.
    """

    def __init__(self, initial_capacity: int = 8) -> None:
        self._capacity = initial_capacity
        self._size = 0
        self._keys: list = [None] * self._capacity
        self._vals: list = [None] * self._capacity

    def _hash(self, key: Any) -> int:
        return hash(key) % self._capacity

    def put(self, key: Any, value: Any) -> None:
        if self._size / self._capacity >= 0.5:
            self._resize(self._capacity * 2)
        idx = self._hash(key)
        while self._keys[idx] not in (None, _DELETED):
            if self._keys[idx] == key:
                self._vals[idx] = value
                return
            idx = (idx + 1) % self._capacity
        self._keys[idx] = key
        self._vals[idx] = value
        self._size += 1

    def get(self, key: Any, default: Any = None) -> Any:
        idx = self._hash(key)
        while self._keys[idx] is not None:
            if self._keys[idx] == key:
                return self._vals[idx]
            idx = (idx + 1) % self._capacity
        return default

    def delete(self, key: Any) -> bool:
        idx = self._hash(key)
        while self._keys[idx] is not None:
            if self._keys[idx] == key:
                self._keys[idx] = _DELETED
                self._vals[idx] = None
                self._size -= 1
                return True
            idx = (idx + 1) % self._capacity
        return False

    def _resize(self, new_capacity: int) -> None:
        old_keys, old_vals = self._keys, self._vals
        self._capacity = new_capacity
        self._size = 0
        self._keys = [None] * new_capacity
        self._vals = [None] * new_capacity
        for k, v in zip(old_keys, old_vals):
            if k is not None and k is not _DELETED:
                self.put(k, v)

    def __len__(self) -> int:
        return self._size


# ──────────────────────────────────────────────
# Smoke test
# ──────────────────────────────────────────────

if __name__ == "__main__":
    for MapClass in (SeparateChainingHashMap, OpenAddressingHashMap):
        print(f"\n── {MapClass.__name__} ──")
        m = MapClass()
        for i in range(20):
            m.put(f"key{i}", i * 10)
        print("get key5:", m.get("key5"))
        print("get key19:", m.get("key19"))
        m.delete("key5")
        print("after delete key5:", m.get("key5", "NOT FOUND"))
        print("size:", len(m))
