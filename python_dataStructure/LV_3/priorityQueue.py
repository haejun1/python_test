#--------------우선순위 큐 = 힙------------------------
# #1 이진 힙-------------------------------------------------------------
#     # 완전 이진 트리 : 빈 곳 없이 왼쪽부터 채워진 이진 트리
#         # 배열 인덱스를 사용해 부모/자식 위치 계산을 쉽게 함
#             # 특정 노드 i에 대해서
#                 # 부모 : i//2
#                 # 왼쪽 자식 : i*2
#                 # 오른쪽 자식 : i*2 + 1
#     # 최소 힙 : 루트가 항상 가장 작은 값
#     # or 최대 힙 : 루트가 항상 가장 큰 값
#     #!!! 루트가 최소or 최대인건 맞음
#     #!!! 다만 마지막 노드값이 최대 or 최소인건 x
#     #!!! 부모가 자식보다 크거나 작으면 만족하는 구조임
#     #     1
#     #  3     2   도 가능
# class MinHeap: #루트가 최소값
#     def __init__(self):
#         self.heap = [None]  # index 1부터 시작

#     def push(self, value):
#         self.heap.append(value)
#         self._up(len(self.heap)-1)

#     # 위로 올리기 (heapify-up)
#     def _up(self, idx):
#         while idx > 1:
#             parent = idx // 2
#             if self.heap[parent] > self.heap[idx]:
#                 self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
#                 idx = parent
#             else:
#                 break

#     # 최소값 제거(pop)
#     def pop(self):
#         if len(self.heap) == 1:
#             return None
        
#         # 루트 제거
#         root = self.heap[1]

#         # 마지막 노드를 루트로 이동
#         self.heap[1] = self.heap[-1]
#         self.heap.pop()
#             # 마지막 노드를 루트로 복사해놨고
#             # 원래 마지막 노드의 위치인 맨 끝 요소를 제거함 (LIFO 스택)
        
#         # 아래로 내리기 (heapify-down)
#         self._down(1) #다시 정렬
#         return root

#     # 아래로 내리기
#     def _down(self, idx):
#         while True:
#             left = idx * 2
#             right = idx * 2 + 1
#             smallest = idx

#             if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#                 smallest = left

#             if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#                 smallest = right

#             #최소값이 바뀌면 여기로 와서 idx를 smallest로 바꿔주네
#             if smallest != idx:
#                 self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
#                 idx = smallest
#             else:
#                 break

# # 테스트
# h = MinHeap()
# h.push(5)
# h.push(3)
# h.push(8)
# h.push(1)

# print(h.pop())  # 1
# print(h.pop())  # 3
# print(h.pop())  # 5
# print(h.pop())  # 8

#2 허프만 코딩-------------------------------------------------------------
    # 문자 빈도가 높은 것은 짧은 비트
    # 낮은것은 긴 비트로 압축하는 알고리즘
    # -> 효율적으로 비트 길이를 분배해서 전체 길이를 최소화 하는 방식
    # 가장 낮은 빈도의 문자 2개를 하나의 노드로 합치는 작업을 반복하는 것
        #ex) A A A B B C 가 있을 때
            # A(3) B(2) C(1) 임으로 B와 C를 합친 X(3)
            # X(3) 자식으로 B(2)와 C(1)이 있고 A와 X 의 부모로 루트(6)이 있는겨

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # priorityQueue에서 비교될 때 freq 기준으로 정렬되도록
    def __lt__(self, other):
        return self.freq < other.freq
    

def huffman(chars):
    pq = []
    for ch, freq in chars.items():
        heapq.heappush(pq, Node(ch, freq))

    #합쳐서 트리 만듦
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(pq, parent)

    root = pq[0]
    codes = {}

    def dfs(node, code):
        if not node:
            return
        if node.char is not None:
            codes[node.char] = code
        dfs(node.left, code + "0")
        dfs(node.right, code + "1")
    
    dfs(root, "")
    return codes

freq = {"A": 3, "B": 2, "C": 1}
print(huffman(freq))