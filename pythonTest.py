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