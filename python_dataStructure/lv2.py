# """
# stack
# - LIFO, append(), pop()
# queue
# - FIFO, deque
# 연결리스트(Linked List)
# - 노드, 포인터
# Hash Table
# - 충돌 해결, 키 해싱
# """

# #1. stack문제------------------------------------------------------------------------------------------------
#     #1) pop, push
# st1 = []
# st1.append(10)
# st1.append(20)
# st1.append(30)
# st1.pop()
# print(st1)

#     #2) pop없이 top값 출력
# st2 = [10,20,30,40]
# print(st2[-1])
# print(st2)

#     #3) 괄호 짝 검사
# stw3 = "(())()"
# st3 = []
# isTrue = True
# for i in stw3:
#     if i == "(":
#         st3.append(i)
#     else:
#         if st3:
#             st3.pop()
#         else:
#             isTrue = False
#             break
# if isTrue and not st3:
#     print("괄호 짝 맞아요")
# else:
#     print("땡")

#     #4) 문자열 뒤집기
# stw4 = "apple"
# st4 = list(stw4)
# stwr4 = ""
# while st4:
#     stwr4 += st4.pop()
# print(stwr4)

#     #5) stack 입출력 확인하기
# stc5 = ["push 1", "push 2", "pop", "push 3", "push 4", "pop"]
# st5 = []
# for i in stc5:
#     parts5 = i.split()
#     if parts5[0] == "push":
#         num5 = int(parts5[1])
#         st5.append(num5)
#     elif parts5[0] == "pop":
#         if stc5:
#             print("pop된 값: ", st5.pop())
# print("남은스택 ", st5)
#
#2. queue문제------------------------------------------------------------------------------------------------
# from collections import deque
#     #1) queue 입출력 확인하기
# q1 = ["enqueue 10", "enqueue 20", "dequeue", "enqueue 30", "enqueue 40", "dequeue"]
# qu1 = deque()
# for i in q1:
#     pq1 = i.split()
#     if pq1[0] == "enqueue":
#         qn1 = int(pq1[1])
#         qu1.append(qn1)
#     elif pq1[0] == "dequeue":
#         if qu1:
#             print("출력값 : ", qu1.popleft())
#     #2) queue 다루기
# qu2 = deque()
# qu2.append(1)
# qu2.append(2)
# qu2.append(3)
# while qu2:
#     print("큐 출력", qu2.popleft())

#     #3) 은행 대기열
# qu3 = deque(["A", "B", "c"])
# qu3.popleft()
# qu3.append("D")
# qu3.append("E") #한번에 여러개 x
# qu3.popleft()
# qu3.popleft()
# print(qu3)
#     #4) 사이즈가 있는 야매 큐
# qu4 = deque([]) 
# def enqueue(x):
#     if len(qu4) == 5:
#         print("꽉찼다")
#     else:
#         qu4.append(x)
#         print(x,"투입완료")
# def dequeue():
#     if qu4:
#         print(qu4.popleft(),"제거완료")
#     else:
#         print("비어있다")
# enqueue(10)
# enqueue(20)
# enqueue(30)
# dequeue()
# enqueue(40)
# enqueue(50)
# enqueue(60)
#     #5) 크기가 5인 원형 큐
# size = 5
# queue = [None] * size
# front,rear = 0,0 #front는 꺼낼 위치 rear은 다음 넣을 위치 FIFO
# count = 0

# def enqueue(x):
#     global rear, count
#     if count == size:
#         print("꽉찼다")
#     else:
#         queue[rear] = x
#         rear = (rear+1) % size
#         count += 1
#         print(x, "투입완료")
# def deque():
#     global front, count
#     if count == 0:
#         print("비었음")
#     else:
#         trash = queue[front]
#         queue[front] = None
#         front = (front+1)%size
#         count -= 1
#         print(trash, "제거완료")
# def show_queue():
#     print("큐 상태: ", queue, "front: ", front, "rear: ", rear)
# enqueue(10)
# enqueue(20)
# enqueue(30)
# deque()
# enqueue(40)
# enqueue(50)
# enqueue(60)  # 꽉 차서 못 들어감
# deque()
# deque()
# enqueue(70)
# show_queue()
