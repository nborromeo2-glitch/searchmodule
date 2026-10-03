
import heapq
from collections import deque

# Undirected weighted graph: node -> {neighbor: edge_cost}
GRAPH = {
    "S": {"A": 4, "B": 3, "C": 2},
    "A": {"S": 4, "D": 5},
    "D": {"A": 5, "G": 4},
    "B": {"S": 3, "G": 1},
    "C": {"S": 2, "G": 8},
    "G": {"D": 4, "B": 1, "C": 8},
}

# Heuristic h(n): estimated cost from n to goal G (admissible and consistent)
H = {"S": 4, "A": 8, "D": 4, "B": 1, "C": 6, "G": 0}


def path_cost(graph, path):
    return sum(graph[a][b] for a, b in zip(path, path[1:]))


def bfs(graph, start, goal):
    """Breadth-first search: fewest edges, ignores weights."""
    frontier = deque([[start]])
    visited = {start}
    order = []
    while frontier:
        path = frontier.popleft()
        node = path[-1]
        order.append(node)
        if node == goal:
            return path, order
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                frontier.append(path + [nxt])
    return None, order


def dfs(graph, start, goal):
    """Depth-first search: goes deep first, not guaranteed shortest."""
    stack = [[start]]
    visited = set()
    order = []
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        if node == goal:
            return path, order
        # reversed so neighbors are explored in dictionary order
        for nxt in reversed(list(graph[node])):
            if nxt not in visited:
                stack.append(path + [nxt])
    return None, order


def astar(graph, h, start, goal, verbose=True):
    """A* search: expands the node with the lowest f(n) = g(n) + h(n)."""
    open_heap = [(h[start], 0, start, [start])]  # (f, g, node, path)
    best_g = {start: 0}
    closed = set()
    order = []
    if verbose:
        print(f"{'expand':<8}{'g':>4}{'h':>4}{'f':>4}   path")
    while open_heap:
        f, g, node, path = heapq.heappop(open_heap)
        if node in closed:
            continue
        closed.add(node)
        order.append(node)
        if verbose:
            print(f"{node:<8}{g:>4}{h[node]:>4}{f:>4}   {' -> '.join(path)}")
        if node == goal:
            return path, g, order
        for nxt, cost in graph[node].items():
            new_g = g + cost
            if nxt not in closed and new_g < best_g.get(nxt, float("inf")):
                best_g[nxt] = new_g
                heapq.heappush(
                    open_heap, (new_g + h[nxt], new_g, nxt, path + [nxt])
                )
    return None, float("inf"), order


def main():
    start, goal = "S", "G"

    path, order = bfs(GRAPH, start, goal)
    print("BFS")
    print("  visit order:", " ".join(order))
    print("  path:", " -> ".join(path), "| cost:", path_cost(GRAPH, path))

    path, order = dfs(GRAPH, start, goal)
    print("\nDFS")
    print("  visit order:", " ".join(order))
    print("  path:", " -> ".join(path), "| cost:", path_cost(GRAPH, path))

    print("\nA* search")
    path, cost, order = astar(GRAPH, H, start, goal)
    print("  path:", " -> ".join(path), "| cost:", cost)


if __name__ == "__main__":
    main()
