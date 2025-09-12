#1. DFS 재귀함수
# graph = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1],
#     4: [2]
# }
# visited = set()
# def dfs(node):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node, end=" ")
#     for nxt in graph[node]:
#         dfs(nxt)
# dfs(4)  # 4 2 1 3

#2-1. BFS
from collections import deque

def bfs(start):
    queue = deque([start])   # 큐 초기화
    visited = set([start])   # 방문 기록 (중복 방지)

    print(f"시작 노드: {start}")

    while queue:
        node = queue.popleft()   # 큐에서 꺼내기
        print(node, end=" ")

        for nxt in graph[node]:  # 인접 노드 확인
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}
bfs(1)

