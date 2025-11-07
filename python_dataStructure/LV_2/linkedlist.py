#3. linked list문제------------------------------------------------------------------------------------------------
    #1) 단일 연결 리스트 (단방향 이동)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_node(head, value):
    if head.data == value: #헤드가 삭제 대상이면 
        return head.next #다음 대상을 헤드로 바꾸고(삭제하고) 나감
    
    current = head #시작은 다 헤드에서 시작 (탐색도 O(1))
    while current.next:
        if current.next.data == value: #마침내 현재값의 다음값이 목표값일때(2)
            current.next = current.next.next #앞에서 2개뒤를 이어 다음값인 목표값 삭제(3)
            return head
        current = current.next #현재값을 하나씩 뒤로 옮기면서 (1)
    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = delete_node(node1, 4)
while head:
    print(head.data, ">", end=" ")
    head = head.next

   #2) 이중 연결 리스트 (양방향 이동)
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def delete_node(head, value):
    if head.data == value: 
        return head.next 
    current = head 
    while current.next:
        if current.next.data == value: 
            current.next = current.next.next
            current.next.prev = current
            return head
        current = current.next 
    return head

def insert_node(head,target,value):
    current = head
    new_node = Node(value) #value는 인수 상태, Node로 바꿔 사용해주어야 한다
    while current.next:
        if current.data == target:
            if current.next == None:
                current.next = new_node
                new_node.prev = current
                return head
            origin_next = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = origin_next
            origin_next.prev = new_node
            return head
        current = current.next
    return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
node3.prev = node2
node2.prev = node1

head = insert_node(node1, 20, 25)
while head:
    print(head.data, ">", end=" ")
    head = head.next

   #3) 원형 연결 리스트 (순환의 구조)
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def delete_node(head, value):
    if head.data == value: 
        head.prev.next = head.next
        head.next.prev = head.prev
        return head.next
    elif head.next == None and head.prev == None:
        return None
    current = head 
    while current.next:
        if current.next.data == value: 
            current.next = current.next.next
            current.next.prev = current
            return head
        current = current.next 
        if current == head:
            break
    return head

def insert_node(head,target,value):
    current = head
    origin_head = head
    new_node = Node(value) #value는 인수 상태, Node로 바꿔 사용해주어야 한다
    while current.next:
        if current.data == target:
            if current.next == None:
                current.next = new_node
                new_node.prev = current
                return head
            origin_next = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = origin_next
            origin_next.prev = new_node
            return head
        current = current.next
        if current == origin_head:
            return head
    return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1
node4.prev = node3
node3.prev = node2
node2.prev = node1
node1.prev = node4

head = delete_node(node1, 30)
current = head
while True:
    print(current.data, ">", end=" ")
    current = current.next
    if current == head:
        print(f"(다시 {head.data})")
        break