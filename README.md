# Data Structures — Study Portfolio

> A systematic study of data structures from fundamentals to research-level topics,
> implemented in Python with rigorous complexity analysis and curated problem sets.
>
> Built as part of doctoral program preparation in Computer Science / Information Systems.

---

## Overview

This repository documents a structured progression through classical and advanced data structures.
Each module contains a from-scratch Python implementation, a formal complexity analysis note,
and a set of LeetCode problems that exercise the structure in practice.

The goal is not to collect solutions, but to build the analytical vocabulary needed
to read, evaluate, and extend research in algorithms and systems.

---

## Structure

| Layer | Topic | Status |
|-------|-------|--------|
| L1 | [Array & Linked List](./01_arrays_linked_lists/) | ✅ |
| L1 | [Stack & Queue](./02_stacks_queues/) | ✅ |
| L1 | [Hash Table](./03_hash_tables/) | ✅ |
| L1 | [Heap / Priority Queue](./04_heaps/) | ✅ |
| L2 | [BST / AVL / Red-Black Tree](./05_trees/) | 🔄 |
| L2 | [Graph & Traversals](./06_graphs/) | 🔄 |
| L2 | [Trie](./07_tries/) | 🔄 |
| L3 | [Advanced Structures](./08_advanced/) | 📋 |
| L4 | [Research-Level Topics](./09_research/) | 📋 |

✅ Complete · 🔄 In progress · 📋 Planned

---

## Module Format

Every topic folder follows this structure:

```
01_arrays_linked_lists/
├── implementation.py   # From-scratch Python implementation
├── analysis.md         # Complexity analysis with proofs
└── problems.md         # LeetCode problems & solution notes
```

---

## Complexity Reference

All analysis uses the following notation:

- **O / Ω / Θ** — asymptotic upper, lower, and tight bounds
- **Amortized** — average cost over a sequence of operations (aggregate / accounting / potential method)
- **Expected** — average over random choices (for randomised structures)

---

## References

- Cormen, Leiserson, Rivest, Stein — *Introduction to Algorithms* (CLRS), 4th ed.
- Sedgewick & Wayne — *Algorithms*, 4th ed.
- Okasaki — *Purely Functional Data Structures*
- Original papers linked per topic where applicable

---

*Author: Yanzhen · NKUST Supply Chain Management Dept.*
*Last updated: 2026*
