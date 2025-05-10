"""만약 오늘 === 월요일 : 
  출근한다.
  만약 오늘 == 일요일 :
    더잔다.
  """

today = "월요일"

#월요일이라면 출근해야지
if today == "월요일" :
    print("출근해야지.")
elif today == "일요일" :   #else if 
    print("더잔다.")
else :
    print("무슨요일이지")



todayNum = 24

#월요일이라면 출근해야지
if todayNum < 30 :
    print("돈이 없네.")
elif todayNum == 30 :   #else if 
    print("곧 월급 들어온다.")
else :
    print("무슨요일이지?")


#false true

pizza = True
hamburger = True

if pizza :
    print("야호 피자다")
elif hamburger :  # if 라면 else if 가 아니라 if 가 두개라 두개다 출력
    print("야호 햄버거다 !!")
else :
    print("아 배고파")