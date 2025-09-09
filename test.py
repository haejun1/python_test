<<<<<<< HEAD
# print("hello world")

# a = 5
# b = 3
# print(a+b)

# name = input("이름 뭐야?")
# print("안녕", name)

# num = int(input("숫자 입력 : "))

# if num %2 == 0:
#     print(num,"은 짝수다")
# else:
#     print(num,"은 홀수다")

# dan = int(input("몇 단 출력할까? "))
# for i in range(1,10):
#     print(f"{dan} x {i} = {dan*i}")

# import random

# answer = random.randint(1,10)
# guess = int(input("1부터 10 사이 숫자 맞혀봐"))
# if guess == answer:
#     print("정답이다")
# else:
#     print(f"틀렸다. 정답은 {answer}이다")

# num = int(input("소수인지 확인할 숫자를 입력하세요: "))
# is_prime = True

# if num < 2 :
#     is_prime = False
# else:
#     for i in range(2, int(num**0.5)+1):
#         if num%i==0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{num}은 소수입니다.")
# else:
#     print(f"{num}은 소수가 아닙니다.")


scores = []

n = int(input("학생 수를 입력하세요: "))
for i in range(n):
    score = int(input(f"{i+1}번 학생의 점수를 입력하세요: "))
    scores.append(score)

average = sum(scores)/n
highest = max(scores)

print(f"평균점수는 {average:.2f}")
print(f"최고점수는 {highest}")

