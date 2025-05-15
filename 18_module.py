#파이썬에는 수많은 모듈이있음.

#하나에 파일로 만들어서 저장하는것이 모듈이다.

#모듈 불러오기
import time
#시간 라이브러리
import random
#랜덤 라이브러리
import datetime
#시간 라이브러리
import os
#운영체제와 상호 작용

# print(1)
# time.sleep(2) #시간을 멈춤.
# print(2)

# for i in range(1,10):
#   print(f"{i}, Hi!!")
#   time.sleep(1)
#==================================


#랜덤한 소수 숫자 생성==============
# x = random.random()
# x = random.randint(1, 10)
# print("랜덤한 숫자 입니다 : ", x)


#list 형태 랜덤 변환==========================
# a = [1,2,3,4,5,6,7,8,9]
# random.shuffle(a)
# print(a)

#list 하나만 빼와서 랜덤 숫자 =================
# a = [1,2,3,4,5,6,7,8,9]
# y = random.choice(a)
#choice를 활용하여 하나만 가져오기
# s = random.sample(a, 3)
# sample 활용하여 여러개 가져오기 가능
# print(s)


#시간 불러오기 ==========================

# today = datetime.date.today()
# print(today.day)


# 운영체제 상호 작용 =====================

# print(os.getcwd())
#디렉토리 경로
# print(os.listdir())
#디렉토리에 어떤 파일이 있는지 확인.