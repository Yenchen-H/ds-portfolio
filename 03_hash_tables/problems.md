# Hash Table — Problem Set

Difficulty: 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 題目清單

| # | Title | Difficulty | 核心技巧 |
|---|-------|-----------|----------|
| 1 | Two Sum | 🟢 | 用 hash map 存已看過的數 |
| 217 | Contains Duplicate | 🟢 | 用 set 偵測重複 |
| 242 | Valid Anagram | 🟢 | 字母頻率計數 |
| 49 | Group Anagrams | 🟡 | 排序後的字串當 key |
| 128 | Longest Consecutive Sequence | 🟡 | set 快速查找 |
| 146 | LRU Cache | 🟡 | Hash map + Doubly Linked List |
| 380 | Insert Delete GetRandom O(1) | 🟡 | Hash map + Array |
| 41 | First Missing Positive | 🔴 | Array 當 hash table |

---

## 解題筆記

### #1 Two Sum 🟢

**題意**：給一個陣列和目標值，找出兩個數相加等於目標，回傳索引。

**思路**：
- 暴力法：兩層迴圈，O(n²)
- Hash map：邊走邊記「需要什麼數才能湊到 target」，O(n)

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}   # 存 {數值: 索引}

    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

    return []
```

**為何 O(1) 查找**：`need in seen` 是 hash map 的查找，平均 O(1)。
整體時間複雜度 O(n)，空間 O(n)。

---

### #242 Valid Anagram 🟢

**題意**：判斷兩個字串是否為 anagram（字母相同但順序不同）。

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        count[ch] = count.get(ch, 0) - 1

    return all(v == 0 for v in count.values())
```

---

### #49 Group Anagrams 🟡

**題意**：把 anagram 分在同一組。

**關鍵想法**：排序後相同的字串 → 同一組的 key。

```python
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    groups = {}

    for s in strs:
        key = tuple(sorted(s))   # "eat" → ('a','e','t')
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return list(groups.values())
```

---

### #146 LRU Cache 🟡

**題意**：實作 LRU Cache，get 和 put 都要 O(1)。

**思路**：Hash map（快速查找）+ Doubly Linked List（快速移動到最近使用）

這題是 Hash Table 和 Linked List 的經典組合，
詳細實作見 `01_arrays_linked_lists/problems.md`。

---

## 自我挑戰

做完上面題目後，試著回答：

1. 為什麼 LRU Cache 需要 Doubly Linked List 而不是 Singly Linked List？
2. `#380 Insert Delete GetRandom O(1)` 為什麼需要同時用 hash map 和 array？
3. Hash Table 在什麼情況下會退化成 O(n)？如何避免？
