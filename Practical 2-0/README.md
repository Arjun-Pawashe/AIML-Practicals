# Search Algorithm Performance Comparison (Python)

## Overview
Implementation and empirical comparison of five **graph-search algorithms** — BFS, DFS, UCS, Greedy Best-First Search, and A* — on a sample weighted/unweighted graph, plus four **N-Queens solving techniques** — Hill Climbing, Simulated Annealing, Backtracking, and Forward Checking. Each algorithm is benchmarked on nodes explored, execution time, and solution quality (path cost / conflicts), with results visualized as bar charts.

## Problem Statement
Implement and compare BFS, DFS, UCS, Greedy Best-First Search and A* for pathfinding from a start node `S` to a goal node `Z` in a sample graph, and Hill Climbing, Simulated Annealing, Backtracking and Forward Checking for solving the N-Queens constraint satisfaction problem (N = 10), evaluating each algorithm on path cost/solution quality, nodes explored, and execution time.

## Files
| File | Description |
|---|---|
| `search_algorithms.py` | Python source implementing all nine algorithms, the comparison tables, and the plotting functions |
| `README.md` | This file |
| `sample_input_output.txt` | Sample console output |
| `performance_chart.png` | Bar-chart comparison of the graph-search algorithms (nodes explored, execution time, path cost) |

## How It Works
- **Graph search:**
  - `bfs` / `dfs` — classic queue/stack-based traversal of `UNWEIGHTED_GRAPH`.
  - `ucs` — priority-queue search on `WEIGHTED_GRAPH` expanding the lowest cumulative cost first (optimal, Dijkstra-like).
  - `greedy_best_first` — priority-queue search ordered purely by heuristic `h(n)` from the `HEURISTIC` table (fast, not optimal).
  - `a_star` — priority-queue search ordered by `f(n) = g(n) + h(n)` (optimal and complete with an admissible heuristic).
- **N-Queens (N = 10):**
  - `hill_climbing` — iterative neighbour improvement with random restarts.
  - `simulated_annealing` — probabilistic local search with a cooling schedule.
  - `backtracking_nqueens` — depth-first constraint checking with backtracking on conflict.
  - `forward_checking_nqueens` — backtracking enhanced with domain pruning after each assignment.
- `run_all_and_compare()` runs every algorithm, prints two comparison tables, and calls the plotting helpers to visualize the results.

## Requirements
- Python 3
- `numpy`, `matplotlib` (install with `pip install numpy matplotlib`)
- Standard library: `heapq`, `time`, `math`, `random`, `collections.deque`

## How to Run
```bash
python search_algorithms.py
```
This prints the comparison tables to the console and opens two figures with bar-chart comparisons.

## Sample Output
See `sample_input_output.txt` for the full console output, and `performance_chart.png` for the graph-search bar-chart comparison.

```
Algorithm      Path                          Cost      Nodes    Time(s)
-----------------------------------------------------------------------
BFS            S -> A -> D -> Z              N/A           8   0.000022
UCS            S -> C -> F -> E -> Z         9             9   0.000025
A*             S -> C -> F -> E -> Z         9             5   0.000008
```

## Key Observations
- **A\*** finds the same optimal-cost path as **UCS** while exploring roughly half as many nodes, thanks to heuristic guidance.
- **Greedy Best-First Search** explores the fewest nodes but returns a higher-cost (sub-optimal) path.
- **Forward Checking** solves N-Queens with far fewer node visits (68) than plain **Backtracking** (975) by pruning inconsistent domain values early.
- **Simulated Annealing** avoids getting permanently stuck in local optima (unlike plain Hill Climbing) but needs many more iterations to converge.

## Author
[Your Name]
