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
"""
>> map()함수는 리스트,튜플 등에 쓰임
>> 반복문 없이 처리가 가능
>> .map(함수, 리스트 등)으로 사용
"""
#map 예제
# words = ["apple", "banana", "kiwi"]
# lengths = list(map(len, words))
# print(lengths)  # [5, 6, 4]

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

#11. 단어 빈도수 세기(dict)
# txtC = "apple banna apple orange apple banna"
# freq =  {}
# for word in txtC.split():
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print(freq)
# print(f"apple 갯수는 {freq["apple"]}")
# print(f"apple 갯수는 {freq.get("apple")}")

#12. 소인수분해
# soinsu = int(input("소인수 분해 할 숫자를 입력하시오 : "))
# solist = []
# if soinsu > 1:
#     i = 2
#     while i <= soinsu:
#         if soinsu % i == 0:
#             solist.append(i)
#             soinsu = soinsu / i
#         else:
#             i += 1
# print(solist)

#13. 팰린드롬 문장 판별(공백, 대소문자 무시)
# isPal = input("팰린드롬 판별할 문장 입력해봐 : ")
# isPal = isPal.lower()
# isPal = isPal.replace(" ","")
# if isPal == isPal[::-1]:
#     print(f"{isPal}은 palindrome입니다")
# else:
#     print(f"{isPal}은 palindrome이 아닙니다")
"""
>> .lower() 함수와 .replace("뭐를", "뭐로") 기억하자
"""

#14. 아나그램 판별하기(sorted)
# str1 = "해준백멋지다"
# str2 = "지다멋준해백"
# if sorted(str1) == sorted(str2):
#     print(f"{str1}과 {str2}는 아나그램입니다.")
# else:
#     print(f"{str1}과 {str2}는 아나그램이 아닙니다.")

#15. 2차원 리스트 90도 회전
# twodim = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]
# rtwodim = []
# for i in range(len(twodim)):
#     for j in range(len(twodim[1])):
#         rtwodim.append(twodim[-j-1][i])
# print(rtwodim)
"""
>> 계속 append쓰니깐 1차원이 되어버림 한줄마다 리스트써서 넣어주려면 리스트 하나더 필요
"""
# twodim = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]
# rtwodim = []
# for i in range(len(twodim)):
#     row=[]
#     for j in range(len(twodim[1])):
#         row.append(twodim[-j-1][i])
#     rtwodim.append(row)
# print(rtwodim)