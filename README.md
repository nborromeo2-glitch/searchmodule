# Search Module: BFS, DFS, A*

Python implementations of three search algorithms on a small weighted graph.

## Run

```bash
python3 search.py
```

No dependencies (standard library only).

## Graph

```
        4        5        4
   S ------- A ------- D ------- G
   | \                           /|
   |  \ 3          1            / |
   |   B ----------------------'  |
   | 2                            | 8
   C ----------------------------'
```

Edit `GRAPH` and `H` in `search.py` to change the graph or heuristic.

## Results (start S, goal G)

| Algorithm | Path | Cost | Notes |
|-----------|------|------|-------|
| BFS | S -> B -> G | 4 | Fewest edges; ignores weights |
| DFS | S -> A -> D -> G | 13 | Goes deep first; not optimal |
| A* | S -> B -> G | 4 | Optimal; uses f(n) = g(n) + h(n) |

## A* notes

- g(n): cost from start to n
- h(n): heuristic estimate from n to goal (admissible and consistent here)
- f(n) = g(n) + h(n): A* always expands the lowest f next
