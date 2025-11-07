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

    #5) stack 입출력 확인하기
stc5 = ["push 1", "push 2", "pop", "push 3", "push 4", "pop"]
st5 = []
for i in stc5:
    parts5 = i.split()
    if parts5[0] == "push":
        num5 = int(parts5[1])
        st5.append(num5)
    elif parts5[0] == "pop":
        if stc5:
            print("pop된 값: ", st5.pop())
print("남은스택 ", st5)