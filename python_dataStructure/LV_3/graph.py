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

# #4 최소신장트리(MST) ------------------------------------------------------------
#     #4-1 Kruskal (Union-Find)
#         # 가중치가 작은 간선부터 선택함
#         # 사이클 유뮤 체크를 위해 Union-Find를 사용
#         #1. 간선을 가중치 기준으로 오름차순 정렬
#         #2. 간선이 연결한 두 정점이 같은 집합인지 확인
#             # 이미 연결되어 있으면 하나의 그룹 상태ex) (1,2) (3,4)
#             # -> 추가로 연결하면 사이클이 생기니 안된다
#         #3. 다른 그룹끼리는 Union 가능 ex) (1,2)-(3,4)

# class UnionFind:
#     def __init__(self, n): #n은 정점 개수
#         self.parent = list(range(n+1)) #parent, 초기엔 자기 자신을 부모로 가짐
#                                         #연결을 통해 그룹 상태가 되면 첫 정점이 parent가 됨
#         self.rank = [0] * (n+1) #각 집합의 높이를 뜻함
#                                 #집합끼리 Union했을 때 높은 랭크 밑으로 들어감
    
#     def find(self, x):
#         if self.parent[x] != x: #독립 노드가 아니면
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
    
#     def union(self, a, b):
#         ra, rb = self.find(a), self.find(b) #부모 찾고
#         if ra == rb: #같은 그룹이면 합치면 안되니깐 False
#             return False
        
#         if self.rank[ra] < self.rank[rb]: # 높은 rank밑으로 들어감
#             self.parent[ra] = rb
#         elif self.rank[ra] > self.rank[rb]:
#             self.parent[rb] = ra
#         else: #둘이 높이 같으면 그냥 ra가 큰걸로 ㅎ
#             self.parent[rb] = ra 
#             self.rank[ra] += 1
#         return True

# def kruskal(edges, n):
#     edges.sort(key=lambda x:x[2]) #(u,v,w) 중 w를 기준으로 정렬하겠다
#     uf = UnionFind(n)

#     mst = []
#     total_weight = 0

#     for u,v,w in edges:
#         if uf.union(u,v):
#             mst.append((u,v,w))
#             total_weight += w

#     return mst, total_weight

# edges = [
#     (1, 2, 1),
#     (1, 3, 3),
#     (2, 4, 2),
#     (3, 4, 4),
# ]

# mst, total = kruskal(edges, 4)
# print("MST:", mst)
# print("Total Weight:", total)

#     #4-2 Prim
#         #가장 싼 비용으로 확장해 가는 방식
#         # 1. 아무 시작 노드를 고름
#         # 2. 그 노드 중 가장 가중치가 작은 것을 선택 -> 반복
#             # ex) a에서의 간선이 2개 였고 가중치가 작은 b를 택함
#             # ex) a-c와 b-d중 가중치가 작은 걸 선택
#             # => 새로 연결된 노드도 후보로 올라 그중 작은 걸 선택하는 방식

# import heapq 
# #우선순위가 가장작은 요소를 꺼내주는 Heap 라이브러리
# # 우선순위 큐 = Heap
# from collections import defaultdict

# def prim(graph, start=1):
#     visited = set()
#     pq = []
#     total_cost = 0

#     # start에서 뻗는 간선들을 넣기
#     visited.add(start)
#     for nxt, w in graph[start]:
#         heapq.heappush(pq, (w, start, nxt))

#     mst = []

#     while pq:
#         w, u, v = heapq.heappop(pq)

#         # 이미 방문한 노드면 skip
#         if v in visited:
#             continue

#         visited.add(v)
#         mst.append((u, v, w))
#         total_cost += w

#         # 새로 들어온 v에서 뻗는 간선들 추가
#         for nxt, w2 in graph[v]:
#             if nxt not in visited:
#                 heapq.heappush(pq, (w2, v, nxt))

#     return mst, total_cost


# #5 최단경로 알고리즘 ------------------------------------------------------------
#     #5-1 Dijkstra
#         # 하나의 정점에서 다른 모든 정점까지의 최소비용(거리)
#         # 최단거리는 "항상" 작은 비용을 먼저 선택 => Heap사용
#         # 양수 가중치만 계산 가능 (음수 포함시 Bellman-Ford 사용 필요)

# import heapq
# from collections import defaultdict

# def dijkstra(start, graph):
#     INF = float('inf') #infinity 무한대를 뜻하는 특수한 실수 값
#     dist = {node: INF for node in graph} #distance, 각 노드의 초기 거리를 무한대로 설정
#     dist[start] = 0 # 시작은 0

#     pq = [(0,start)] #(거리,노드)를 저장함

#     while pq:
#         cur_dist, node = heapq.heappop(pq) #힙에서 pop하는 방식

#         #거리가 더 멀면 최소거리가 아니므로 무시
#         if cur_dist > dist[node]:
#             continue

#         for nxt, weight in graph[node]:
#             new_dist = cur_dist + weight

#             if new_dist < dist[nxt]:
#                 dist[nxt] = new_dist
#                 heapq.heappush(pq, (new_dist, nxt))

#     return dist

# graph = defaultdict(list)
# graph[1] = [(2, 1), (3, 4)]
# graph[2] = [(4, 2)]
# graph[3] = [(4, 1)]
# graph[4] = []

#     #5-2 Bellman-Ford
#         # 다익스트라에서 음수 간선까지 처리하는 알고리즘
#         # 음수 찾는 법
#             # 모든 간선을 N-1번 반복하여 최단거리를 갱신 (287줄 참고)
#             # N번째 반복에도 값이 줄어든다면? ==> 음수 간선 존재

# def bellman_ford(graph, start, n):
#     INF = float('inf')
#     dist = {node: INF for node in graph}
#     dist[start] = 0

#     for _ in range(n-1):
#         for u in graph:
#             # 전 정점+가중치가 현 노드보다 작으면 최단거리 갱신
#             for v, w in graph[u]:
#                 if dist[u] + w < dist[v]:
#                     dist[v] = dist[u] + w 
            
#     # 모든 간선을 갱신했는데도 더 작은 값이 나온다는 건 음수 간선이 존재한다는 것
#     for u in graph:
#         for v,w in graph[u]:
#             if dist[u] + w < dist[v]:
#                 return "Negative cycle detected!"
    
#     return dist

# n = 4
# graph = {
#     1: [(2, 4), (3, 1)],
#     2: [(4, 2)],
#     3: [(2, -2), (4, 5)],
#     4: []
# }

# result = bellman_ford(graph, 1, n)
# print(result)


    #5-3 Floyd-Warshall
        #모든 정점 간 쌍방향 최단거리
        #방향/무방향/양수/음수 모두 가능
        #DP동적프로그래밍 기반으로 작동
            #dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

def floyd_warshall(graph, n):
    INF = float('inf')

    #거리 행렬 초기화
        #dist[i][j] = i노드에서 j노드까지의 현재 최단거리
    #(n+1) * (n+1) 행렬을 초기화 하고 시작하는 것
    dist = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dist[i][i] = 0

    #간선 반영
    for u in graph:
        for v,w in graph[u]:
            dist[u][v] = w

    #floyd_warshall
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

graph = {
    1: [(2, 4), (3, 1)],
    2: [(4, 2)],
    3: [(2, 2), (4, 5)],
    4: []
}

n = 4
dist = floyd_warshall(graph, n)

for row in dist[1:]:
    print(row[1:])