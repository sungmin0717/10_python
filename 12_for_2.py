# 구구단 출력해보기 

# for 변수 in days:
#     print(f"{변수}요일 입니다")
#range(시작숫자 , 마지막숫자) 숫자 순차적 매김


#for문 안에 for문 적용 가능
for i in range(2,10):
  print(i, "단 끝====================")
  for j in range(1, 10):
    print(f"{i} X {j} = {i * j}")