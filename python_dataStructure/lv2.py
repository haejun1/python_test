"""
stack
- LIFO, append(), pop()
queue
- FIFO, deque
연결리스트(Linked List)
- 노드, 포인터
Hash Table
- 충돌 해결, 키 해싱
"""
#1. stack문제------------------------------------------------------------------------------------------------
    #1) pop, push
st1 = []
st1.append(10)
st1.append(20)
st1.append(30)
st1.pop()
print(st1)
    #2) pop없이 top값 출력
st2 = [10,20,30,40]
print(st2[-1])
print(st2)
    #3) 괄호 짝 검사
stw3 = "(())()"
st3 = []
isTrue = True
for i in stw3:
    if i == "(":
        st3.append(i)
    else:
        if st3:
            st3.pop()
        else:
            isTrue = False
            break
if isTrue and not st3:
    print("괄호 짝 맞아요")
else:
    print("땡")
    #4) 문자열 뒤집기
stw4 = "apple"
st4 = list(stw4)
stwr4 = ""
while st4:
    stwr4 += st4.pop()
print(stwr4)
    #5) 여러 자료를 스택으로 정리
stc5 = ["push 1", "push 2", "pop", "push 3", "push 4", "pop"]
st5 = []
