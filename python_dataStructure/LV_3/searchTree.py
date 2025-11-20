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

#3 레드 블랙 트리 (Red Black Tree)---------------------------------------------------------
"""
특징
- 트리의 모든 노드는 블랙 아니면 레드
- 루트 노드와 리프 노드 : 블랙
- 루트 노드에서 리프 노드까지 경로에서 레드 노드가 연속으로 나올 수 없음
    : 부모 노드가 레드면, 자식 노드는 무조건 블랙 -> 레드 규칙(insert 연산)
- 루트 노드에서 리프 노드까지 모든 경로에서 블랙 노드 개수는 같음
    : delete 연산으로 인해 블랙 노드가 삭제되는 경우
- 새 노드는 빨강
- 삼촌이 빨강이면 recolor
- 삼촌이 검정이면 회전 + recolor
"""
RED = True
BLACK = False

class Node:
    def __init__(self, key, color="RED"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

def LL(root, x):
    y = x.left
    x.left = y.right

    if y.right:
        y.right.parent = x

    y.parent = x.parent

    if not x.parent:
        root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y

    y.right = x
    x.parent = y

    return root

def RR(root, x):
    y = x.right
    x.right = y.left

    if y.left:
        y.left.parent = x

    y.parent = x.parent

    if not x.parent:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y

    return root

def bst_insert(root, z): #이진 탐색트리 규칙으로 삽입
    parent = None
    cur = root

    while cur:
        parent = cur
        if z.key < cur.key:
            cur = cur.left
        else:
            cur = cur.right

    z.parent = parent

    if not parent:
        return z
    elif z.key < parent.key:
        parent.left = z
    else:
        parent.right = z

    return root

def insert_fix(root, z): #Red Black 규칙으로 수정
    while z.parent and z.parent.color == RED:
        if z.parent == z.parent.parent.left:
            uncle = z.parent.parent.right
            # Case 1: 삼촌 RED = recolor
            if uncle and uncle.color == RED:
                z.parent.color = BLACK
                uncle.color = BLACK
                z.parent.parent.color = RED
                z = z.parent.parent
            else:
                # Case 2: 삼촌 BLACK + z가 오른쪽
                if z == z.parent.right:
                    z = z.parent
                    root = RR(root, z)
                # Case 3: 삼촌 BLACK + z가 왼쪽
                z.parent.color = BLACK
                z.parent.parent.color = RED
                root = LL(root, z.parent.parent)
        else:
            # 반대 방향 (대칭)
            uncle = z.parent.parent.left
            if uncle and uncle.color == RED:
                z.parent.color = BLACK
                uncle.color = BLACK
                z.parent.parent.color = RED
                z = z.parent.parent
            else:
                if z == z.parent.left:
                    z = z.parent
                    root = LL(root, z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                root = RR(root, z.parent.parent)

    root.color = BLACK
    return root

def insert(root, key):
    z = Node(key)
    root = bst_insert(root, z)
    root = insert_fix(root, z)
    return root

def print_tree(node, indent=0):
    if node:
        print_tree(node.right, indent + 4)
        color = "R" if node.color == RED else "B"
        print(" " * indent + f"{node.key}({color})")
        print_tree(node.left, indent + 4)

root = None
for x in [7,3,18,10,22,8,11,26]:
    print(f"\n=== Insert {x} ===")
    root = insert(root, x)
    print_tree(root)


#4 B 트리 (B Tree)---------------------------------------------------------
