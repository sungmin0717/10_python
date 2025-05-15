
#함수를 만들어서 사용 가능
#def define 정의하다

def add(a,b):
  print(f"{a}와 {b}를 입력받았습니다.")
  print(f"두 값을 더하면 {a+b}입니다.")
  return a+b
#return 입력 받은 값을 돌려줌
temp = add(5,10)
# print(temp)
#함수를 쓰고 값을 넣을수있음
# add(temp, 100)
# 변수를 다시 사용 가능
print(f"합은 : {temp}")




#사용 하는 이유 함수를 만들어서 사용하기 때문에 간편하고 간결하게 사용 가능


# a = print("Hi!")
# b = input("입력 : ")

# print(a)
#print는 만들어내고 남기는것이 아님
# print(b)
#input 은 만들어내고 남겨둠