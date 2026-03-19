# Hash Table — Complexity Analysis

## 1. 核心概念

Hash Table 用一個 hash function 把 key 轉成陣列索引，
達到平均 O(1) 的 get / put / delete。

```
key → hash(key) % capacity → bucket index → value
```

---

## 2. 操作複雜度

| 操作 | 平均 | 最壞 | 說明 |
|------|------|------|------|
| put | O(1) | O(n) | 最壞：所有 key 碰撞到同一格 |
| get | O(1) | O(n) | 同上 |
| delete | O(1) | O(n) | 同上 |
| resize | O(n) | O(n) | 搬移所有元素 |
| Space | O(n) | O(n) | |

最壞情況在實務中極少發生，好的 hash function 讓碰撞趨近均勻分布。

---

## 3. 碰撞處理 — 兩種策略

### Separate Chaining（鏈結串列）

每個 bucket 是一條 linked list，碰撞的 key 接在後面。

```
bucket[3] → [("apple", 5)] → [("grape", 2)] → None
```

- 負載因子 α = n / m（n 個元素，m 個 bucket）
- 平均鏈長 = α
- 建議 α ≤ 0.75 → 超過就 resize

### Open Addressing（線性探測）

碰撞時往下一格找空位，不用額外指標。

```
put("apple"):  hash = 3，bucket[3] 空 → 放入
put("grape"):  hash = 3，bucket[3] 滿 → 試 bucket[4] → 放入
```

- 建議 α ≤ 0.5（比 chaining 更嚴格，避免 clustering）
- 刪除需用「懶刪除」標記，不能直接清空（會斷掉探測鏈）

---

## 4. Resize 的攤銷分析

Resize 發生在 α 超過閾值，將容量加倍並搬移所有元素。

用 aggregate method：
- 每個元素從加入到下次 resize，至少又加入了 n/2 個新元素
- 所以每個元素平均只被搬移 O(1) 次
- **put 的攤銷複雜度 = O(1)**

---

## 5. 好的 Hash Function 條件

1. **均勻分布** — key 盡量散佈到所有 bucket
2. **快速計算** — O(1) 時間
3. **確定性** — 相同 key 永遠得到相同 hash

Python 內建 `hash()` 已滿足以上條件，
但注意：`hash()` 的結果在不同執行之間可能不同（加了隨機鹽）。

---

## 6. Array vs Linked List vs Hash Table

| 操作 | Array | Linked List | Hash Table |
|------|-------|-------------|------------|
| 搜尋 | O(n) | O(n) | O(1) 平均 |
| 插入 | O(n) | O(1) | O(1) 平均 |
| 刪除 | O(n) | O(1) | O(1) 平均 |
| 有序 | 可 | 可 | ❌ |
| 記憶體 | 低 | 中 | 高（需預留空間）|

---

## References

- CLRS §11（Hash Tables）
- Sedgewick & Wayne, *Algorithms* §3.4
