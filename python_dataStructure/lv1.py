"""
list
- 인덱싱, 슬라이싱, 추가, 삭제, 복사
tuple
- 좌표 저장
dict
- 키-값 구조, 검색
set
- 중복 제거, 집합 연산
"""

#1. list문제------------------------------------------------------------------------------------------------
#     #1) 합계, 평균
# numbers = [3,7,1,9,2]
# nsum = sum(numbers)
# navg = nsum / len(numbers)
# print(nsum, navg)

#     #2) 최대값 최소값
# scores = [88,92,79,93,85,91]
# smax = max(scores)
# smin = min(scores)
# print(f"최대값은 {smax}, 최솟값은 {smin}")

#     #3) 짝수 판별
# nums = [1,4,7,10,13,16]
# nums2 = []
# for i in nums:
#     if i%2 == 0:
#         nums2.append(i)
# print(nums2)

#     #4) 리스트  뒤집기
# data = [1,2,3,4,5]
# rdata = []
# for i in range(len(data)-1):
#     rdata.append(data[-i-1])
# print(rdata)

#     #5) 리스트 정렬
# num5 = [4,2,7,2,3,7,1,4]
# print(sorted(set(num5)))



#2. tuple문제------------------------------------------------------------------------------------------------
#     #1) 위치, 길이 출력
# t1 = (10,20,30,40,50)
# t1f = t1[0]
# t1l = t1[-1]
# t1le = len(t1)
# print(t1f, t1l, t1le)

#     #2) 튜플 리스트로 바꾸기
# t2 = (10,20,30)
# t2 = list(t2)
# t2.append(40)
# t2 = tuple(t2)
# print(t2)

#     #3) 튜플 언패킹
# t3 = ("Alice", 24, "Seoul")
# t3name, t3age, t3city = t3
# print(t3name, t3age, t3city)

#     #4) 튜플 안 튜플 합치기
# t4 = ((1,2,3),(4,5),(6,7,8))
# t4sum = 0
# for i in range(len(t4)):
#     t4sum += sum(t4[i])
# print(t4sum)

#     #5) 튜플 정렬
# t5 = [(1,3),(2,2),(3,1)]
# t5sorted = sorted(t5, key=lambda x: x[1])
# print(t5sorted)



#3. dictionary문제------------------------------------------------------------------------------------------------
#     #1) 조회
# d1 = {
#     "name": "Alice",
#     "age": 25,
#     "city": "Seoul"
# }
# print(d1["age"],d1["city"])

#     #2) 새로운 키-값 추가
# d2 = {
#     "name": "Alice",
#     "age": 25
# }
# d2["email"] = "haejun@gmail.com"
# print(d2)

#     #3) 값 변경하기
# d3 = {
#     "name": "pen",
#     "price": 1500
# }
# d3["price"] = 3000
# print(d3)

#     #4) 키 값 각각 출력
# d4 = {
#     "name": "Tom",
#     "grade": "A",
#     "score": 95
# }
# for key,value in d4.items():
#     print(f"{key} : {value}")

#     #5) 단어 개수 세기
# d5 = "apple banana apple grape banana apple"
# d5s = d5.split()
# d5d = {}
# for i in d5s:
#     if i in d5d:
#         d5d[i] += 1
#     else:
#         d5d[i] = 1
# print(d5d)



#4. set문제------------------------------------------------------------------------------------------------
    #1) 중복 제거
s1 = [1,2,2,3,4,4,5]
s1 = set(s1)
print(s1)

    #2) 추가 및 제거
s2 = {1,2,3,4,5}
s2.add(6)
s2.remove(2)
print(s2)

    #3) 집합연산
s3a = {1,2,3,4}
s3b = {3,4,5,6}
s3inter = s3a.intersection(s3b) #교집합= &
s3union = s3a.union(s3b)        #합집합= |
s3diff = s3a.difference(s3b)    #차집합= -
print(s3inter, s3union, s3diff)

    #4) 중복제거
s4 = "banana"
s4 = set(s4)
print(s4)

    #5) 집합여부
s5x = {1,2,3}
s5y = {1,2,3,4,5}
isxyqn = bool(s5x.issubset(s5y)) #부분집합
isyxqn = bool(s5y.issubset(s5x))
print(isxyqn, isyxqn)