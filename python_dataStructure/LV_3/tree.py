#1 트리 구조와 노드---------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value #노드에 저장할 값
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value) #tree.root가 위 Node클래스의 루트를 참조하게 된다
    
    def print_tree(self, node=None, level = 0):
        if node is None: #처음엔 지정 안돼서 루트노드로 노드가 시작되고
            node = self.root
        print(" " * level + f"{node.value}") #출력하고 
        for child in node.children:
            self.print_tree(child, level + 1) #재귀로 하위노드 출력
        
        #DFS
    def find_node(self, value, node = None): #value는 찾으려는 값
        if node is None:
            node = self.root
        
        if node.value == value: #목표값 찾으면 바로 값 리턴
            return node
        
        for child in node.children:  #첫 노드느 루트노드, 그의 자식들중 찾기
            found = self.find_node(value, child) #찾으려는게 루트노드가 되면
            if found:
                return found #리턴
        return None

# 트리 생성
tree = Tree("A")

# 노드 추가
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
    #a = tree.root임으로 아래 저렇게 쓴 것

tree.root.add_child(b)
tree.root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)

# 트리 출력
print("트리 구조:")
tree.print_tree()

# 노드 탐색
print("\n노드 탐색:")
target = tree.find_node("E")
if target:
    print(f"'{target.value}' 노드를 찾았습니다!")
else:
    print("노드를 찾을 수 없습니다.")




#2 이진트리(Binary Tree)-------------------------------------------------------
    # 전위 순회(왼쪽부터), 중위 순회(루트부터), 후위 순회(오른쪽부터)
#3 이진 탐색트리 (Binary Search Tree)---------------------------------------------------------
