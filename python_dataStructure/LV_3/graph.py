#1 그래프 기본 구조
    #인접 리스트
    #인접 행렬
    #방향 / 무방향
    #가중치 그래프
#2 그래프 탐색
    #DFS, BFS
#3 기본 알고리즘
    #3-1 위상 정렬(Topological Sort) / DFS, BFS로 
#4 최소 신장 트리
    #4-1 Kruskal (Union-Find)
    #4-2 Prim
#5 최단경로 알고리즘
    #5-1 Dijkstra
    #5-2 Bellman-Ford
    #5-3 Floyd-Warshall

# #1 그래프 기본 구조 ------------------------------------------------------------
#     # 정점과 간선으로 구성
#     # 방향&무방향 / 가중치로 나뉘어짐
#     # -> 여기서 한 건 그저 코드로 표현한 것. 알고리즘으로 만들어야 함
#     #     -> 다익스트라 , 벨만포드, 플로이드 등

# # 무방향 그래프 (비가중치)
# graph = {
#     1: [2, 3],
#     2: [1, 4],
#     3: [1],
#     4: [2]
# }
# from collections import defaultdict #딕셔너리 만드는 함수

# graph = defaultdict(list)

# def add_edge(u, v):
#     graph[u].append(v)
#     graph[v].append(u) #무방향이라 둘다 연결

# add_edge(1,2)
# add_edge(1,3)
# add_edge(2,4)

# print(dict(graph))

# # 무방향 그래프 (가중치)
# from collections import defaultdict
# graph1 = {
#     1: [(2, 5), (3, 2)],   # 1→2(5), 1→3(2)
#     2: [(1, 5)],
#     3: [(1, 2)]
# }

# graph1 = defaultdict(list)

# def add_edge1(u, v, w): #가중치까지 받아준다
#     graph1[u].append((v,w))
#     graph1[v].append((u,w)) #한쪽만 연결하면 방향그래프

# add_edge1(1,2,5)
# add_edge1(1,3,2)

# print(dict(graph1))

# #2 그래프 탐색 ------------------------------------------------------------
#     # 정점들을 어떤 규칙으로 방문하는 과정(DFS, BFS)
# from collections import defaultdict, deque

# graph = defaultdict(list)

# def add_edge(u,v):
#     graph[u].append((v))
#     graph[v].append((u))

# add_edge(1,2)
# add_edge(1,3)
# add_edge(2,4)
# add_edge(3,5)

# print(dict(graph))

# def dfs(start, graph, visited=None):
#     if visited is None:
#         visited = set()
    
#     visited.add(start)
#     print(start, end='->')

#     for nxt in graph[start]: #첫노드와 연결된걸 쭉 탐색
#         if nxt not in visited:
#             dfs(nxt, graph, visited)

# dfs(1, graph)

# def bfs(start, graph):
#     visited = set([start])
#     q = deque([start])

#     while q:
#         node = q.popleft()
#         print(node, end='->')

#         for nxt in graph[node]:
#             if nxt not in visited:
#                 visited.add(nxt)
#                 q.append(nxt)
# print()
# bfs(1, graph)
# #3 위상정렬 ------------------------------------------------------------
#     # 방향 그래프에서 노드를 순서대로 나열하는 법
#         # 선행해야 할 작업이 앞에 오도록 정렬하는 것
#     # 진입차수(in-degree) : 노드로 들어오는 간선의 개수
#         # 진입차수가 0인 노드가 시작
#             # 그 노드의 간선으로 이어지는 노드로 이동, 
#             # 해당 노드들의 진입차수를 1씩 감소

# from collections import deque, defaultdict

# def topological_sort(graph):
#     # 진입차수 계산
#     in_degree = defaultdict(int)
#     for u in graph:
#         for v in graph[u]:
#             in_degree[v] += 1 # 진입차수가 많으면 리스트안에 많겠지요
    
#     for u in graph:
#         in_degree[u] += 0 # 진입차수가 없는 시작노드 0으로 초기화

#     #진입차수가 0인 노드를 큐에 넣기
#     q = deque([node for node in in_degree if in_degree[node] == 0])
#     result = []

#     # 위상정렬
#     while q:
#         node = q.popleft()
#         result.append(node)
#         for nxt in graph[node]:
#             in_degree[nxt] -= 1
#             if in_degree[nxt] == 0:
#                 q.append(nxt)
    
#     if len(result) != len(in_degree):
#         return None #사이클 존재
    
#     return result


# graph = {
#     1: [2,3],
#     2: [4],
#     3: [4],
#     4: []
# }
# print()
# print(topological_sort(graph))

#4 최소신장트리 ------------------------------------------------------------
    #4-1 Kruskal (Union-Find)
        # 가중치가 작은 간선부터 선택함
        # 사이클 유뮤 체크를 위해 Union-Find를 사용
        #1. 간선을 가중치 기준으로 오름차순 정렬
        #2. 간선이 연결한 두 정점이 같은 집합인지 확인
            # 이미 연결되어 있으면 하나의 그룹 상태ex) (1,2) (3,4)
            # -> 추가로 연결하면 사이클이 생기니 안된다
        #3. 다른 그룹끼리는 Union 가능 ex) (1,2)-(3,4)
    #4-2 Prim
#5 최단경로 알고리즘 ------------------------------------------------------------
    #5-1 Dijkstra
    #5-2 Bellman-Ford
    #5-3 Floyd-Warshall