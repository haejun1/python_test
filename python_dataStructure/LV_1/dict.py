#3. dictionary문제------------------------------------------------------------------------------------------------
    #1) 조회
d1 = {
    "name": "Alice",
    "age": 25,
    "city": "Seoul"
}
print(d1["age"],d1["city"])

    #2) 새로운 키-값 추가
d2 = {
    "name": "Alice",
    "age": 25
}
d2["email"] = "haejun@gmail.com"
print(d2)

    #3) 값 변경하기
d3 = {
    "name": "pen",
    "price": 1500
}
d3["price"] = 3000
print(d3)

    #4) 키 값 각각 출력
d4 = {
    "name": "Tom",
    "grade": "A",
    "score": 95
}
for key,value in d4.items(): #언패킹
    print(f"{key} : {value}")

    #5) 단어 개수 세기
d5 = "apple banana apple grape banana apple"
d5s = d5.split()
d5d = {}
for i in d5s:
    if i in d5d:
        d5d[i] += 1 #키-값 추가하는 과정
    else:
        d5d[i] = 1
print(d5d)