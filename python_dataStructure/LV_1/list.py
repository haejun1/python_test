#1. list문제------------------------------------------------------------------------------------------------
    #1) 합계, 평균
numbers = [3,7,1,9,2]
nsum = sum(numbers)
navg = nsum / len(numbers)
print(nsum, navg)

    #2) 최대값 최소값
scores = [88,92,79,93,85,91]
smax = max(scores)
smin = min(scores)
print(f"최대값은 {smax}, 최솟값은 {smin}")

    #3) 짝수 판별
nums = [1,4,7,10,13,16]
nums2 = []
for i in nums:
    if i%2 == 0:
        nums2.append(i)
print(nums2)

    #4) 리스트  뒤집기
data = [1,2,3,4,5]
rdata = []
for i in range(len(data)-1):
    rdata.append(data[-i-1])
print(rdata)

    #5) 리스트 정렬
num5 = [4,2,7,2,3,7,1,4]
print(set(num5))