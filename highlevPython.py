#1. DFS 재귀함수
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
visited = set()
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    print(node, end=" ")
    for nxt in graph[node]:
        dfs(nxt)
dfs(1)  