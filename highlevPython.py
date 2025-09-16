#1-1. DFS 재귀함수(1)
# graph = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1],
#     4: [2]
# }
# visited = set() #순서가 없는 집합
# def dfs(node):
#     if node in visited:
#         return
#     visited.add(node)
#     print(node, end=" ")
#     for nxt in graph[node]:
#         dfs(nxt)
# dfs(4)  

#1-2. DFS 재귀함수(2) / 그래프가 몇 개의 연결요소로 나뉘어져 있는가?
# graph = {
#     1: [2],
#     2: [1, 3],
#     3: [2],
#     4: [5],
#     5: [4],
#     6: []
# }
# visted = set()
# def dfs(node):
#     if node in visted:
#         return
#     visted.add(node)
#     for nxt in graph[node]:
#         dfs(nxt)
# line = 0
# for node in graph:
#     if node not in visted:
#         dfs(node)
#         line += 1
# print(f"연결 요소 개수: {line}")

#1-3. DFS 재귀함수(3) / 미로 경로 찾기 (0은 이동 가능, 1은 벽 / 길이 있는가?)
# maze = [
#     [0, 1, 0, 0],
#     [0, 0, 0, 1],
#     [1, 1, 0, 0],
#     [0, 0, 0, 0]
# ]
# N, M = len(maze), len(maze[0])
# visited = [[False]*M for _ in range(N)] #리스트 컴프리헨션
# dx = [1, -1, 0, 0] #좌표이동식
# dy = [0, 0, 1, -1] #i=0이면 우로 한칸 / 1이면 좌로 한칸 / 2면 아래로 한칸 / 3이면 위로 한칸
# def dfs(x, y):
#     if x == N-1 and y == M-1: 
#         return True
#     visited[x][y] = True
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M:
#             if maze[nx][ny] == 0 and not visited[nx][ny]:
#                 if dfs(nx, ny):
#                     return True
#     return False
# if dfs(0, 0):
#     print("출구에 도착할 수 있습니다!")
# else:
#     print("출구에 도착할 수 없습니다.")
"""
>> 좌표이동을 사용하여 푼다.
>> list comprehension은 파이썬에서 자주쓰는 문법
    >> 기존 리스트를 활용해 같은 크기의 새 리스트를 만듦 (0으로 채우거나 false로 채우는 등)
"""

#1-4. DFS 반복함수(1)
# graph = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1],
#     4: [2]
# }
# def dfs(start):
#     stack = [start] #스택(리스트형태)에 start노드를 넣음
#     visted = set()
#     while stack: #스택에 값이 없을때까지 = 다 pop될 때까지
#         node = stack.pop()
#         if node not in visted:
#             visted.add(node)
#             print(node, end = " ")
#             for nxt in reversed(graph[node]): #stack이자 pop으로 뽑아내기에 뒤부터 나오도록
#                 stack.append(nxt)
# dfs(1) 

#1-5. DFS 반복함수(2)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': [],
#     'F': []
# }
# def dfs(start):
#     stack = [start]
#     visited = set()
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             print(node, end = " ")
#             for nxt in reversed(graph[node]):
#                 stack.append(nxt)
# dfs('A')

#1-6. DFS 반복함수(3) / 2차원 그리드 (1은 땅, 0은 바다일 때 섬의 갯수는?)
grid = [
    [1,1,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,0,0]
]
N, M = len(grid), len(grid[0])
visited = [[False]*M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y):
    stack = [(x,y)]
    while stack:
        cx, cy = stack.pop()
        if not visited[cx][cy]: #이 좌표가 FALSE였으면 TRUE로 만들겠다
            visited[cx][cy] = True
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] == 1 and not visited[nx][ny]:
                        stack.append((nx, ny))

# 전체 그리드 돌면서 섬 개수 세기
count = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            count += 1

print(f"섬 개수: {count}")