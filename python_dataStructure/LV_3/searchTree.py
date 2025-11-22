# #1 이진 탐색트리 (Binary Search Tree)---------------------------------------------------------
#     #왼쪽 서브트리에는 부모보다 작은 값
#     #오른쪽 서브트리에는 부모보다 큰 값
#     #탐색,삽입,삭제가 평균 O(log n)
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.right = None
#         self.left = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self.insertRecursive(self.root, value) #recursive = 재귀적
        
#     def insertRecursive(self, node, value):
#         if value < node.value:
#             if node.left is None:
#                 node.left = Node(value)
#             else:
#                 self.insertRecursive(node.left, value)
#         elif value > node.value:
#             if node.right is None:
#                 node.right = Node(value)
#             else:
#                 self.insertRecursive(node.right, value)
        
#     def search(self, value):
#         return self.searchRecursive(self.root, value)
    
#     def searchRecursive(self, node, value):
#         if node is None:
#             return False
#         if node.value == value:
#             return True
#         elif value < node.value:
#             return self.searchRecursive(node.left, value)
#         else:
#             return self.searchRecursive(node.right, value)
        
#     def preorder(self, node, level = 0):
#         if node:
#             print(" "*level, node.value)
#             self.preorder(node.left, level+1)
#             self.preorder(node.right, level+1)

# bst = BinarySearchTree()

# for num in [5,3,1,6,7,2,4]:
#     bst.insert(num)

# print("전위 순회 결과 : ")
# bst.preorder(bst.root)
# print("\n")

# print("탐색 결과 : ")
# for target in [5,2,10]:
#     found = bst.search(target)
#     print(f"{target} : {'있음' if found else '없음'}")

# #2 AVL트리 (AVL Tree)---------------------------------------------------------
#     #균형을 맞추는 트리
#     #Right Rotation (LL회전)
#         #왼쪽으로 치우쳐져 있어 오른쪽으로 회전
#         #       z         y
#         #    y     ->  x     z
#         # x
#     # Left Rotation (RR 회전)
#         #오른쪽으로 치우쳐져 있어 왼쪽으로 회전 (Left Rotation)
#         #  x               y
#         #     y      ->  x    z
#         #       z
#     # Left Right 회전 (LR 회전)
#         #왼쪽 자식의 오른쪽에 삽입되어 불균형 → 
#         #왼쪽 자식 기준으로 왼쪽 회전 후, 부모 기준으로 오른쪽 회전
#         #   z         z         y
#         # x   ->     y     -> x   z
#         #  y       x
#     # Right Left 회전 (RL 회전)
#         #오른쪽 자식의 왼쪽에 삽입되어 불균형 → 
#         #오른쪽 자식 기준으로 오른쪽 회전 후, 부모 기준으로 왼쪽 회전
#         #  x         x            y
#         #     z   ->   y     -> x   z
#         #   y            z

# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.height = 1

# def height(n):
#     return n.height if n else 0

# def update_height(n):
#     n.height = max(height(n.left), height(n.right))+1

# def balance_factor(n):
#     return height(n.left) - height(n.right)

# def LL(z):
#     #     z
#     #    / 
#     #   y
#     #  / \
#     # x   T3
#     y = z.left
#     T1 = y.right

#     y.right = z
#     z.left = T1
#     #z가 T3에 들어가는 회전이다
#     #이 과정에서 사라질 서브트리 T3을 지키기 위해 T3을 보존
    
#     update_height(z)
#     update_height(y)
#     return y

# def RR(z):
#     y = z.right
#     T2 = y.left

#     y.left = z
#     z.right  = T2

#     update_height(z)
#     update_height(y)
#     return y

# def LR(z):
# #     z           z        y
# #  x      ->    y   ->   x   z
# #    y        x
#     z.left = RR(z.left)
#     return LL(z)
    
# def RL(x):
# #  x         x             y
# #      z ->    y     ->  x   z
# #    y           z
#     x.right = LL(x.right)
#     return RR(x)

# def insert(node, key):
#     if not node:
#         return Node(key)

#     if key < node.key:
#         node.left = insert(node.left, key)
#     else:
#         node.right = insert(node.right, key)

#     update_height(node)

#     bf = balance_factor(node)

#     if bf > 1 and key < node.left.key:
#         return LL(node)

#     if bf < -1 and key > node.right.key:
#         return RR(node)

#     if bf > 1 and key > node.left.key:
#         return LR(node)

#     if bf < -1 and key < node.right.key:
#         return RL(node)

#     return node

# def print_tree(node, indent=0):
#     if node is not None:
#         print_tree(node.right, indent + 4)
#         print(" " * indent + f"{node.key}")
#         print_tree(node.left, indent + 4)

# root = None
# for num in [5,3,1,6,7,2,4]:
#     print(f"\n=== Insert {num} ===")
#     root = insert(root, num)
#     print_tree(root)

# #3 레드 블랙 트리 (Red Black Tree)---------------------------------------------------------
# """
# 특징
# - 루트 노드와 리프 노드 : 블랙
# - 루트 노드에서 리프 노드까지 경로에서 레드 노드가 연속으로 나올 수 없음
#     : 부모 노드가 레드면, 자식 노드는 무조건 블랙 -> 레드 규칙(insert 연산)
# - 블랙 블랙은 가능
# - 루트 노드에서 리프 노드까지 모든 경로에서 블랙 노드 개수는 같음
#     : delete 연산으로 인해 블랙 노드가 삭제되는 경우
# - 새 노드는 빨강
# - 삼촌이 빨강이면 recolor
# - 삼촌이 검정이면 회전 + recolor
# """
# RED = True
# BLACK = False

# class Node:
#     def __init__(self, key, color="RED"):
#         self.key = key
#         self.color = color
#         self.left = None
#         self.right = None
#         self.parent = None

# def LL(root, x):
#     y = x.left
#     x.left = y.right

#     if y.right:
#         y.right.parent = x

#     y.parent = x.parent

#     if not x.parent:
#         root = y
#     elif x == x.parent.right:
#         x.parent.right = y
#     else:
#         x.parent.left = y

#     y.right = x
#     x.parent = y

#     return root

# def RR(root, x):
#     y = x.right
#     x.right = y.left

#     if y.left:
#         y.left.parent = x

#     y.parent = x.parent

#     if not x.parent:
#         root = y
#     elif x == x.parent.left:
#         x.parent.left = y
#     else:
#         x.parent.right = y

#     y.left = x
#     x.parent = y

#     return root

# def bst_insert(root, z): #이진 탐색트리 규칙으로 삽입
#     parent = None
#     cur = root

#     while cur:
#         parent = cur
#         if z.key < cur.key:
#             cur = cur.left
#         else:
#             cur = cur.right

#     z.parent = parent

#     if not parent:
#         return z
#     elif z.key < parent.key:
#         parent.left = z
#     else:
#         parent.right = z

#     return root

# def insert_fix(root, z): #Red Black 규칙으로 수정
#     #insert_fix는 부모가 red일 때만 작동한다
#     #(black이면 자연스럽게 red자식으로 들어오면 되니깐)
#     while z.parent and z.parent.color == RED:
#         if z.parent == z.parent.parent.left:
#             uncle = z.parent.parent.right
#             # Case 1: 삼촌 RED = recolor
#             if uncle and uncle.color == RED:
#                 z.parent.color = BLACK
#                 uncle.color = BLACK
#                 z.parent.parent.color = RED
#                 z = z.parent.parent
#             else:
#                 # Case 2: 삼촌 BLACK + z가 오른쪽
#                 if z == z.parent.right:
#                     z = z.parent
#                     root = RR(root, z)
#                 # Case 3: 삼촌 BLACK + z가 왼쪽
#                 z.parent.color = BLACK
#                 z.parent.parent.color = RED
#                 root = LL(root, z.parent.parent)
#         else:
#             # 반대 방향 (대칭)
#             uncle = z.parent.parent.left
#             if uncle and uncle.color == RED:
#                 z.parent.color = BLACK
#                 uncle.color = BLACK
#                 z.parent.parent.color = RED
#                 z = z.parent.parent
#             else:
#                 if z == z.parent.left:
#                     z = z.parent
#                     root = LL(root, z)
#                 z.parent.color = BLACK
#                 z.parent.parent.color = RED
#                 root = RR(root, z.parent.parent)

#     root.color = BLACK
#     return root

# def insert(root, key):
#     z = Node(key)
#     root = bst_insert(root, z)
#     root = insert_fix(root, z)
#     return root

# def print_tree(node, indent=0):
#     if node:
#         print_tree(node.right, indent + 4)
#         color = "R" if node.color == RED else "B"
#         print(" " * indent + f"{node.key}({color})")
#         print_tree(node.left, indent + 4)

# root = None
# for x in [7,3,18,10,22,8,11,26]:
#     print(f"\n=== Insert {x} ===")
#     root = insert(root, x)
#     print_tree(root)

#4 B 트리 (B Tree)---------------------------------------------------------
# 하나의 노드 안에 여러 key값을 저장한다
# 여러 자식 노드를 가질 수 있다.
# 항상 균형을 유지하기 좋다 (낮은 높이 유지 가능)
# 규칙
    # 항상 리프노드에 insert
    # 정렬을 유지하여(bst) key를 노드에 insert
    # 노드가 key 개수를 초과하면 split (노드의 최대 key 개수를 정해둠)
    # split으로 중앙값이 부모로 올라가는 형식
    # 부모도 초과되면 부모도 split하는 거임 (루트도 split 및 새 루트 생성 가능)
    # 노드안에 k의 데이터가 있다 -> 자식 노드의 수는 k+1개여야 한다
        # 루트 노드는 항상 2개 이상의 자식을 갖는다
    # 리프노드의 key만 삭제 가능하다 (리프노드가 아니라면 변형해서 삭제해야 함)
    # t(차수)는 BTree가 유지해야하는 최소 용량을 말한다
        # 각 노드는 2t-1개의 key, 2t의 자식을 가질 수 있다 (t는 차수)
        # 한 노드가 가져야하는 최소 key의 수는 t-1
        
class BTreeNode:
    def __init__(self, t, leaf = False):
        self.t = t #최소 차수
        self.keys = []
        self.children = []
        self.leaf = leaf # 리프노드 여부(기본은 루트임으로 False)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, leaf = True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1: #루트가 꽉차면 split
            new_root = BTreeNode(self.t, leaf = False) #루트화
            new_root.children.append(root) #리스트에 append로 넣어줌
            self.split_child(new_root, 0)
            self.insert_nonfull(new_root, key)
            self.root = new_root
        else:
            self.insert_nonfull(root, key)

    def insert_nonfull(self, node, key): #꽉 안 찬 노드
        i = len(node.keys) -1
        if node.leaf: #안 찬게 리프 노드가 맞으면 key추가
            node.keys.append(key)
            node.keys.sort()
        else:
            #내려갈 위치 찾기
            while i >=0 and key < node.keys[i]:
                i -= 1
            i += 1

            #내려갈 자식이 full이면 split
            if len(node.children[i].keys) == 2*self.t - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self.insert_nonfull(node.children[i], key)

    #자식 노드 split -> 중간key가 위로 올라감, 나머지는 좌/우로 분리
    def split_child(self, parent, i):
        t = self.t
        full_child = parent.children[i]

        #오른쪽 새노드 생성
        new_node = BTreeNode(t, leaf=full_child.leaf)
        
        #오른쪽 키들 복사
        new_node.keys = full_child.keys[t:]

        #leaf가 아니면 children도 분배
        if not full_child.leaf:
            new_node.children = full_child.children[t:]
            full_child.children = full_child.children[:t]
        
        #가운데 key를 parent로 올림
        parent.keys.insert(i, full_child.keys[t-1])

        #왼쪽 절반만 남겨서 저장(parent로 올린 중간 값 빼고)
        full_child.keys = full_child.keys[:t-1]

        #정리 끝내고 새로만든 오른쪽 노드에 추가
        parent.children.insert(i+1, new_node)

bt = BTree(t=2)

for num in [10,20,5,6,12,30,7,17]:
    bt.insert(num)

print("Root keys : ", bt.root.keys)
for i, child in enumerate(bt.root.children):
    print(f"Child {i} keys : ", child.keys)
