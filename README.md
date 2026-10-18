# Algorithm Showdown

A final project for **Algorithms and Complexity** comparing brute-force algorithms with greedy and heuristic approaches across three problems.

Each problem uses the same sample data to compare the **results, running times, and efficiency** of both approaches.

## Problems

1. **Exam Scheduling** — Graph coloring
2. **Delivery Route** — Traveling Salesperson Problem (TSP)
3. **Budget Allocation** — Knapsack problem

## Project Structure

```text
main.py
sample_data.json
problem1_exam_scheduling.py
problem2_delivery_route.py
problem4_budget_allocation.py
README.md
```

## Requirements

- Python 3.8+
- No external libraries required

The project uses Python's built-in `json`, `itertools`, `math`, and `time` modules.

## How to Run

Run all three problems:

```bash
python main.py
```

Run an individual problem:

```bash
python problem1_exam_scheduling.py
python problem2_delivery_route.py
python problem4_budget_allocation.py
```

Make sure `sample_data.json` is in the same directory as the Python files.

## Algorithm Comparison

### 1. Exam Scheduling

**Goal:** Assign exams to time slots without scheduling conflicting exams at the same time, using as few slots as possible.

| Approach | Method | Result |
|---|---|---|
| Brute Force | Tests possible assignments to find the minimum number of slots | 2 slots |
| Greedy | Assigns each exam to the first available valid slot | 3 slots |

**Takeaway:** Brute force finds the optimal solution, while greedy is faster but may use more time slots depending on the exam order.

### 2. Delivery Route

**Goal:** Find the shortest round trip from the school, visiting all seven destinations exactly once before returning.

| Approach | Method | Total Distance |
|---|---|---:|
| Brute Force | Tests every possible stop order | 28.92 |
| Nearest Neighbor | Visits the closest unvisited destination | 33.60 |

**Takeaway:** Brute force finds the shortest route but becomes expensive as the number of destinations increases. Nearest neighbor is faster but does not guarantee the shortest route.

### 3. Budget Allocation

**Goal:** Select equipment requests with the highest total score without exceeding a budget of 90.

| Approach | Method | Total Score |
|---|---|---:|
| Brute Force | Tests every possible combination of items | 360 |
| Greedy | Prioritizes items by score-to-cost ratio | 359 |

**Takeaway:** Greedy quickly selects items with better value per cost, but brute force can find a better combination.

## Key Takeaways

| Problem | Brute Force | Greedy / Heuristic |
|---|---|---|
| Exam Scheduling | Optimal: 2 slots | Faster: 3 slots |
| Delivery Route | Shortest: 28.92 | Faster: 33.60 |
| Budget Allocation | Best score: 360 | Faster: 359 |

Brute-force algorithms can guarantee the optimal answer for these problems when they exhaustively evaluate all valid possibilities. However, their computational cost grows rapidly as the input size increases.

Greedy and heuristic algorithms reduce computation time by making locally efficient choices, but they do not always produce the optimal result.

**The main lesson:** Better performance does not always mean a better answer. Choosing an algorithm involves balancing execution time, solution quality, and problem size.

## Sources

- Frontend Masters 
- Course lecture notes for Algorithms and Complexity
- [Python Documentation — `itertools`](https://docs.python.org/3/library/itertools.html)
- [Python Documentation — `time`](https://docs.python.org/3/library/time.html)

---

*Academic project for Algorithms and Complexity.*