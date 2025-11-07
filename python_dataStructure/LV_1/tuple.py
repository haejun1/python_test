#2. tuple문제------------------------------------------------------------------------------------------------
    #1) 위치, 길이 출력
t1 = (10,20,30,40,50)
t1f = t1[0]
t1l = t1[-1]
t1le = len(t1)
print(t1f, t1l, t1le)

    #2) 튜플 리스트로 바꾸기
t2 = (10,20,30)
t2 = list(t2)
t2.append(40)
t2 = tuple(t2)
print(t2)

    #3) 튜플 언패킹
t3 = ("Alice", 24, "Seoul")
t3name, t3age, t3city = t3
print(t3name, t3age, t3city)

    #4) 튜플 안 튜플 합치기
t4 = ((1,2,3),(4,5),(6,7,8))
t4sum = 0
for i in range(len(t4)):
    t4sum += sum(t4[i])
print(t4sum)

    #5) 튜플 정렬
t5 = [(1,3),(2,2),(3,1)]
t5sorted = sorted(t5, key=lambda x: x[1]) #lamda는 간단한 함수를 한줄로 만들 때 사용
print(t5sorted)