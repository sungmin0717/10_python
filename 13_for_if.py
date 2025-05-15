#반복문 조건문 함께 사용


#숫자에 범위를 정한뒤 짝수,홀수인지 판별 후 출력


# for i in range(1, 21):
#   # print(i)
#   if i % 2 == 0:
#     print(f"{i}짝수입니다.")
#   else:
#     print(f"{i}홀수입니다.")


for i in range(1, 31):
  if i % 3 == 0 and i % 5 == 0 :
    print(f"{i}는 3과5의 배수입니다.")
  # print(i)
  elif i % 3 == 0:
    print(f"{i}는 3의 배수입니다.")
  #5의 배수 
  elif i % 5 == 0:
    print(f"{i}는 5의 배수입니다.")
