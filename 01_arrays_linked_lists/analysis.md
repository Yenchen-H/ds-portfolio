# Array & Linked List — Complexity Analysis

## 1. Static Array

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access `A[i]` | Θ(1) | — | Base address + offset |
| Search (unsorted) | Θ(n) | — | Linear scan |
| Search (sorted) | Θ(log n) | — | Binary search |
| Insert at end | Θ(1) | — | Fixed capacity assumed |
| Insert at index `i` | Θ(n − i) | — | Must shift right |
| Delete at index `i` | Θ(n − i) | — | Must shift left |

**Spatial locality**: contiguous memory makes arrays cache-friendly.
A sequential scan of n elements causes at most ⌈n / B⌉ cache misses,
where B is the cache-line size in elements.

---

## 2. Dynamic Array (Amortised Analysis)

### Doubling strategy

When the array is full, allocate a new array of size 2·capacity and copy all elements.

**Aggregate method**:

Let the final size be n. Copying occurs at sizes 1, 2, 4, …, 2^⌊log n⌋.
Total copy cost:

```
1 + 2 + 4 + … + n ≤ 2n = O(n)
```

Spread over n appends → **O(1) amortised per append**.

**Potential method**:

Define Φ = 2·size − capacity.

- Before first insert: Φ = 2·0 − 1 = −1 ≈ 0 (non-negative is sufficient after normalisation; we track the change ΔΦ).
- Normal append (no resize): actual cost = 1, ΔΦ = 2. Amortised = 1 + 2 = 3 = O(1).
- Resize append (size = capacity = k): actual cost = k + 1, new capacity = 2k.  
  ΔΦ = (2(k+1) − 2k) − (2k − k) = 2 − k. Amortised = (k+1) + (2−k) = 3 = O(1).

Either method confirms **O(1) amortised append**.

### Shrinking strategy

Shrink at load factor ≤ 1/4 (not 1/2) to avoid thrashing on alternating insert/delete.

---

## 3. Singly Linked List

| Operation | Time | Notes |
|-----------|------|-------|
| Prepend | Θ(1) | Update head pointer |
| Append | Θ(n) | Must walk to tail |
| Access index `i` | Θ(i) | No random access |
| Delete (given node) | Θ(n) | Need predecessor |
| Delete head | Θ(1) | |
| Reverse | Θ(n) | Three-pointer walk |
| Cycle detection | Θ(n) time, Θ(1) space | Floyd's algorithm |

### Floyd's cycle detection (proof sketch)

Let slow move 1 step, fast move 2 steps. If a cycle of length λ exists
starting at position μ from the head:

1. When slow enters the cycle (after μ steps), fast is already inside at position μ mod λ.
2. The gap closes at 1 step per iteration → they meet within λ more steps.
3. Total: O(μ + λ) = O(n). ∎

---

## 4. Doubly Linked List

| Operation | Time | Notes |
|-----------|------|-------|
| Insert after node `p` | Θ(1) | 4 pointer updates |
| Delete node `p` | Θ(1) | Given a direct reference |
| Append / prepend | Θ(1) | Using sentinel nodes |
| Search | Θ(n) | |

**Sentinel nodes** (dummy head + dummy tail) eliminate all boundary checks —
no special cases for empty list, insert at front, or insert at back.

---

## 5. Array vs Linked List — Trade-off Summary

| Criterion | Array | Linked List |
|-----------|-------|-------------|
| Random access | O(1) | O(n) |
| Insert at known position | O(n) | O(1) with pointer |
| Memory overhead | Low (no pointers) | High (1–2 pointers/node) |
| Cache performance | Excellent | Poor (pointer chasing) |
| Resizing | O(n) copy | O(1) per node |
| Suitable for | Random access, sorting | Frequent splice/delete |

> **Key insight for research**: in modern CPUs, cache effects often make arrays
> faster than linked lists even for operations where the pointer-based analysis
> predicts equal or better performance. Always benchmark, never assume.

---

## 6. Lower Bound

Any comparison-based search on an unsorted sequence of n elements requires
Ω(n) comparisons in the worst case — follows from the information-theoretic
argument that n possible positions produce a decision tree of height ≥ log₂ n...
wait, that's for sorting. For search: any algorithm must inspect at least 1 element
per unexamined candidate. Without structure, Ω(n) is tight.

---

## References

- CLRS §10 (Elementary Data Structures), §17 (Amortised Analysis)
- Sedgewick & Wayne, *Algorithms* §1.3 (Bags, Queues, Stacks)
