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