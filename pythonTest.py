#1~5 : 난이도(하)
#1. 홀짝 판별하기
# num = int(input("숫자를 입력하시오 : "))
# if num%2 == 0:
#     print(f"{num}은 짝수입니다.")
# else:
#     print(f"{num}은 홀수입니다.")

#2. 구구단 출력하기
# num = int(input("숫자를 입력하시오 : "))
# for i in range(1,10):
#     print(f"{num}*{i}={num*i}")

#3. 리스트에서 최대값 찾기
# list = [10,23,5,99,2]
# maximum = list[0]
# for i in range(len(list)):
#     if list[i]>maximum:
#         maximum = list[i]
# print(f"가장 큰 값은 {maximum}")

#4. 문자열 뒤집기
# text = input("문자열을 입력하시오 : ")
# reverse = []
# for i in range(len(text)):
#     reverse.append(text[len(text)-i-1])
# reverse_text = ", ".join(map(str, reverse))
# print(f"뒤집힌 문자열은 {reverse_text}입니다")

#5. 1부터 N까지 합 구하기
# num = int(input("숫자를 입력하시오 : "))
# total = 0
# for i in range(1,num+1):
#     total += i
# print(f"1부터{num}의 합은 {total}입니다.")

#6~10 : 난이도(중하)
#6. Palindrome판별하기 
# pal = input("문자열을 입력하세요 : ")
# isPal = True
# for i in range(int(len(pal)/2)):
#     if pal[i] != pal[-i-1]:
#         isPal = False
#         break
# if isPal:
#     print(f"{pal}은 palindrome입니다")
# else:
#     print(f"{pal}은 palindrome이 아닙니다")
"""
문자열 뒤집기인 list[::-1]을 사용하면 간단해짐
"""
# pal = input("문자열을 입력하세요 : ")
# if pal == pal[::-1]:
#     print(f"{pal}은 palindrome입니다")
# else:
#     print(f"{pal}은 palindrome이 아닙니다")

#7. 리스트 중복 제거하기
# numbers = [4,2,9,2,1,4,7]
# numbers.sort()
# sortedNumbers = []
# for i in range(len(numbers)):
#     if i ==0 or numbers[i] != numbers[i-1]:
#         sortedNumbers.append(numbers[i])
# print(f"정렬 및 중복 제거 결과 : {sortedNumbers}")
"""
>> 마찬가지로 i-1이 문제를 일으킬 수 있음 => 처음 i=0일때는
    성립하도록 i==0 or을 넣어 해결
>> set()함수를 사용해 중복을 제거
"""
# numbers = [4,2,9,2,1,4,7]
# sortedNumbers = sorted(set(numbers))
# print(f"정렬 및 중복 제거 결과 : {sortedNumbers}")

#8. 단어 개수 세기
# text = input("문자열을 입력하시오 : ")
# count = 1
# for i in range(len(text)):
#     if text[i] == " " and text[i] != text[i-1]:
#         count += 1
# print(f"{text}의 단어 갯수는 {count}개 입니다.")
"""
>> i-1이라는 끝자리 여부에 따라 오류 발생 가능
>> 첫 글자가 공백이면 count = 1로 시작하는 것이 오류 발생 가능
>> .split()을 쓰면 쉽게 풀 수 있음
>> .strip()을 쓰면 앞뒤 공백을 없앨 수 있음
"""
# text = input("문자열을 입력하시오 : ").strip()
# words = text.split()
# print(f"{text}의 단어 개수는 {len(words)}개 입니다.")
#9. 소수 판별하기
# isPrime = False
# prime = int(input("숫자를 입력하시오 : "))
# pri = int(prime/2)
# if prime>2:
#     for i in range(2,pri+1):
#         if prime % i == 0:
#             isPrime = False
#             break
#         isPrime = True
# elif prime==2:
#     isPrime = True

# if isPrime:
#     print(f"{prime}은 소수입니다")
# else:
#     print(f"{prime}은 소수가 아닙니다")
"""
>> 좋은디 루트를 써서 더 가볍게 가능
>> 100번째 줄에서 의미없이 계속 True를 넣는 비효율 발생
   초기값을 True로 설정하면 더 효과적으로 가능
"""
# isPrime = True
# prime = int(input("숫자를 입력하시오 : "))
# pri = int(prime/2)
# if prime < 2:
#     isPrime = False
# elif prime > 2:
#     for i in range(2, pri+1):
#         if prime % i == 0:
#             isPrime = False
#             break
# if isPrime:
#     print(f"{prime}은 소수입니다")
# else:
#     print(f"{prime}은 소수가 아닙니다")
""""
>> 루트써서 pri없애면
"""
# prime = int(input("숫자를 입력하시오 : "))
# isPrime = True
# if prime < 2:
#     isPrime = False
# else:
#     for i in range(2, int(prime**0.5) + 1):  # √n까지만 검사
#         if prime % i == 0:
#             isPrime = False
#             break
# if isPrime:
#     print(f"{prime}은 소수입니다")
# else:
#     print(f"{prime}은 소수가 아닙니다")
# isPrime = True
# prime = int(input("숫자를 입력하시오 : "))
# if prime < 2:
#     isPrime = False
# else:
#     for i in range(2, int(prime**0.5) + 1):
#         if prime % i == 0:
#             isPrime = False
#             break
# if isPrime:
#     print(f"{prime}은 소수입니다")
# else:
#     print(f"{prime}은 소수가 아닙니다")

#10. 피보나치 수열 구하기
# num = int(input("피보나치 값을 입력하시오 : "))
# plist = []
# for i in range(num):
#     if i < 2:
#         plist.append(i)
#     else:
#         plist.append(plist[i-1] + plist[i-2])
# print(f"피보나치 수열 : {plist}")
#ㅜㅜ