# #1 선택정렬
#     # 배열 중 가장 작은 값을 골라 맨 앞과 교환
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j]<arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i] #i에 min값 넣어주고, min에는 원래 i값 넣어줌 (교환 느낌, 순차적으로 하는게 x)

#     return arr

# print(selection_sort([9,4,1,6,3]))
# #19463
# #13946
# #13496
# #13469


# #2 삽입정렬
#     # 왼쪽은 정렬됐다고 가정하고  오른쪽에서 하나씩 값을 꺼내 자기 자리 앞으로 이동해 정렬
# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1
        
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1

#         arr[j+1] = key
#     return arr

# print(insertion_sort([5, 2, 9, 1, 5, 6]))
# #259156
# #259156
# #125956
# #125596
# #125569

# #3 쉘정렬
#     #멀리 떨어진 요소끼리 먼저 정렬해서 전체를 빠르게 정렬하고
#     #간격을 줄여가며 삽입정렬로 다듬기
# def shell_sort(arr):
#     n = len(arr)
#     gap = n//2

#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i

#             while j >= gap and arr[j-gap] > temp:
#                 arr[j] = arr[j-gap]
#                 j -= gap
            
#             arr[j] = temp
        
#         gap //=2

#     return arr

# print(shell_sort([12, 34, 54, 2, 3]))
#     #gap = 2일 때
#         #12 34 54 2 3 (i = 2)
#         #12 2 54 34 3 (i = 3)
#         #3 2 12 34 54 (i = 4)
#     #gap = 1일 때 (= 삽입정렬)
#         #2 3 12 34 54


# #4 힙 정렬
#     # 완전이진트리 사용
#     # 최대힙 사용, 오름차순 정렬
#     # 루트가 최대값, 자식은 부모보다 작음
#     # 과정 좀 헷갈림 디버깅버전 참고
# def heapify(arr, n, i):
#     largest = i
#     left = 2*i+1
#     right = 2*i+2

#     if left < n and arr[left] > arr[largest]:
#         largest = left
    
#     if right < n and arr[right] > arr[largest]:
#         largest = right

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#     #heapify는 최대값을 쉽게 알수 있는 준비가 된 상태
#     #추가적인 정렬은 그 후에 진행 하는 것

# def heap_sort(arr):
#     n = len(arr)
#     #자식이 존재하려면 2i+1보다 큰 n이여야함
#     #   2i+1<n
#     # = i < (n-1)/2
#     # 따라서 이를 만족하는 가장 큰 정수i는 (n-1)/2의 올림값인 n//2-1이 된다
#     # 즉 n//2 - 1은 마지막 부모노드의 인덱스 = 맨오른쪽 아래 부모노드
#         #마지막 부모노드부터 루트노드까지 이동한다는 뜻 
#     #배열을 최대힙으로 변환했다.
#                     #range(start, end, step)
#                     #i는 n//2-1부터 -1까지 반복됐다
#     for i in range(n//2-1, -1, -1): 
#         heapify(arr,n,i)

#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr,i,0)

#     return arr

# arr = [4, 10, 3, 5, 1]
# print(heap_sort(arr))


# #5 합병 정렬
#     # divide : 배열을 반으로 계속 쪼갬
#     # conquer : 각 조각을 정렬
#     # merge : 정렬된 두 배열을 합쳐 더 큰 정렬된 배열을 만듦

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)


# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right): #좌,우는 이미 각각 정렬된 상태
#         if left[i] < right[j]: #가장 작은거부터 비교(0번째는 최소값)
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# mergeArr = [4,1,3,9,7]
# print(merge_sort(mergeArr))


# #6 퀵 정렬
#     # 중간값을 고른 뒤 그 기준 좌 우로 정렬
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr) // 2]  # 가운데 피벗
#     # print(pivot)
#     left = [x for x in arr if x < pivot]
#     mid  = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
    
#     return quick_sort(left) + mid + quick_sort(right)

# quickArr = [4,1,7,3,8,2]
# print(quick_sort(quickArr))


# #7 기수 정렬
#     #숫자를 자리수별로 정렬하는 방식 (1의자리부터 큰자리수로)
#     #계수정렬을 사용해 정렬한다. 기수정렬이 digit값 올려줌

#     #계수정렬, ex)일의자리값으로만 비교한다
# def counting_sort_by_digit(arr, digit):
#     count = [0] * 10   # 0~9 숫자 카운팅
#     output = [0] * len(arr)

#     # 해당 자리수의 숫자 추출 후 카운트
#     for num in arr:
#         idx = (num // digit) % 10
#         count[idx] += 1

#     # 누적합으로 변경
#     for i in range(1, 10):
#         count[i] += count[i - 1]

#     # 뒤에서부터 안정적으로 정렬
#     for num in reversed(arr):
#         idx = (num // digit) % 10
#         count[idx] -= 1
#         output[count[idx]] = num

#     return output


# def radix_sort(arr):
#     max_val = max(arr)
#     digit = 1

#     while max_val // digit > 0:
#         arr = counting_sort_by_digit(arr, digit)
#         digit *= 10

#     return arr

# radixArr = [170, 45, 75, 90, 802, 24, 2, 66]
# print(radix_sort(radixArr))


#8 외부 정렬
