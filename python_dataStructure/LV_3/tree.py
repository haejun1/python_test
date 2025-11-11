# #1 트리 구조와 노드---------------------------------------------------------
# class Node:
#     def __init__(self, value):
#         self.value = value #노드에 저장할 값
#         self.children = []
    
#     def add_child(self, child_node):
#         self.children.append(child_node)

# class Tree:
#     def __init__(self, root_value):
#         self.root = Node(root_value) #tree.root가 위 Node클래스의 루트를 참조하게 된다
    
#     def print_tree(self, node=None, level = 0):
#         if node is None: #처음엔 지정 안돼서 루트노드로 노드가 시작되고
#             node = self.root
#         print(" " * level + f"{node.value}") #출력하고 
#         for child in node.children: #B에는 children이 2개라 level유지한채로 2번 반복
#             self.print_tree(child, level + 1) #재귀로 하위노드 출력
        
#         #DFS
#     def find_node(self, value, node = None): #value는 찾으려는 값
#         if node is None:
#             node = self.root
        
#         if node.value == value: #목표값 찾으면 바로 값 리턴
#             return node
        
#         for child in node.children:  #첫 노드느 루트노드, 그의 자식들중 찾기
#             found = self.find_node(value, child) #찾으려는게 루트노드가 되면
#             if found:
#                 return found #리턴
#         return None

# # 트리 생성
# tree = Tree("A")

# # 노드 추가
# b = Node("B")
# c = Node("C")
# d = Node("D")
# e = Node("E")
# f = Node("F")
#     #a = tree.root임으로 아래 저렇게 쓴 것

# tree.root.add_child(b)
# tree.root.add_child(c)
# b.add_child(d)
# b.add_child(e)
# c.add_child(f)

# # 트리 출력
# print("트리 구조:")
# tree.print_tree()

# # 노드 탐색
# print("\n노드 탐색:")
# target = tree.find_node("E")
# if target:
#     print(f"'{target.value}' 노드를 찾았습니다!")
# else:
#     print("노드를 찾을 수 없습니다.")

# #2 이진트리(Binary Tree)-------------------------------------------------------
#     # 전위 순회(preorder), 중위 순회(inorder), 후위 순회(postorder)
#     #          A
#     #      B       C
#     #    D   E   F    G
#     # preorder  : (A->B->D->E->C->F->G)
#     # inorder : (D->B->E->A->F->C->G)
#     # postorder: (D->E->B->F->G->C->A)
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None #왼쪽자식
#         self.right = None

# def preorder(node):
#     if node:
#         print(node.value, end=' ')
#         preorder(node.left)
#         preorder(node.right)

# def inorder(node):
#     if node:
#         inorder(node.left)
#         print(node.value, end=' ')
#         inorder(node.right)

# def postorder(node):
#     if node:
#         postorder(node.left)
#         postorder(node.right)
#         print(node.value, end=' ')

# root = Node("A")
# root.left = Node("B")
# root.right = Node("C")
# root.left.left = Node("D")
# root.left.right = Node("E")
# root.right.left = Node("F")
# root.right.right = Node("G")

# print("루트부터 전위 순회 preorder : ")
# preorder(root)
# print("\n")

# print("왼쪽 루트 오른쪽의  중위 순회 (Inorder):")
# inorder(root)
# print("\n")

# print("왼쪽 오른쪽 루트의  후위 순회 (Postorder):")
# postorder(root)
# print("\n")

#3 이진 탐색트리 (Binary Search Tree)---------------------------------------------------------
    #왼쪽 서브트리에는 부모보다 작은 값
    #오른쪽 서브트리에는 부모보다 큰 값
    #탐색,삽입,삭제가 평균 O(log n)
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertRecursive(self.root, value) #recursive = 재귀적
        
    def insertRecursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insertRecursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insertRecursive(node.right, value)
        
    def search(self, value):
        return self.searchRecursive(self.root, value)
    
    def searchRecursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self.searchRecursive(node.left, value)
        else:
            return self.searchRecursive(node.right, value)
        
    def preorder(self, node, level = 0):
        if node:
            print(" "*level, node.value)
            self.preorder(node.left, level+1)
            self.preorder(node.right, level+1)

bst = BinarySearchTree()

for num in [5,3,1,6,7,2,4]:
    bst.insert(num)

print("전위 순회 결과 : ")
bst.preorder(bst.root)
print("\n")

print("탐색 결과 : ")
for target in [5,2,10]:
    found = bst.search(target)
    print(f"{target} : {'있음' if found else '없음'}")
